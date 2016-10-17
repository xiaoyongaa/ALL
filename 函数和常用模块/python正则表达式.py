import re  #导入正则表达式的模块 #0-多次 *  + 1到多次 ？0-1次
'''
r=re.findall("a[\d]b","a1b")
print(r)
#[]#中括号一个范围 中括号里面的^是非的意思 \d是匹配任意数字 \反斜杠

r=re.search("b","abbbb") #不怎么好用,只能取出第一个结果
print(r)

l=re.sub("g.t","1111","i get a,i get b,i get c",2)  #替换功能
print(l)
l=re.subn("g.t","1111","i get a,i get b,i get c",2)  #替换功能,展现替换次数
print(l)

r=re.split("\|","2|12|12|1")  #按正则指定的分割字符串
print(r)
#把规则封装成一个对象，方便以后调用
text="dksakjd,akjsdkjaksjd.,dkjaskjdkjasd"
regex=re.compile(r"dk*")
print(type(regex))
print(regex.findall(text))
'''
a=re.findall(r"am","Iww am w.run\comoob") #里面的r是原生字符
print(a)