from processor.redis_conn import RedisClient

r = RedisClient().db
print(r.hgetall('house_temp_hum'))
