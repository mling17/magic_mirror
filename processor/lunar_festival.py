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
        # http://api.xlongwei.com/service/datetime/workday.json?type=info&day=2022-05-05
        url = 'http://api.xlongwei.com/service/datetime/workday.json?%s' % params
        try:
            info = requests.get(url, headers=choice(HEADERS)).json()
            return info
        except Exception as e:
            pass

    def get_day_info(self, **kwargs):
        import requests

        cookies = {
            '__gads': 'ID=33003fec839c50b4-222d14649be00057:T=1683254230:RT=1683254230:S=ALNI_MaOdrY89bXDxv2fjmkVH4PewGe0EQ',
            '__gpi': 'UID=00000c01b75cac7d:T=1683254230:RT=1683254230:S=ALNI_MaEjTkTfQrDkfggIXJT0e4-zGZdyQ',
        }

        headers = {
            'authority': 'v.api.aa1.cn',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cache-control': 'no-cache',
            # 'cookie': '__gads=ID=33003fec839c50b4-222d14649be00057:T=1683254230:RT=1683254230:S=ALNI_MaOdrY89bXDxv2fjmkVH4PewGe0EQ; __gpi=UID=00000c01b75cac7d:T=1683254230:RT=1683254230:S=ALNI_MaEjTkTfQrDkfggIXJT0e4-zGZdyQ',
            'pragma': 'no-cache',
            'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'cross-site',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        }
        try:
            response = requests.get('https://v.api.aa1.cn/api/nl/', cookies=cookies, headers=headers)
            return response.json()
        except Exception as e:
            pass

    def get_day_info_2(self, **kwargs):
        params = urlencode(kwargs)
        url = 'https://www.iamwawa.cn/nongli/api?%s' % params
        try:
            print(url)
            info = requests.get(url, headers=choice(HEADERS)).json()
            print(info)
            return info
        except Exception as e:
            print(e)
            pass

    def run(self):
        while True:
            day_info = self.redis.hget('day_info', 'day')
            redis_day = None if day_info is None else day_info.strip('"').split('-')[-1]
            today = datetime.date.today()
            today_day = str(today.day)
            if redis_day != today_day:
                info_dict = self.get_day_info(type='info', day=datetime.date.today())
                # info_dict = self.get_day_info_2(type='solar', year=today.year, month=today.month, day=today_day)
                # print(info_dict)
                redis_day is not None and self.redis.delete('day_info')
                if info_dict:
                    for k, v in info_dict.items():
                        info_dict[k] = json.dumps(v, ensure_ascii=False).strip('"')
                    self.redis.hmset('day_info', info_dict)
            else:
                time.sleep(min(get_rest_second(), CYCLE_LUNAR))


if __name__ == '__main__':
    obj = DateInfo()
    obj.run()
#     # print(__file__)
