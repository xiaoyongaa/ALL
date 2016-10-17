'''
笔记
for i in range(10):

#3次机会问一次

'''
age=22
c=0
while True:
    if c<3:
        cai=input("请输入要猜的年龄：")
        if cai.isdigit():   #判断是否为整数
            print("格式正确")
            cai1=int(cai)     #判断为整数把输入的变量变成int型
            if cai1==age and c<3:
                print("猜对了")
                break
            elif cai1>age and c<3:
                print("猜大了")
                c+=1
            elif cai1<age and c<3:
                print("猜小了")
                c+=1
        else:                 #判断是否为整数
            print("输入格式不正确")
    else:
        p=input("次数用完，是否要继续，继续请按：yes，不想继续请按no:")
        if p=="yes":
            c=0
            cai=input("请输入要猜的年龄：")
            if cai.isdigit():   #判断是否为整数
                print("格式正确2")
                cai1=int(cai)     #判断为整数把输入的变量变成int型
                if cai1==age and c<3:
                    print("猜对了")
                    break
                elif cai1>age and c<3:
                    print("猜大了")
                    c+=1
                elif cai1<age and c<3:
                    print("猜小了")
                    c+=1
            else:                 #判断是否为整数
                print("输入格式不正确")
        elif p=="no":
            print("你选择了退出 bye bye")
            break

