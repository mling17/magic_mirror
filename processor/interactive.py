import time
import random
import requests
from constant import HEADERS
from loguru import logger
from processor.redis_conn import conn
from utiles import get_rest_second

taboo_words = ['逝世', '出生', ]  # 禁忌词


def has_taboo_word(string):
    for word in taboo_words:
        if word in string:
            return True
    return False


def get_json_data(url):
    try:
        r = requests.get(url, headers=random.choice(HEADERS))
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.json()
    except Exception as e:
        logger.error(e)
        return {}


class Interactive:
    def __init__(self):
        self.display_list = []

    def phrase(self):
        # 一个短句
        data = []
        url = 'https://v1.hitokoto.cn/?encode=json&charset=utf-8'
        count = 0
        while len(data) < 3 and count < 100:
            res = get_json_data(url).get('hitokoto').rstrip('。')
            if res:
                data.append(res)
            time.sleep(random.randint(0, 2))
            count += 1
        return data

    def history(self):
        # 历史上的今天
        url = 'https://www.ipip5.com/today/api.php?type=json'
        history_list = []
        res = get_json_data(url)
        if res:
            for item in res['result']:
                year = item.get('year')
                title = item.get('title').rstrip('。')
                if has_taboo_word(title):
                    continue
                history_list.append(f'{year}年-{title}')
        return history_list[:-1]

    def poetry(self):
        # 诗词
        url = 'https://v2.jinrishici.com/one.json?client=browser-sdk/1.2&X-User-Token=A6BZsFOV4Ga2HnAPX8sl3IOnROMqI7Zb'
        data = []
        count = 0
        while len(data) < 3 and count < 100:
            res = get_json_data(url)
            if res and res['status'] == 'success':
                data.append(res['data']['content'].rstrip('。'))
            time.sleep(random.randint(0, 2))
            count += 1
        return data

    def run(self):
        while True:
            conn.del_key('interactive')
            ph = self.phrase()  # list
            hi = self.history()  # list
            po = self.poetry()  # list
            logger.info(f'添加金句：{",".join(ph)}')
            logger.info(f'历史上的今天：{",".join(hi)}')
            logger.info(f'今日诗词：{",".join(po)}')
            self.display_list = []
            self.display_list.extend(ph)
            self.display_list.extend(po)
            for i in hi:
                if len(i) < 40:
                    self.display_list.append(i)
            for item in self.display_list:
                conn.db.rpush('interactive', item)
            time.sleep(get_rest_second())


if __name__ == '__main__':
    Interactive().run()
