from rediss import RedisClient

redis = RedisClient()
redis.db.hset('house_temp_hum', mapping={'temp': 18, 'hum': 50})
