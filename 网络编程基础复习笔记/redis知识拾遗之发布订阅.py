import redis
class Redishelps():
    def __init__(self):
        self.connect=redis.Redis(host="192.168.1.11")
    def publish(self,msg,chan):
        self.connect.publish(chan,msg)
    def subscribe(self,chan):
        pub=self.connect.pubsub()
        pub.subscribe(chan)
        pub.parse_response()
        return pub


obj=Redishelps()
obj.publish("sasda","fm110")
obj.subscribe("fm110").parse_response()


