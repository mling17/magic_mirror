import time
import datetime


def seconds_to_tomorrow():
    today = datetime.date.today()
    tomorrow = today.replace(day=today.day + 1)
    tomorrow = datetime.datetime(year=tomorrow.year, month=tomorrow.month, day=tomorrow.day)
    ex = round(tomorrow.timestamp() - time.time())
    return ex
