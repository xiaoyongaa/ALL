#定义全局菜单内容
#默认三级菜单定义北京-昌平-沙河
#所有城市
chengshi=open("chengshi.txt","w")
chengshi.write("1.北京\n")
chengshi.write("2.上海\n")
chengshi.write("3.南京\n")
chengshi.close()
chengshi=open("chengshi.txt").read()
#print(chengshi)
#####################################
#选择北京市下的区域
beijingqu=open("beijingqu.txt","w")
beijingqu.write("1.东城\n")
beijingqu.write("2.朝阳\n")
beijingqu.write("3.昌平\n")
beijingqu.close()
beijingqu=open("beijingqu.txt").read()
#print(beijingqu)
################################
#选择昌平
beijingcangping=open("beijingcangping.txt","w")
beijingcangping.write("1.沙河\n")
beijingcangping.write("2.天通苑\n")
beijingcangping.close()
beijingcangping=open("beijingcangping.txt").read()
#print(beijingcangping)
####################################
#选择沙河
beijingshahe=open("beijingshahe.txt","w")
beijingshahe.write("1.老男孩教育\n")
beijingshahe.write("2.马哥教育\n")
beijingshahe.write("3.微软\n")
beijingshahe.close()
beijingshahe=open("beijingshahe.txt").read()
#print(beijingshahe)
########################################################
##城市选择分支
flag = True
while flag:
    print(chengshi)
    choose=input("请选择你要进入的城市：")
    if choose=="1":
        print("你选择了北京")
        while flag:
            print(beijingqu)
            choose2=input("请输入北京市的区域：")
            if choose2=="1":
                print("东城")
            elif choose2=="2":
                print("朝阳")
            elif choose2=="3":
                print("昌平")
                while flag:
                    print(beijingcangping)
                    choose3=input("请输入昌平以下的区域：")
                    if choose3=="1":
                        print("沙河")
                        while flag:
                            print(beijingshahe)
                            choose4=input("输入沙河下的企业：")
                            if choose4=="1":
                                print("老男孩教育")
                                break
                            elif choose4=="2":
                                print("马哥教育")
                                break
                            elif choose4=="3":
                                print("微软")
                                break
                            elif choose4=="b":
                                break
                            elif choose4=="q":
                                flag=False
                                break
                    elif choose3=="2":
                        print("通天苑")
                    elif choose3=="b":
                        break
                    elif choose3=="q":
                        flag=False
                        break
            elif choose2=="b":
                  break
            elif choose2=="q":
                flag=False
                break
    elif choose=="b" or choose == "q":
        break
    elif choose=="2":
        print("你选择了上海")

    elif choose=="3":
        print("你选择了南京")









































#