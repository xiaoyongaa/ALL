import redis
# pool=redis.Connection(host="10.0.0.25",port=6379)
# r=redis.Redis(connection_pool=pool)
# r.set("foo","bar")
# r=redis.Redis(host="10.0.0.25",port=6379)
# r.set("foo","bar")
# print(r.get("foo"))
pool=redis.ConnectionPool(host="10.0.0.25",port=6379)
r=redis.Redis(connection_pool=pool)
r.set("foo","bar")
res=r.get("foo")
print(res)


