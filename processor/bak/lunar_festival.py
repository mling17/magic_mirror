"""
获取农历和节日
"""
import time
import requests
import datetime
import json
from urllib.parse import urlencode
from tools.seconds_to_tomorrow import seconds_to_tomorrow
from tools.redis_connection import r


def log(message):
    msg = "[%s] 更新了%s" % (time.ctime(), message)
    print(msg)


type_list = [
    'isworkday',  # 是否工作日
    # 'nextworkday,'  # 遇工作日顺延
    # 'offsetworkday'  # 增减offset个工作日，skipweekend是否跳过周末
    # 'offsetday',  # 增减offset个自然日
    'countworkday',  # 计算start~day之间有几个工作日
    'countday',  # 计算start~day之间有几个自然日
    'isholiday',  # 是否节假日
    'holiday',  # 节假日信息
    'isweekend',  # 是否周末
    'convert',  # 阳历与农历互转
    'nongli',  # 阳历转农历
    'yangli',  # 农历转阳历
    'info',  # 日期信息
    'calendar'
]


class DateInfo:
    def __init__(self):
        self.flag = False

    def get_day_info(self, **kwargs):
        params = urlencode(kwargs)
        url = 'http://api.xlongwei.com/service/datetime/workday.json?%s' % params
        print(url)
        try:
            info = requests.get(url).json()
            print(info)
            return info
        except Exception as e:
            pass

    def info(self):
        day_info = r.hget('day_info', 'day')
        today = datetime.date.today()

        if day_info is None:
            redis_day = None
        else:
            year, month, day = day_info.decode('utf-8').strip('"').split('-')
            redis_day = datetime.date(year=int(year), month=int(month), day=int(day))

        if redis_day != today:
            info_dict = self.get_day_info(type='info', day=datetime.date.today())
            for k, v in info_dict.items():
                info_dict[k] = json.dumps(v, ensure_ascii=False)
            log(info_dict)
            r.hmset('day_info', info_dict)
            ex = seconds_to_tomorrow()
            r.expire('day_info', ex)

    def main(self):
        # while True and not self.flag and not first:
        #     nt = datetime.datetime.now()
        #     # print(nt.minute, nt.second, sep=":")
        #     if nt.minute == 0 and nt.second == 0:
        #         self.flag = True
        #         break
        #     time.sleep(1)
        self.info()


if __name__ == '__main__':
    obj = DateInfo()
    obj.main()
#     # print(__file__)
