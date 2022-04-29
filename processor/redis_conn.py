import redis
from settings import REDIS_CONNECTION_STRING, REDIS_HOST, REDIS_PORT, REDIS_PASSWORD, REDIS_DB

REDIS_CLIENT_VERSION = redis.__version__
IS_REDIS_VERSION_2 = REDIS_CLIENT_VERSION.startswith('2.')


class RedisClient(object):
    """
    redis connection client of pool
    """

    def __init__(self, host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD, db=REDIS_DB,
                 connection_string=REDIS_CONNECTION_STRING, **kwargs):
        """
        init redis client
        :param host: redis host
        :param port: redis port
        :param password: redis password
        :param connection_string: redis connection_string
        """
        # if set connection_string, just use it
        if connection_string:
            self.db = redis.StrictRedis.from_url(connection_string, decode_responses=False, **kwargs)
        else:
            self.db = redis.StrictRedis(
                host=host, port=port, password=password, db=db, decode_responses=True, **kwargs)

    def del_key(self, key):
        self.db.delete(key)


conn = RedisClient()
if __name__ == '__main__':
    conn = RedisClient()
    # result = conn.random()
    # print(result)
