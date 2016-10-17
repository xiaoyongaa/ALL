'''
正则分组
去已经到的数据中再提取数据
'''
import re
# msg="has dasjdjkasdkalsdaksd"
# res=re.match("(?P<na>^h\w+)",msg)
# print(res.group())
# print(res.groups())
# print(res.groupdict())
msg="hello alex bad alex lge 121321"
r=re.split("a(le)x",msg)
print(r)