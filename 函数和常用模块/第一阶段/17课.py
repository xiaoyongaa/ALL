#文件操作
#打开文件
#操作文件
#关闭文件
############
#写入文件
#f=open("db.txt","a+")
#b=bytes("理解",encoding="utf-8")
#f.write("b")
#f.close()
#############
#读取
f=open("db.txt","r+")
date=f.read()
print(date)
print(f.tell())  #tell当前指针所在的位置
f.seek(0) #主动的吧指针调到1位置
f.write("a")
f.close()
#l=str(f,encoding="utf-8")
#print(l)
#read（）无参数，读全部，有参数，b按直接，无b按字符
#tell()获取当前指针位置（字节）
#seek(1)指针跳转到指定位置（字节）
#write（）写数据 b字节 无b字符
#fileno文件描述符
#fulsh强制写进硬盘，强刷
#readline 只读取1行
#truncate 截断，指针位置后的清空
# f=open("db.txt","r")
#for line in f:
#with open("xb") as f1,open("x2b") as f2: #打开关闭操作
#line.replace #字符串替换方法
