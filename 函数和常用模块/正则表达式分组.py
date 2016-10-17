'''
正则分组：
去已经提取到的数据中，再提取数据
'''
import re
o="hasaabc dkjsa  halaabc kdksakjdksakd"
'''
r=re.match("h(?P<name>\w+)",o)
print(r.group())
print(r.groups())   #匹配到已经匹配的
print(r.groupdict())
'''
r=re.findall("h\w+abc",o)
r=re.findall("h(\w+)ab(c)",o)  #去已经提匹配的数据中，再提取数据
print(r)

r=re.split("dk(js)a",o)   #去已经匹配到的数据中，再提取数据
print(r)


