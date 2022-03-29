"""
未完成：
http://127.0.0.1:8000/temp_hum/   # POST方法未完成
http://127.0.0.1:8000/todo/  # 读取mysql
"""
import json
import datetime
from flask import Flask, request, render_template, jsonify, g
from constant import WEATHER_TABLE, WIND_DIRECT, LUNAR_SOLAR_MONTH, LUNAR_SOLAR_DAY
from .redis_conn import RedisClient
from settings import API_HOST, API_PORT, API_THREADED, IS_DEV

__all__ = ['app']

app = Flask(__name__)

if IS_DEV:
    app.debug = True


def get_conn():
    """
    get redis client object
    :return:
    """
    if not hasattr(g, 'redis'):
        g.redis = RedisClient().db
        # g.redis = redis.StrictRedis('192.168.1.4')
        # g.redis = redis.StrictRedis('127.0.0.1')
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
            weather_info_dict['weather_icon'] = WEATHER_TABLE.get(v)
        if k == 'winddirection':
            weather_info_dict['winddirection_icon'] = WIND_DIRECT.get(v)
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
    lunar_month = LUNAR_SOLAR_MONTH.get(day_info_dict['lunarMonth'])
    if is_leap_month:
        lunar_month += '闰'
    day_info_dict['lunarMonth'] = lunar_month
    lunar_day = LUNAR_SOLAR_DAY.get(day_info_dict['lunarDay'])
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
    return jsonify([todo_list, period_todo])
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
