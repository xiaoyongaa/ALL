import requests
import json
response=requests.get("http://wthrcdn.etouch.cn/weather_mini?city=北京") #获取所有信息
print(type(response))
response.encoding="utf-8"
print(response.text)  #只获取内容
print(type(response.text))

response=json.loads(response.text)
print(response)
print(type(response))