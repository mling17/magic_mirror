import platform
from os.path import dirname, abspath, join
from environs import Env

# from loguru import logger


env = Env()
env.read_env()

# redis host
REDIS_HOST = env.str('PROXYPOOL_REDIS_HOST',
                     env.str('REDIS_HOST', '127.0.0.1'))
# redis port
REDIS_PORT = env.int('PROXYPOOL_REDIS_PORT', env.int('REDIS_PORT', 6379))
# redis password, if no password, set it to None
REDIS_PASSWORD = env.str('PROXYPOOL_REDIS_PASSWORD',
                         env.str('REDIS_PASSWORD', None))
# redis db, if no choice, set it to 0
REDIS_DB = env.int('PROXYPOOL_REDIS_DB', env.int('REDIS_DB', 0))

REDIS_CONNECTION_STRING = env.str(
    'REDIS_CONNECTION_STRING', env.str('REDIS_CONNECTION_STRING', None))
REDIS_KEY = env.str('REDIS_KEY', env.str(
    'REDIS_KEY', 'proxies:universal'))
# read location，weather use it.
LOCATION = env.str('PI_LOCATION', '潍坊')

# enable switch
ENABLE_PI = True
ENABLE_WEATHER = True
ENABLE_DHT11 = True
ENABLE_FAN = True
ENABLE_PI_INFO = True
# cycle time set.
CYCLE_INFO = 10  # 获取pi信息的频率
CYCLE_DHT11 = 60 * 30  # 获取室内温湿度的频率
CYCLE_FAN = 10  # 风扇检测频率
CYCLE_WEATHER = 60 * 30  # 获取天气信息的频率
# dht11
GPIO_DHT11 = 17
TEMP_HUM_API = "http://127.0.0.1:8000/temp_hum/"
TEMP_HUM_STORAGE = False

# fan
GPIO_FAN = 26  # 风扇GPIO引脚
FAN_HIGH_TEMP = 65  # 风扇散热温度
FAN_LOW_TEMP = 55  # 风扇停止温度
FAN_ENABLE_TIME = (6, 22)  # 风扇使能时间段，范围0-23，(0,0)表示全天
# server
API_HOST = env.str('API_HOST', '0.0.0.0')
API_PORT = env.int('API_PORT', 5555)
API_THREADED = env.bool('API_THREADED', True)
IS_DEV = True
