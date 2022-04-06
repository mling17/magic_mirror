import datetime


def get_rest_second():
    """
    获取当前时间到第二天0时的秒数
    """
    now = datetime.datetime.now()
    today_begin = datetime.datetime(now.year, now.month, now.day, 0, 0, 0)
    tomorrow_begin = today_begin + datetime.timedelta(days=1)
    rest_seconds = (tomorrow_begin - now).seconds
    return rest_seconds
