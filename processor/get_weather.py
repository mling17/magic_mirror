import time
import requests
from loguru import logger
from settings import LOCATION, CYCLE_WEATHER
from processor.redis_conn import conn as r_conn
from processor.mysql_conn import conn
from random import choice
from constant import HEADERS


class Weather(object):
    # 输入位置，查询天气
    def __init__(self):
        self.redis = r_conn.db
        # import redis
        # self.redis = self.db = redis.StrictRedis(host='127.0.0.1', port=6379)

    @staticmethod
    def get_stationid(district):
        district = district.strip().rstrip('县')
        sql = "select district,stationid from area_cn where district like %s or city like %s"
        result = conn.fetch_one(sql, (district, district))
        if not result:
            logger.error('未找到【%s】的地区ID，请检查地区设置是否正确。')
            return {'district': '北京', 'stationid': '101010100'}
        else:
            return result

    def weather(self, locate):
        """高德天气
        天气实况：天气，气温，风向，风力，湿度
        'lives': [{'province': '山东',
         'city': '潍坊市', 'adcode': '370700',
         'weather': '多云', 'temperature': '31', 'winddirection': '东南', 'windpower': '5', 'humidity': '64',
          'reporttime': '2021-07-17 15:31:33'}]
        :param locate:
        :return:
        """
        key = '4c5d8cfd09b55f48aee4a9f26e83aa75'
        url = 'https://restapi.amap.com/v3/weather/weatherInfo?key=%s&city=%s' % (key, locate)
        try:
            weather_dict = requests.get(url, headers=choice(HEADERS)).json()
            status = weather_dict.get('status')
            # print(status, type(status))
            if status == "1":
                return weather_dict['lives'][0]
            return {}
        except Exception as e:
            logger.error(e)
            return {}

    def forecast(self, locate):
        stationid = Weather.get_stationid(locate).get('stationid')
        url = 'https://www.weatherol.cn/api/home/getCurrAnd15dAnd24h?cityid=%s' % stationid
        # 'https://www.weatherol.cn/api/home/getCurrAnd15dAnd24h?cityid=101120601'
        try:
            r = requests.get(url, headers=choice(HEADERS)).json()
            return r['data']
            # return r['data']['forecast15d'][2:5]
        except Exception as e:
            logger.error(e)
            return {}

    def run(self):
        while True:
            weather_info = self.weather(locate=LOCATION)
            # weather_info = self.weather(locate='潍坊')
            # weather_info = {'province': '山东', 'city': '潍坊市', 'adcode': '370700', 'weather': '多云', 'temperature': '32',
            #                 'winddirection': '东南', 'windpower': '4', 'humidity': '50', 'reporttime': '2021-07-21 13:31:35'}
            if weather_info:
                self.redis.hmset('weather_info', weather_info)
                logger.info(
                    f'{weather_info["city"]}，{weather_info["weather"]}，{weather_info["winddirection"]}风{weather_info["windpower"]}级，气温{weather_info["temperature"]}℃，湿度{weather_info["humidity"]}%，更新时间{weather_info["reporttime"]}')
            weather_data = self.forecast(locate=LOCATION)
            current = weather_data['current']
            nongli = current.get('nongLi').split()[-1]
            tips = current.get('tips')
            self.redis.lpush('interactive', tips)
            self.redis.hset('day_info', 'nongLi', nongli)  # 如果获取农历API失效会使用此数据，前端不至于无显示
            forecast = weather_data.get('forecast15d')
            if forecast:
                for index, item in enumerate(forecast[2:5], 1):
                    self.redis.hmset('forecast_%s' % index, item)
                    logger.info(f'forecast_{index}--->{item}')
            time.sleep(CYCLE_WEATHER)


if __name__ == '__main__':
    Weather().run()
