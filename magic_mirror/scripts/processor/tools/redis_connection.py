import redis

pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
r = redis.Redis(connection_pool=pool, decode_responses=True, encoding='utf-8', charset='utf-8')
