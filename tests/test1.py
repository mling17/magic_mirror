class RedisClient(object):
    """
    redis connection client of proxypool
    """

    def __init__(self, ):
        import redis
        self.db = redis.StrictRedis()


r = RedisClient().db
# res = r.delete('day_info')
res = r.hset('weather_info','winddirection','西北')
print(res)
