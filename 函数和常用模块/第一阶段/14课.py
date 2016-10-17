#内置函数
#取绝对值的函数
#abs()
#n=abs(-212)
#print(n)
#############
#n=all([1,2,0])  #传入的值有1个是假的就全部为False
#print(n)
###############
#n=any([1,2,3,0])  #传入的有一个是真，就是True
#print(n)
#bin() 十进制转换成二进制
#oct() 十进制转化成八进制
#hex() 十进制转换成十六进制
#n=bool(0)
#print(n)
#utf-8 一个汉字;3字节
#gbk 一个汉字：2字节
#字符串转换字节类型
#bytes（转换的字符串，按照什么编码）
s="你好"
n=bytes(s,encoding="utf-8")
print(n)
#字节转化成字符串
l=str(bytes(s,encoding="utf-8"),encoding="utf-8")
print(l)


