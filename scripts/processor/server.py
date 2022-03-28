"""
apis:
http://127.0.0.1:8000/
http://127.0.0.1:8000/weather/
http://127.0.0.1:8000/forecast/
http://127.0.0.1:8000/temp_hum/   #GET,POST
http://127.0.0.1:8000/todo/
http://127.0.0.1:8000/pi_info/
http://127.0.0.1:8000/lunar/
"""
import redis
from flask import Flask, render_template, jsonify
from flask import Flask, g
from tools.weather_table import weather_table, wind_direct

# from .redis_conn import RedisClient
# from ..settings import API_HOST, API_PORT, API_THREADED, IS_DEV

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
        g.redis = redis.StrictRedis('127.0.0.1')
    return g.redis


@app.route('/')
def index():
    """
    get home page, you can define your own templates
    :return:
    """
    return render_template('index.html')


@app.route('/weather')
def weather():
    """
    get weather info
    :return: get a random proxy
    """
    conn = get_conn()
    weather_info = conn.hgetall('weather_info')
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
    return jsonify(weather_info_dict, safe=False)


@app.route('/all')
def get_proxy_all():
    """
    get a random proxy
    :return: get a random proxy
    """
    conn = get_conn()
    proxies = conn.all()
    proxies_string = ''
    if proxies:
        for proxy in proxies:
            proxies_string += str(proxy) + '\n'

    return proxies_string


@app.route('/count')
def get_count():
    """
    get the count of proxies
    :return: count, int
    """
    conn = get_conn()
    return str(conn.count())


if __name__ == '__main__':
    app.debug = True
    app.run()
