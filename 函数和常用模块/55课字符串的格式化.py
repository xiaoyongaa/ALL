s="-----{name:s}_______{age:d}======{name:s}".format(name="dsda",age=213)
#print(s)
s2="-----{:*^20s}===={:+d}================{:b}".format("xiaoyong",123,15)
#print(s2)
#填充任意字符
s3="number {:b},{:o},{:d},{:x},{:%}".format(15,15,51,55,15,2)
print(s3)

s4="i am{},age{},{}".format("是大事","dsas",11)
print(s4)
s5="i am{},age{}.{}".format(*["是大事","dsas",11])
print(s5)

s6="i am{name},age{age},relay{name}".format(name="axsad",age=1221)
print(s6)

s7="i am{name},age{age},realy{name}".format(**{"name":"dsada","age":18})
print(s7)