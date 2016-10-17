import os
import json
import datetime
import logging
import sys
d2=os.getcwd()
d2=d2.replace("bin","")
d2=d2.replace("\\","/")
sys.path.append(d2)
d2=d2+"db/admin/"
##################
d3=os.getcwd()
d3=d3.replace("bin","")
d3=d3.replace("\\","/")
sys.path.append(d3)
d3=d3+"db/user/"
time=datetime.date.today()
time=str(time)
time=time.replace("-","_")

user_stat={"kahao":"","user":"","pass":"","edu":"","benyueedu":"","createdata":"","status":"","saving":""}


def main():
    falg=True
    msg=["1.取款","2.存款","3.转账","4.还款"]
    while falg:
        for i in msg:
            print(i)
        chosse=input("请输入你要选择操作的编号：")
        chosse=chosse.strip()
        if chosse=="1":
            print("你选择了取款")
            qukuan()
        elif chosse=="2":
            print("你选择了存款")
            chunkuan()
        elif chosse=="3":
            print("你选择了转账")
            zhuanzhang()
        elif chosse=="4":
            print("你选择了还款")
            huankuan()
        elif chosse=="q":
            break
        else:
            print("你选择的操作编号不正确，请重新输入")

#取款模块
def qukuan():
    falg=True
    kahao=user_stat.get("kahao")
    saving=user_stat.get("saving")
    user=user_stat.get("user")
    edu=user_stat.get("edu")
    saving=int(saving)
    edu=int(edu)
    while falg:
        choose=input("请选择取款金额:")
        choose=choose.strip()
        if choose=="q":
                exit("你选择了退出")
        elif choose=="b":
            flag=False
            break
        if choose.isdigit():
            print("你输入的金额格式正确")
            choose=int(choose)
            if choose<=saving:
                print("你的储存卡的余额足够，可以提现,提现成功!!!!")
                saving=saving-choose
                #更新用户数据操作
                os.chdir(d3)
                os.chdir(kahao)
                basic_infor=json.load(open("basic_infor","r"))
                basic_infor["saving"]=saving
                json.dump(basic_infor,open("basic_infor","w"))
                #更新用户数据操作结束
                message="卡号{kahao}，用户{user},取款{choose}成功！！！".format(kahao=kahao,user=user,choose=choose)
                log_suer("普通用户取款成功",kahao,message)
                user_stat["saving"]=saving
                #####写入账单
                zhangdan_user("提现记录",kahao,message)
                break
            elif choose>saving:
                print("你的储存卡的余额不够，需要从信用卡提现")
                kamax=edu*0.7   #信用卡最多提现的钱
                tixian=choose-saving   #减去储存卡里面的余额，从信用卡上提现的钱
                if tixian<=kamax:
                    print("可以提现,提现成功!!!!")
                    #更新用户数据操作
                    os.chdir(d3)
                    os.chdir(kahao)
                    basic_infor=json.load(open("basic_infor","r"))
                    basic_infor["saving"]="0"
                    edu=edu-tixian-tixian*0.05
                    #basic_infor["edu"]=edu
                    basic_infor["benyueedu"]=edu
                    json.dump(basic_infor,open("basic_infor","w"))
                    #更新用户数据操作结束
                    message="卡号{kahao}，用户{user},取款{choose}成功！！！".format(kahao=kahao,user=user,choose=choose)
                    log_suer("普通用户取款成功",kahao,message)
                    user_stat["saving"]="0"
                    user_stat["benyueedu"]=edu
                    #####写入账单
                    zhangdan_user("提现记录",kahao,message)
                    break
                elif tixian>kamax:
                    print("不可以提现，你要提现的金额超出范围")
                    message="不可以提现，你要提现的金额超出范围"
                    log_suer("不可以提现，你要提现的金额超出范围",kahao,message)
        else:
            print("你输入的金额格式错误，请重新输入")
            message="你输入的金额格式错误，请重新输入"
            log_suer("你输入的金额格式错误，请重新输入",kahao,message)
#取款模块

#存款模块
def chunkuan():
    falg=True
    kahao=user_stat.get("kahao")
    saving=user_stat.get("saving")
    user=user_stat.get("user")
    while falg:
        chosse=input("请选择要存款的金额: ")
        chosse=chosse.strip()
        if chosse=="q":
            exit("你选择了退出")
        elif chosse=="b":
            falg=False
            break
        if chosse.isdigit():
            print("你输入的金额正确")
            chosse=int(chosse)
            saving=int(saving)
            saving=chosse+saving
            ##更新用户信息
            os.chdir(d3)
            os.chdir(kahao)
            basic_infor=json.load(open("basic_infor","r"))
            basic_infor["saving"]=saving
            json.dump(basic_infor,open("basic_infor","w"))
            ##更新用户信息完毕
            message="卡号{kahao}用户{user}存款{chosse}".format(kahao=kahao,user=user,chosse=chosse)
            log_suer("用户存款成功！！！",kahao,message)
            user_stat["saving"]=saving
            #####写入账单
            zhangdan_user("存款记录",kahao,message)
            break
        else:
            print("你输入的金额不正确")
            message="你输入的金额不正确"
            log_suer("你输入的金额不正确!!!",kahao,message)
