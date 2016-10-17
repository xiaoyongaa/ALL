#默认选择是0.家电类下面的所有商品
#按c查看购物车内容，按q退出程序
#购买多件商品按，（逗号）隔开，例如1,2,3
import os
import time
shoop1=[
    ("家电类"),
    ("衣服类"),
    ("手机类"),
    ("车类"),
]
jiadianshoop=[
    ("电冰箱",20000),
    ("彩电",2000),
    ("洗衣机",400),
    ("脸盆",30),
    ("牙刷",50)
]
flag=True
long=len(jiadianshoop)
user=input("请输入用户名：")
passwd=input("请输入密码：")
if os.path.exists("cash"+user):
    cash=open("cash"+user).read()
    cash=int(cash)
    print("欢迎回来，你是我们网站的会员，你的余额还有%d元，是否要继续充值?,选Y/N"%(cash))
    choose=input("Y/N")
    if choose=="y" or choose=="Y":
        print("你选择了充值")
        jiaqian=input("请输入你要充值的金额;")
        jiaqian=jiaqian.strip()
        if jiaqian.isdigit():
            jiaqian=int(jiaqian)
            print("你输入的金额合法")
            cash=jiaqian+cash
            cash=str(cash)
            n=open("cash"+user,"w")
            n.write(cash)
            n.close()
            cash=int(cash)
            print("充值成功，你现在账户余额为%d"%(cash))
            #重复代码
            while flag:
                for i in enumerate(shoop1):
                    weizhi=i[0]
                    shangping=i[1]
                    print(weizhi,shangping)
                choose=input("请选择你要购买的商品类别")
                choose=choose.strip()
                if choose.isdigit():
                    choose=int(choose)
                    if choose<len(shoop1):
                        print("你选择范围正确")
                        if choose==0:
                            print("你选择了家电类")
                            while flag:
                                for i in enumerate(jiadianshoop):
                                    weizhi=i[0]
                                    wuping=i[1][0]
                                    jiage=i[1][1]
                                    print(weizhi,wuping,jiage)
                                choose2=input("请选择你要购买的物品：")
                                choose2.strip()
                                #choose2=int(choose2)
                                if choose2=="q":
                                    print("谢谢光临，欢迎下次再来")
                                    if os.path.exists("jilu"+user):
                                        x=open("jilu"+user).read()
                                        print(x)
                                    else:
                                        print("你还没购物")
                                    flag=False
                                    break
                                elif choose2=="c":
                                    if os.path.exists("jilu"+user):
                                        x=open("jilu"+user).read()
                                        print(x)
                                    else:
                                        print("你还没购物")
                                    break
                                for i in choose2.split(","):
                                    i=int(i)
                                    if i<long:
                                        print("你输入的商品号合法")
                                        jiage=jiadianshoop[i][1]
                                        if jiage<=cash:
                                            print("你的钱足够，可以购买。如果你想去结算请按j键，不结算继续购物请按b,退出按q，查看已经买过的商品按c")
                                            x=input("请输入你要选择的操作：")
                                            if x=="j":
                                                cash=cash-jiage  #扣钱
                                                wuping=jiadianshoop[i][0]
                                                n=open(user,"a")   #购买的历史物品按用户名历史保存
                                                n.write(wuping+"\n")
                                                n.close()
                                                cash=str(cash)                  #转换成str形势保存
                                                q=open("cash"+user,"w")        #账户的余额历史保存
                                                q.write(cash)
                                                q.close()
                                                cash=int(cash)                  #存好了转换会int
                                                print("你已经成功购买，现在账户余额还剩%d元"%(cash))
                                                 #生成之前购买记录
                                                wupingdeqjiege=jiadianshoop[i][1]
                                                wupingdeqjiege=str(wupingdeqjiege)
                                                wuping=str(wuping)
                                                jilu=open("jilu"+user,"a")
                                                #time=time.strftime('%Y-%m-%d %H:%M:%S')
                                                #print(time)
                                                #time=str(time)
                                                jilu.write(wuping+"     "+wupingdeqjiege+"\n")
                                                jilu.close()
                                            elif x=="b":
                                                break
                                            elif x=="q":
                                                if os.path.exists("jilu"+user):
                                                    x=open("jilu"+user).read()
                                                    print(x)
                                                else:
                                                    print("你还没购物")
                                                flag=False
                                                break
                                            elif x=="c":
                                                if os.path.exists("jilu"+user):
                                                    x=open("jilu"+user).read()
                                                    print(x)
                                                else:
                                                    print("你还没购物")
                                                break
                                        else:
                                            print("你的余额不足，请充值")
                                    else:
                                        print("你输入的商品号不合法，重新输入")
                        elif choose==1:
                            print("你选择了衣服类")
                        elif choose==2:
                            print("你选择了手机类")
                        elif choose==3:
                            print("你选择了车类")
                        elif choose=="q":
                            if os.path.exists("jilu"+user):
                                x=open("jilu"+user).read()
                                print(x)
                            else:
                                print("你还没购物")
                            flag=False
                            break
                        elif choose=="c":
                            if os.path.exists("jilu"+user):
                                x=open("jilu"+user).read()
                                print(x)
                            else:
                                print("你还没购物")
                            break
                    else:
                        print("你选择的商品编号不在范围之内")
                elif choose=="q":
                    print("bye")
                    if os.path.exists("jilu"+user):
                        x=open("jilu"+user).read()
                        print(x)
                    else:
                        print("你还没购物")
                    flag=False
                    break
                elif choose=="c":
                    if os.path.exists("jilu"+user):
                        x=open("jilu"+user).read()
                        print(x)
                    else:
                        print("你还没购物")
                    break
                else:
                    print("你选择的不是菜单")
                #重复代码
        else:
            print("你输入的金额不合法")
    elif choose=="n" or choose=="N":
        print("你选择了不充值")
    else:
        print("你输入的选择不合法")
