import datetime
import json
with open('/home/pi/magic_mirror/scripts/config.json', "r") as f:
    birthday = json.load(f).get('birthday')


def count_day(date1, date2=datetime.date.today()):
    try:
        year, month, day = date1.split('-')
        d1 = datetime.date(int(year), int(month), int(day))
        if isinstance(date2, datetime.date):
            d2 = date2
        else:
            year, month, day = date2.split('-')
            d2 = datetime.date(int(year), int(month), int(day))
        return abs((d1 - d2).days)
    except Exception as e:
        print(e)
        print('日期格式错误，yyyy-mm-dd')


def live_days():
    days = count_day(birthday)
    string = '您在这%s天过的还好吗?' % days
    return string