#存款模块

#转账模块
def zhuanzhang():
    flag=True
    kahao=user_stat.get("kahao")
    saving=user_stat.get("saving")
    user=user_stat.get("user")
    while flag:
        choose_user=input("请选择转账用户卡号：")
        if choose_user=="q":
            exit("你选择了退出")
        elif choose_user=="b":
            flag=False
            break
        choose_cash=input("请选择转账金额: ")
        choose_user=choose_user.strip()
        choose_cash=choose_cash.strip()
        os.chdir(d3)
        if os.path.exists(choose_user):
            print("你要转账的用户卡号在系统中，可以转账")
            if choose_cash.isdigit():
                print("你输入的金额格式正确")
                choose_cash=int(choose_cash)
                saving=int(saving)
                #判断是否有钱转账
                if saving>=choose_cash:
                    print("你账户里面有足够的钱可以转账")
                    ##自己的账户先扣钱
                    os.chdir(kahao)
                    basic_infor=json.load(open("basic_infor","r"))
                    saving=saving-choose_cash
                    basic_infor["saving"]=saving
                    json.dump(basic_infor,open("basic_infor","w"))
                    user_stat["saving"]=saving
                    ##扣钱完毕
                    ##转给要转账的用户
                    os.chdir("G:/python代码/ATM/db/user")
                    os.chdir(choose_user)
                    basic_infor=json.load(open("basic_infor","r"))
                    old=basic_infor.get("saving")
                    old=int(old)   #原来账户里面的余额
                    new=old+choose_cash
                    basic_infor["saving"]=new
                    json.dump(basic_infor,open("basic_infor","w"))
                    print("转账成功！！！！！！！！！！！！")
                    #转账完毕
                    message="卡号{kahao}用户{user}转入给{choose_user}转账金额{choose_cash}元".format(kahao=kahao,user=user,choose_user=choose_user,choose_cash=choose_cash)
                    log_suer("用户转账成功！！！",kahao,message)
                    #####写入账单
                    zhangdan_user("转账记录",kahao,message)
                    break
                else:
                    print("你的账户余额不足，不能转账,重新输入金额")
                    message="你的账户余额不足，不能转账"
                    log_suer("账户余额不足",kahao,message)
            else:
                print("你输入的金额格式不正确,请重新输入")
                message="你输入的金额格式不正确,请重新输入"
                log_suer("输入的金额格式不正确",kahao,message)
        else:
            print("你要转账的用户卡号不在系统中，请重新输入")
            message="你要转账的用户卡号不在系统中，请重新输入"
            log_suer("转账的用户卡号不在系统中",kahao,message)
#转账模块

#还款模块
def huankuan():
    flag=True
    kahao=user_stat.get("kahao")
    edu=user_stat.get("edu")   #规定的额度
    benyueedu=user_stat.get("benyueedu")  #本月额度
    saving=user_stat.get("saving")  #储存卡的余额
    edu=int(edu)
    benyueedu=int(benyueedu)
    saving=int(saving)
    while flag:
        if edu>benyueedu:
            print("你需要还款")
            cash=input("请输入你要还款的金额:")
            cash=cash.strip()
            if cash=="q":
                exit("你选择了退出")
            elif cash=="b":
                flag=False
                break
            if cash.isdigit():
                print("你输入的金额合法")
                cash=int(cash)
                if cash<=saving:
                    print("你的余额足够，开始还款")
                    os.chdir(d3)
                    os.chdir(kahao)
                    basic_infor=json.load(open("basic_infor","r"))
                    saving=saving-cash
                    benyueedu=benyueedu+cash
                    benyueedu=int(benyueedu)
                    if edu==benyueedu:
                        basic_infor["saving"]=saving
                        basic_infor["benyueedu"]=benyueedu
                        ######更新
                        json.dump(basic_infor,open("basic_infor","w"))
                        user_stat["saving"]=saving
                        user_stat["benyueedu"]=benyueedu
                        ######更新完毕
                        print("你已经全部还完额度")
                        message="你已经全部还完额度"
                        log_suer("你已经全部还完额度",kahao,message)
                        #####写入账单
                        zhangdan_user("还款记录",kahao,message)
                    elif edu>benyueedu:
                        basic_infor["saving"]=saving
                        basic_infor["benyueedu"]=benyueedu
                        ######更新
                        json.dump(basic_infor,open("basic_infor","w"))
                        user_stat["saving"]=saving
                        user_stat["benyueedu"]=benyueedu
                        message="你已经还款，但是还没还清"
                        log_suer("你已经还款，但是还没还清",kahao,message)
                        ######更新完毕
                        #####写入账单
                        zhangdan_user("还款记录",kahao,message)
                    elif edu<benyueedu:
                        print("你所还的钱超出了你的欠款，请重新输入")
                        message="你所还的钱超出了你的欠款，请重新输入"
                        log_suer("你所还的钱超出了你的欠款，请重新输入",kahao,message)
                        break
                else:
                    print("你的余额不足，无法还款")
                    message="你的余额不足，无法还款"
                    log_suer("你的余额不足，无法还款",kahao,message)
            else:
                print("你输入的金额不合法，请重新输入")
                message="你输入的金额不合法，请重新输入"
                log_suer("你输入的金额不合法，请重新输入",kahao,message)
        elif edu==benyueedu:
            print("你不需要还款")
            message="你不需要还款"
            log_suer("你不需要还款",kahao,message)
            break