else:
    cash=input("请输入你要充值的金额：")
    cash=cash.strip()
    if cash.isdigit():
        cash=int(cash)
        print("你输入的金额格式正确")
    else:
        exit("你输入的金额格式不正确")
    while flag:
        for i in enumerate(shoop1):
            weizhi=i[0]
            shangping=i[1]
            print(weizhi,shangping)
        choose=input("请选择你要购买的商品类别")
        choose=choose.strip()
        if choose.isdigit():
            choose=int(choose)
            if choose<len(shoop1):
                print("你选择范围正确")
                if choose==0:
                    print("你选择了家电类")
                    while flag:
                        for i in enumerate(jiadianshoop):
                            weizhi=i[0]
                            wuping=i[1][0]
                            jiage=i[1][1]
                            print(weizhi,wuping,jiage)
                        choose2=input("请选择你要购买的物品：")
                        choose2.strip()
                        #choose2=int(choose2)
                        if choose2=="q":
                            print("谢谢光临，欢迎下次再来")
                            if os.path.exists("jilu"+user):
                                x=open("jilu"+user).read()
                                print(x)
                            else:
                                print("你还没购物")
                            flag=False
                            break
                        elif choose2=="c":
                            if os.path.exists("jilu"+user):
                                x=open("jilu"+user).read()
                                print(x)
                            else:
                                print("你还没购物")
                            break
                        for i in choose2.split(","):
                            i=int(i)
                            if i<long:
                                print("你输入的商品号合法")
                                jiage=jiadianshoop[i][1]
                                if jiage<=cash:
                                    print("你的余额足够，选择的商品还没有结算完成。如果你想去结算请按j键，不结算继续购物请按b,退出按q，查看已经买过的商品按c")
                                    x=input("请输入你要选择的操作：")
                                    if x=="j":
                                        cash=cash-jiage  #扣钱
                                        wuping=jiadianshoop[i][0]
                                        n=open(user,"a")   #购买的历史物品按用户名历史保存
                                        n.write(wuping+"\n")
                                        n.close()
                                        cash=str(cash)                  #转换成str形势保存
                                        q=open("cash"+user,"w")        #账户的余额历史保存
                                        q.write(cash)
                                        q.close()
                                        cash=int(cash)                  #存好了转换会int
                                        print("你已经成功购买，现在账户余额还剩%d元"%(cash))
                                        #生成之前购买记录
                                        wupingdeqjiege=jiadianshoop[i][1]
                                        wupingdeqjiege=str(wupingdeqjiege)
                                        wuping=str(wuping)
                                        jilu=open("jilu"+user,"a")
                                        #time=time.strftime('%Y-%m-%d %H:%M:%S')
                                        #print(time)
                                        #time=str(time)
                                        jilu.write(wuping+"     "+wupingdeqjiege+"\n")
                                        jilu.close()
                                    elif x=="b":
                                        break
                                    elif x=="q":
                                        if os.path.exists("jilu"+user):
                                            x=open("jilu"+user).read()
                                            print(x)
                                        else:
                                            print("你还没购物")
                                        flag=False
                                        break
                                    elif x=="c":
                                        if os.path.exists("jilu"+user):
                                            x=open("jilu"+user).read()
                                            print(x)
                                        else:
                                            print("你还没购物")
                                        break

                                else:
                                    print("你的余额不足，请充值")
                            else:

                              print("你输入的商品号不合法，重新输入")
                elif choose==1:
                    print("你选择了衣服类")
                elif choose==2:
                    print("你选择了手机类")
                elif choose==3:
                    print("你选择了车类")
                elif choose=="q":
                    print("bye")
                    if os.path.exists("jilu"+user):
                        x=open("jilu"+user).read()
                        print(x)
                    else:
                        print("你还没购物")
                    flag=False
                    break
            else:
                print("你选择的商品编号不在范围之内")
        elif choose=="q" :
            print("bye")
            if os.path.exists("jilu"+user):
                x=open("jilu"+user).read()
                print(x)
            else:
                print("你还没购物")
            flag=False
            break
        else:
            print("你选择的不是菜单里面的内容")