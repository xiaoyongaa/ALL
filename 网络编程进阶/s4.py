import s3
obj=s3.RedisHelper()
data=obj.subscribe("7")  #订阅
print(data.parse_response())