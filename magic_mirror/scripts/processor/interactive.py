import time
from tools import sentence  # 一句话
from tools import live  # 出生到现在的天数
from tools import history  # 历史上的今天
import random
from tools.redis_connection import r
from tools.seconds_to_tomorrow import seconds_to_tomorrow

display_list = []


def log(message):
    msg = "[%s] 更新了%s" % (time.ctime(), message)
    print(msg)


def get_data():
    sentence_string = sentence.onePhrase()
    live_days_string = live.live_days()
    history_list = history.history()
    display_list.append(sentence_string)
    display_list.append(live_days_string)
    display_list.extend(history_list)
    random.shuffle(history_list)
    for item in display_list:
        r.rpush('interactive_list', item)
    log(display_list)
    ex = seconds_to_tomorrow()
    r.expire('interactive_list', ex)


def main():
    get_data()


if __name__ == '__main__':
    get_data()
