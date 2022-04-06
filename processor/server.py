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
    weather = weather_info.get('weather')
    weather_info['weather_icon'] = WEATHER_TABLE.get(weather)
    winddirection = weather_info.get('winddirection')
    weather_info['winddirection_icon'] = WEATHER_TABLE.get(winddirection)
    return jsonify(weather_info)


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
    return jsonify(forecast_list)


@app.route('/temp_hum/', methods=['GET', 'POST'])
def temp_hum():
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
            else:
                ret_dict.update(data)
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
    info_dict = {'status': 1}
    if not info:
        info_dict = {'status': 0}
    else:
        info_dict.update(info)
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
    try:
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
    except KeyError:
        day_info_dict['status'] = 2
        day_info_dict['nongli'] = day_info.get('nongLi')
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


if __name__ == '__main__':
    app.debug = True
    app.run()
