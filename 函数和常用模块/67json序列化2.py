import json
li='{"ds":"2121"}'
json.dump(li,open("li","w"))  #序列化li，把li转换为字符串写进文件
l=json.load(open("li","r"))   #取出文件里面的值，并且把值转换成列表或者字典
print(type(l))
l=json.loads(l)
print(type(l))
print(l)







