#%s %d
'''
s="你说%s，按%d"%("dsadas",1)
print(s)
s="你是%(name)s and %(age)d"%{"name":"alex","age":123}
print(s)
'''
'''
s="asd%(name)-10s%(age)10d"%{"name":"assill","age":123}
print(s)
s1="alex %"
print(s1)
s2="alex %s %%"%{"dasdasd"}
print(s2)
'''
#常用的字符串格式化
tp1="i am %s"%"alex"
print(tp1)
tp1="i am %s age %d"%("alex",18)
print(tp1)
tp1="i am %(name)s age %(age)d"%{"name":"alex","age":18}
print(tp1)
tp1="percent %.2f"%99.127123123
print(tp1)
tp1="i am %(pp).2f"%{"pp":1.321321321}
print(tp1)
tp1="i am %.2f %%"%3.2312312
print(tp1)