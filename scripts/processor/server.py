"""
apis:
完成：http://127.0.0.1:8000/
完成：http://127.0.0.1:8000/weather/
完成：http://127.0.0.1:8000/forecast/
完成GET：http://127.0.0.1:8000/temp_hum/   #GET,POST
http://127.0.0.1:8000/todo/
完成：http://127.0.0.1:8000/pi_info/
完成：http://127.0.0.1:8000/lunar/
"""
import json
import redis
import datetime
from flask import Flask, request, render_template, jsonify, g
from tools.weather_table import weather_table, wind_direct

# from .redis_conn import RedisClient
# from ..settings import API_HOST, API_PORT, API_THREADED, IS_DEV
lunar_solar_month = {
    1: '正',
    2: '二',
    3: '三',
    4: '四',
    5: '五',
    6: '六',
    7: '七',
    8: '八',
    9: '九',
    10: '十',
    11: '冬',
    12: '腊',
}
lunar_solar_day = {
    1: '初一',
    2: '初二',
    3: '初三',
    4: '初四',
    5: '初五',
    6: '初六',
    7: '初七',
    8: '初八',
    9: '初九',
    10: '初十',
    11: '十一',
    12: '十二',
    13: '十三',
    14: '十四',
    15: '十五',
    16: '十六',
    17: '十七',
    18: '十八',
    19: '十九',
    20: '廿',
    21: '廿一',
    22: '廿二',
    23: '廿三',
    24: '廿四',
    25: '廿五',
    26: '廿六',
    27: '廿七',
    28: '廿八',
    29: '廿九',
    30: '三十',
}
__all__ = ['app']

app = Flask(__name__)


# if IS_DEV:
#     app.debug = True


def get_conn():
    """
    get redis client object
    :return:
    """
    if not hasattr(g, 'redis'):
        # g.redis = RedisClient()
        # g.redis = redis.StrictRedis('192.168.1.4')
        g.redis = redis.StrictRedis('127.0.0.1')
    return g.redis


@app.route('/')
def index():
    """
    get home page, you can define your own templates
    :return:
    """
    return render_template('index.html')


@app.route('/weather/')
def weather():
    """
    get weather info
    :return: get a random proxy
    """
    r = get_conn()
    weather_info = r.hgetall('weather_info')
    weather_info_dict = {}
    for k, v in weather_info.items():
        k = k.decode('utf-8')
        v = v.decode('utf-8')
        weather_info_dict[k] = v
        if k == 'weather':
            weather_info_dict['weather_icon'] = weather_table.get(v)
        if k == 'winddirection':
            weather_info_dict['winddirection_icon'] = wind_direct.get(v)
    return jsonify(weather_info_dict)


@app.route('/forecast/')
def forecast():
    """
    未来三天天气预报
    """
    r = get_conn()
    forecast_1 = r.hgetall('forecast_1')
    forecast_2 = r.hgetall('forecast_2')
    forecast_3 = r.hgetall('forecast_3')
    forecast_list = [forecast_1, forecast_2, forecast_3]
    forecast_info = []
    for forecast_data in forecast_list:
        forecast_info_dict = {}
        for k, v in forecast_data.items():
            k = k.decode('utf-8')
            v = v.decode('utf-8')
            forecast_info_dict[k] = v
        forecast_info.append(forecast_info_dict)
    return jsonify(forecast_info)


@app.route('/temp_hum/', methods=['GET', 'POST'])
def get_count():
    """
    上传或获取室内温湿度
    """
    r = get_conn()
    if request.method == 'GET':
        ret_dict = {'status': 1}
        try:
            data = r.hgetall('house_temp_hum')
            if not data:
                ret_dict['status'] = 0
            for k, v in data.items():
                k = k.decode('utf-8')
                v = v.decode('utf-8')
                ret_dict[k] = v
        except Exception as e:
            ret_dict['status'] = 0
        return jsonify(ret_dict)


@app.route('/pi_info/')
def pi_info():
    """
    树莓派运行信息
    """
    r = get_conn()
    info = r.hgetall('pi_info')
    info_dict = {}
    for k, v in info.items():
        k = k.decode('utf-8')
        v = v.decode('utf-8')
        info_dict[k] = v
    return jsonify(info_dict)


@app.route('/lunar/')
def lunar():
    """
    农历信息
    status，0错误/无数据
    """
    r = get_conn()
    day_info = r.hgetall('day_info')
    day_info_dict = {'status': 1}
    if not day_info:
        day_info_dict['status'] = 0
        return jsonify(day_info_dict)
    for k, v in day_info.items():
        # print(k.decode('utf-8'), type(v.decode('utf-8')))
        try:
            day_info_dict[k.decode('utf-8')] = json.loads(v.decode('utf-8'))
        except json.decoder.JSONDecodeError:
            day_info_dict[k.decode('utf-8')] = ""
    is_leap_month = day_info_dict['isLeapMonth']
    lunar_month = lunar_solar_month.get(day_info_dict['lunarMonth'])
    if is_leap_month:
        lunar_month += '闰'
    day_info_dict['lunarMonth'] = lunar_month
    lunar_day = lunar_solar_day.get(day_info_dict['lunarDay'])
    day_info_dict["lunarDay"] = lunar_day
    is_holiday = day_info_dict['isholiday']
    if is_holiday is False:
        day_info_dict['holiday'] = ''
    return jsonify(day_info_dict)


@app.route('/todo/')
def todo():
    today = datetime.date.today()
    day = today.day
    # todo_list = models.ToDo.objects.filter(date__day=day).values('title', 'date', 'period', 'fix_day')
    # period_todo = models.ToDo.objects.filter(period__gt=0)
    todo_list = {'title': 'a', 'date': '2022-03-29', 'period': 0, 'fix_day': False}
    period_todo = {'title': 'a', 'date': '2022-03-29', 'period': 1, 'fix_day': False}
    return jsonify([])
    return jsonify([todo_list,period_todo])
    # ret_list = []
    # for item in period_todo:
    #     title = item.title
    #     date = item.date
    #     fix_day = item.fix_day
    #     period = item.period
    #     days = (date - today).days  # 间隔天数
    #     if not fix_day and days % period == 0:  # 间隔日期执行
    #         ret_list.insert(0, title)
    # for item in todo_list:
    #     title = item['title']
    #     date = item['date']
    #     fix_day = item['fix_day']
    #     if fix_day:  # 固定日期执行
    #         if date.month <= today.month and date.year <= today.year:
    #             ret_list.insert(0, title)
    #     if today.day == date.day and date.month == today.month and date.year == today.year:  # 执行一次
    #         if title not in ret_list:
    #             ret_list.insert(0, title)
    # return jsonify(ret_list)


if __name__ == '__main__':
    app.debug = True
    app.run()
