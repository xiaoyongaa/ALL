#默认选择是0.家电类下面的所有商品
#选择你要购买的物品,要结算请在物品编号最后加j，例如（1,2,3，j） 不结算的就不加j
#购买多件商品按，（逗号）隔开，例如1,2,3,j(结算)，不结算（1,2,3）
import os
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
def f():
    #重复代码
    flag=True
    long=len(jiadianshoop)
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
                        choose2=input("请选择你要购买的物品,要结算请在物品编号最后加j，例如1,2,3，j 不结算的就不加j：")
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
                        l=list(choose2)
                        end=choose2[-1]
                        if end=="j":
                            print("你选择了结算，马上结算")
                            for i in choose2.split(","):
                                if i!="j":
                                    i=int(i)
                                    if i<long:
                                        #print("你输入的商品号合法")
                                        jiage=jiadianshoop[i][1]
                                        if jiage<=cash:
                                            print("你的余额足够")
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
while True:
    user=input("请输入用户名：")
    passwd=input("请输入密码：")
    user=user.strip()
    passwd=passwd.strip()
    #判断用户名是否注册过
    if os.path.exists(user+".txt"):
        #print("你是我们网站的会员")
        now_user=open(user+".txt").read()
        now_passwd=open(user+".pass.txt").read()
        if user==now_user and passwd == now_passwd:
            print("你输入的账户密码正确，成功登陆")
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
                                            choose2=input("请选择你要购买的物品,要结算请在物品编号最后加j，例如1,2,3，j 不结算的就不加j：")
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
                                            l=list(choose2)
                                            end=choose2[-1]
                                            if end=="j":
                                                print("你选择了结算，马上结算")
                                                for i in choose2.split(","):
                                                    if i!="j":
                                                        i=int(i)
                                                        if i<long:
                                                            #print("你输入的商品号合法")
                                                            jiage=jiadianshoop[i][1]
                                                            if jiage<=cash:
                                                                print("你的余额足够")
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
                    f()
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
                                    choose2=input("请选择你要购买的物品,要结算请在物品编号最后加j，例如1,2,3，j 不结算的就不加j:")
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
                                    l=list(choose2)
                                    end=choose2[-1]
                                    if end=="j":
                                        print("你选择了结算，马上结算")
                                        for i in choose2.split(","):
                                            if i!="j":
                                                i=int(i)
                                                if i<long:
                                                    #print("你输入的商品号合法")
                                                    jiage=jiadianshoop[i][1]
                                                    if jiage<=cash:
                                                        print("你的余额足够")
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
        else:
            print("你输入的密码不正确，请重新输入")
    else:
        #写进用户名
        n=open(user+".txt","w")
        n.write(user)
        n.close()
        now_user=open(user+".txt").read()
        #写进用户名结束
        #写进密码
        n=open(user+".pass.txt","w")
        n.write(passwd)
        n.close()
        now_passwd=open(user+".pass.txt").read()
        #写进密码结束
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
                                        choose2=input("请选择你要购买的物品,要结算请在物品编号最后加j，例如1,2,3，j 不结算的就不加j:")
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
                                        l=list(choose2)
                                        end=choose2[-1]
                                        if end=="j":
                                            print("你选择了结算，马上结算")
                                            for i in choose2.split(","):
                                                if i!="j":
                                                    i=int(i)
                                                    if i<long:
                                                        #print("你输入的商品号合法")
                                                        jiage=jiadianshoop[i][1]
                                                        if jiage<=cash:
                                                            print("你的余额足够")
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
                                choose2=input("请选择你要购买的物品,要结算请在物品编号最后加j，例如1,2,3，j 不结算的就不加j:")
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
                                l=list(choose2)
                                end=choose2[-1]
                                if end=="j":
                                    print("你选择了结算，马上结算")
                                    for i in choose2.split(","):
                                        if i!="j":
                                            i=int(i)
                                            if i<long:
                                                #print("你输入的商品号合法")
                                                jiage=jiadianshoop[i][1]
                                                if jiage<=cash:
                                                    print("你的余额足够")
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


































