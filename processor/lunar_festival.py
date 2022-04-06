"""
获取农历和节日
"""
import datetime
import json
import time
from random import choice
from urllib.parse import urlencode

import requests

from constant import HEADERS
from settings import CYCLE_LUNAR
from utiles import get_rest_second
from .redis_conn import RedisClient


#
# class RedisClient(object):
#     """
#     redis connection client of proxypool
#     """
#
#     def __init__(self, ):
#         import redis
#         self.db = redis.StrictRedis()


# type_list = [
#     'isworkday',  # 是否工作日
#     # 'nextworkday,'  # 遇工作日顺延
#     # 'offsetworkday'  # 增减offset个工作日，skipweekend是否跳过周末
#     # 'offsetday',  # 增减offset个自然日
#     'countworkday',  # 计算start~day之间有几个工作日
#     'countday',  # 计算start~day之间有几个自然日
#     'isholiday',  # 是否节假日
#     'holiday',  # 节假日信息
#     'isweekend',  # 是否周末
#     'convert',  # 阳历与农历互转
#     'nongli',  # 阳历转农历
#     'yangli',  # 农历转阳历
#     'info',  # 日期信息
#     'calendar'
# ]


class DateInfo:
    def __init__(self):
        self.flag = False
        self.redis = RedisClient().db

    def get_day_info(self, **kwargs):
        params = urlencode(kwargs)
        url = 'http://api.xlongwei.com/service/datetime/workday.json?%s' % params
        try:
            info = requests.get(url, headers=choice(HEADERS)).json()
            return info
        except Exception as e:
            pass

    def run(self):
        while True:
            day_info = self.redis.hget('day_info', 'day')
            redis_day = None if day_info is None else day_info.decode('utf-8').strip('"').split('-')[-1]
            today_day = str(datetime.date.today().day)
            if redis_day != today_day:
                info_dict = self.get_day_info(type='info', day=datetime.date.today())
                redis_day is not None and self.redis.delete('day_info')
                if info_dict:
                    for k, v in info_dict.items():
                        info_dict[k] = json.dumps(v, ensure_ascii=False)
                    self.redis.hmset('day_info', info_dict)
            else:
                time.sleep(min(get_rest_second(), CYCLE_LUNAR))


if __name__ == '__main__':
    obj = DateInfo()
    obj.run()
#     # print(__file__)