#还款模块

#登录模块
def longin():
    falg=True
    while falg:
        os.chdir(d3)
        user=input("请输入卡号: ")
        pas=input("请输入密码: ")
        user=user.strip()
        pas=pas.strip()
        if os.path.exists(user):
            print("你输入的用户存在")
            os.chdir(user)
            basic_infor=json.load(open("basic_infor","r"))
            kahao=basic_infor.get("kahao")
            pas2=basic_infor.get("pass")
            status=basic_infor.get("status")
            edu=basic_infor.get("edu")
            benyueedu=basic_infor.get("benyueedu")
            user=basic_infor.get("user")
            createdata=basic_infor.get("createdata")
            saving=basic_infor.get("saving")
            if pas==pas2 and status==0:
                print("账户密码正确，成功登陆")
                user_stat["kahao"]=kahao
                user_stat["user"]=user
                user_stat["pass"]=pas2
                user_stat["edu"]=edu
                user_stat["benyueedu"]=benyueedu
                user_stat["createdata"]=createdata
                user_stat["status"]=status
                user_stat["saving"]=saving
                message="卡号{kahao}，用户{user}".format(kahao=kahao,user=user)
                os.chdir(d2)
                log("普通用户登录成功","record/",message)
                ###############
                log_suer("普通用户登录成功",kahao,message)
                return True
            else:
                print("账户密码不正确，登陆失败")
                os.chdir(d2)
                message="账户密码不正确，登陆失败"
                log("账户密码不正确，登陆失败","record/",message)
        else:
            print("你输入的用户不存在")
            os.chdir(d2)
            message="你输入的用户不存在"
            log("你输入的用户不存在","record/",message)
#登录模块

#日志模块
def log_suer(name,kahao,message):
    #create logger
    logger=logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    #文件输出Handler
    os.chdir(d3)
    os.chdir(kahao)
    os.chdir("record")
    fh=logging.FileHandler(time+".log")
    fh.setLevel(logging.DEBUG)
    #指定日志格式
    formatter=logging.Formatter("%(asctime)s-%(name)s-%(levelname)s-%(message)s")
    #Formatter注册给Handler
    fh.setFormatter(formatter)
    #Handler注册给logeer
    logger.addHandler(fh)
    ######################
    logger.info(message)

def log(name,path,message):
    #create logger
    logger=logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    #文件输出Handler
    os.chdir(path)
    fh=logging.FileHandler(time+".log")
    fh.setLevel(logging.DEBUG)
    #指定日志格式
    formatter=logging.Formatter("%(asctime)s-%(name)s-%(levelname)s-%(message)s")
    #Formatter注册给Handler
    fh.setFormatter(formatter)
    #Handler注册给logeer
    logger.addHandler(fh)
    ######################
    logger.info(message)

def zhangdan_user(name,kahao,message):
    #create logger
    logger=logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    #文件输出Handler
    os.chdir(d3)
    os.chdir(kahao)
    os.chdir("record")
    fh=logging.FileHandler(time+".record")
    fh.setLevel(logging.DEBUG)
    #指定日志格式
    formatter=logging.Formatter("%(asctime)s-%(name)s-%(levelname)s-%(message)s")
    #Formatter注册给Handler
    fh.setFormatter(formatter)
    #Handler注册给logeer
    logger.addHandler(fh)
    ######################
    logger.info(message)

def run():
    r=longin()
    if r==True:
        main()