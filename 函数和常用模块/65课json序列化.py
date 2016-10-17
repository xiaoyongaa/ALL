#序列化相关的
import json
import pickle
#li={"k1":"v1"}   #创建一个字典
#print(type(li))  #查看类型为字典
#将python的基本数据类型转换成字符串
#li=json.dumps(li) #jison序列化转换成字符串
#print(type(li))  #查看字符串
#将python的基本数据类型转换成字符串


#将字符串转换为字典
'''
k='{"k":123}'
print(type(k))
k=json.loads(k)
print(type(k))
'''
k='{"k":123}'
print(type(k))
k=json.dumps(k)
print(type(k))
print(k)
k=json.loads(k)
print(type(k))
print(k)


