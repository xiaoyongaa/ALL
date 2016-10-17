#compile() #编译 模式 sing，eval，exec #把字符串编译成python代码
#eval()
#exec() 可以执行python所有功能
'''
s="print(123)"
r=compile(s,"<string>","exec")
#执行python代码
exec(r)
'''
#s="8*8"
#s=eval(s)
#print(s)

#执行python代码，或者字符串
r=exec("1+2+3")
#执行表达式，并获取结果
ret=eval("1+2+3")
print(ret)
