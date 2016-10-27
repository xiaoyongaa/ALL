import redis
# pool=redis.ConnectionPool(host="10.0.0.25",port=6379)
# r=redis.Redis(connection_pool=pool)
# r.set("foo","bar")
# print(r.get("foo"))

class RedisHelper:
    def __init__(self):
        self.__conn = redis.Redis(host='10.0.0.25',port=6379)

    def public(self,chan,msg):
        self.__conn.publish(chan,msg)
        return True

    def subscribe(self,chan):
        pub = self.__conn.pubsub()
        pub.subscribe(chan)
        pub.parse_response()
        return pub

