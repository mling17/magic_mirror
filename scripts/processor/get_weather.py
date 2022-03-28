import time
import requests
from loguru import logger
from settings import LOCATION, CYCLE_WEATHER
from .redis_conn import RedisClient


class Weather(object):
    # 输入位置，查询天气
    def __init__(self):
        self.redis = RedisClient().db
        # import redis
        # self.redis = self.db = redis.StrictRedis(host='127.0.0.1', port=6379)

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
            weather_dict = requests.get(url).json()
            status = weather_dict.get('status')
            # print(status, type(status))
            if status == "1":
                return weather_dict['lives'][0]
            return {}
        except Exception as e:
            logger.error(e)
            return {}

    def forecast(self):
        # todo city id
        url = 'https://www.weatherol.cn/api/home/getCurrAnd15dAnd24h?cityid=101120601'
        try:
            r = requests.get(url).json()
            return r['data']['forecast15d'][2:5]
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
            forecast = self.forecast()
            if forecast:
                for index, item in enumerate(forecast, 1):
                    self.redis.hmset('forecast_%s' % index, item)
                    logger.info(f'forecast_{index}--->{item}')
            time.sleep(CYCLE_WEATHER)


if __name__ == '__main__':
    Weather().run()
