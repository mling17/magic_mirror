import platform
from os.path import dirname, abspath, join
from environs import Env
from loguru import logger

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

# read location，weather use it.
LOCATION = env.str('PI_LOCATION', '潍坊')
