# Create your views here.
# Create your views here.
# coding:utf-8
import datetime
from django.http import JsonResponse, HttpResponse
from django_redis import get_redis_connection
from django.shortcuts import render
from mirror import models
import json
import redis
from scripts.tools.weather_table import weather_table, wind_direct

pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
r = redis.Redis(connection_pool=pool, encoding='utf-8', charset='utf-8', decode_responses=True)

conn = get_redis_connection('default')
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
    20: '二十',
    21: '二十一',
    22: '二十二',
    23: '二十三',
    24: '二十四',
    25: '二十五',
    26: '二十六',
    27: '二十七',
    28: '二十八',
    29: '二十九',
    30: '三十',
}


def interactive(request):
    contents = []

    length = r.llen('interactive_list')
    if length == 0:
        return JsonResponse(contents, safe=False)
    for i in range(5):
        content = r.lpop('interactive_list').decode('utf-8')
        if content is None:
            break
        contents.append(content)
        # print(content)
    return JsonResponse(contents, safe=False)


def get_lunar(request):
    day_info = r.hgetall('day_info')
    day_info_dict = {}
    if not day_info:
        return JsonResponse(day_info_dict, safe=True)
    for k, v in day_info.items():
        # print(k.decode('utf-8'), type(v.decode('utf-8')))
        try:
            day_info_dict[k.decode('utf-8')] = json.loads(v.decode('utf-8'))
        except json.decoder.JSONDecodeError:
            day_info_dict[k.decode('utf-8')] = ""
    isLeapMonth = day_info_dict['isLeapMonth']
    lunarMonth = lunar_solar_month.get(day_info_dict['lunarMonth'])
    if isLeapMonth:
        lunarMonth += '闰'
    day_info_dict['lunarMonth'] = lunarMonth

    lunarDay = lunar_solar_day.get(day_info_dict['lunarDay'])
    day_info_dict["lunarDay"] = lunarDay

    isholiday = day_info_dict['isholiday']
    if isholiday is False:
        day_info_dict['holiday'] = ''
    return JsonResponse(day_info_dict, safe=True)


def index(request):
    return render(request, 'index.html')


def weather(request):
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
    print(weather_info_dict)

    return JsonResponse(weather_info_dict, safe=False)


def forecast(request):
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
    return JsonResponse(forecast_info, safe=False)


def temp_hum(request):
    if request.method == 'GET':
        data = r.hgetall('house_temp_hum')
        ret_dict = {}
        for k, v in data.items():
            k = k.decode('utf-8')
            v = v.decode('utf-8')
            ret_dict[k] = v
        return JsonResponse(ret_dict, safe=False)
    temp = float(request.POST.get('temperature'))
    hum = float(request.POST.get('humidity'))
    try:
        r.hset('house_temp_hum', mapping={'temp': temp, 'hum': hum})
        models.TempHum.objects.create(temperature=temp, humidity=hum)
    except Exception as e:
        return HttpResponse(e)
    return HttpResponse('ok')


def todo(request):
    today = datetime.date.today()
    day = today.day
    todo_list = models.ToDo.objects.filter(date__day=day).values('title', 'date', 'period', 'fix_day')
    period_todo = models.ToDo.objects.filter(period__gt=0)

    ret_list = []
    for item in period_todo:
        title = item.title
        date = item.date
        fix_day = item.fix_day
        period = item.period
        days = (date - today).days  # 间隔天数
        if not fix_day and days % period == 0:  # 间隔日期执行
            ret_list.insert(0, title)
    for item in todo_list:
        title = item['title']
        date = item['date']
        fix_day = item['fix_day']
        if fix_day:  # 固定日期执行
            if date.month <= today.month and date.year <= today.year:
                ret_list.insert(0, title)
        if today.day == date.day and date.month == today.month and date.year == today.year:  # 执行一次
            if title not in ret_list:
                ret_list.insert(0, title)
    return JsonResponse(ret_list, safe=False)

def pi_info(request):
    info = r.hgetall('pi_info')
    info_dict = {}
    for k, v in info.items():
        k = k.decode('utf-8')
        v = v.decode('utf-8')
        info_dict[k] = v
    print(info_dict)
    return JsonResponse(info_dict, safe=False)