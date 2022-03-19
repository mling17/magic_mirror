import json
from tools.weather import ThirdPartInfo
from tools.redis_connection import r
import time


def log(message):
    msg = "[%s] 更新了%s" % (time.ctime(), message)
    print(msg)


def main():
    with open('/home/pi/magic_mirror/scripts/config.json', "r") as f:
        location = json.load(f).get('location')
    obj = ThirdPartInfo()
    if not location:
        ip = obj.GetOuterIP()
        location = obj.IPLocation(ip)
    weather_info = obj.weather(locate=location)
    forecast = obj.forecast()
    # weather_info = {'province': '山东', 'city': '潍坊市', 'adcode': '370700', 'weather': '多云', 'temperature': '32',
    #                 'winddirection': '东南', 'windpower': '4', 'humidity': '50', 'reporttime': '2021-07-21 13:31:35'}
    if weather_info:
        log(weather_info)
        r.hmset('weather_info', weather_info)
    if forecast:
        for index, item in enumerate(forecast, 1):
            r.hmset('forecast_%s' % index, item)


if __name__ == '__main__':
    main()
