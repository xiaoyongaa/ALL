#n=[1]
#print(len(n))   #查看任何东西的长度
#元组，不可变的列表
#u=(1,2,3,4,5)   #只读列表
########################
#字符串的常用功能
#移除空白
#分割
#索引
#切片
'''
name="Alex li"
username=input("请输入你的名字：")
if name==username.strip():
    print("ok")
#移除空白功能
'''
name="alex,jack,rain"
n=name.split(",")    #字符串的拆分
print("|".join(n))    #字符串的合并

if " " in name:    #判断有没有空格
    print("ok")
###############################
#format方法的字符串格式化
msg="hello,{q},{w},jdask{e}"
msg2=msg.format(q="kk",w="qq",e="ee")
print(msg2)
#########################################
#字符串切片
print(msg2[9:11])
############################
l=msg.center(40,"-")
print(l)
###################################
print(msg.find("h"))
#find方法，如果找到该元素返回改元素的下标，如果没找到返回-1
'''
age=input("你的名字：")  #判断是否为数字 isalnum
if age.isdigit():
    print("ok")
    if age.startswith("7"):
        print("ok %s"%age)
################################
#age.endswith
#age.startswith
'''
age=input("你的名字：")
age=age.strip()
if age.isdigit():
    print("ok")








































