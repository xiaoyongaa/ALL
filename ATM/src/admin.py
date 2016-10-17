import os
import json
import logging
import datetime
import subprocess
import sys
time=datetime.date.today()
time=str(time)
time=time.replace("-","_")
time2=datetime.date.today()
time2=str(time2)
current_user={"longing_user":"","stat":""}
d2=os.getcwd()
d2=d2.replace("bin","")
d2=d2.replace("\\","/")
sys.path.append(d2)
d2=d2+"db/admin/"
#print(d2)
d3=os.getcwd()
d3=d3.replace("bin","")
d3=d3.replace("\\","/")
sys.path.append(d3)
d3=d3+"db/user/"
#print(d3)


def log(name,path,message):
    #create logger
    os.chdir(d2)
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

def log_suer(name,kahao,message):
    #create logger
    logger=logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    #文件输出Handler
    os.chdir("G:/python代码/ATM/db/user")
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



def main():
    flag=True
    msg=["1.创建普通用户","2.删除普通用户","3.锁定普通用户","4.搜索普通用户"]
    while flag:
        for i in msg:
            print(i)
        choose=input("请输入你要选择的操作编号：")
        choose=choose.strip()
        if choose=="1":
            print("你选择了创建用户")
            add_user()
        elif choose=="2":
            print("你选择了删除用户")
            delete_user()
        elif choose=="3":
            print("锁定用户")
            lock_user()
        elif choose=="4":
            print("搜索普通用户")
            search_user()
        elif choose=="q":
            #flag=False
            break
        else:
            print("你选择的格式不对，请重新输入")






#增加用户
def add_user():
    falg=True
    while falg:
        kahao=input("请输入卡号：")
        user=input("请输入用户：")
        pas=input("请输入密码: ")
        edu=input("请输入信用卡额度：")
        kahao=kahao.strip()
        user=user.strip()
        pas=pas.strip()
        edu=edu.strip()
        os.chdir(d3) #切换到普通用户目录
        if os.path.exists(kahao):
            print("卡号存在，无需创建")
            os.chdir(d2)
            message="卡号存在，无需创建"
            log("卡号存在，无需创建","record/",message)
            #log("用户添加失败","G:/python代码/ATM/db/admin/record/",message)
            break
        else:
            print("卡号不存在，需要创建,创建成功")
            os.chdir(d3)    #切换到普通用户目录
            os.mkdir(kahao)     #创建卡号目录
            os.chdir(kahao)     #进入卡号目录
            os.mkdir("record")  #创建record目录文件
            basic={"kahao":kahao,"user":user,"pass":pas,"edu":edu,"benyueedu":edu,"saving":0,"status":0,"createdata":time2,"yuqirecored":""}
            json.dump(basic,open("basic_infor","w"))
            os.chdir(d2)
            message="%s账号，%s用户，%s额度的信用卡创建成功!!!"%(kahao,user,edu)
            log("普通用户成功创建","record/",message)
            break
#增加用户


#删除用户
def delete_user():
    falg=True
    while falg:
        choose_user=input("请选择要删除的用户: ")
        choose_user=choose_user.strip()
        os.chdir(d3)
        if os.path.exists(choose_user):
            print("该卡号存在，可以删除")
            os.chdir(d3)
            os.system("rd /s/q "+choose_user)
            print("删除成功")
            os.chdir(d2)
            message="删除普通用户成功"
            log("删除普通用户成功","record/",message)
            break
        else:
            print("该卡号不存在，无法删除")
            os.chdir(d2)
            message="删除普通用户失败"
            log("删除普通用户失败","record/",message)
            break
#删除用户

#锁定用户
def lock_user():
    flag=True
    while flag:
        chosse=input("请选择你要锁定的用户卡号：")
        chosse=chosse.strip()
        os.chdir(d3)
        if os.path.exists(chosse):
            print("存在，可以锁定该账户")
            os.chdir(chosse)
            basic_infor=json.load(open("basic_infor","r"))
            basic_infor["status"]=1
            basic_infor=json.dump(basic_infor,open("basic_infor","w"))   #更新账户状态
            print("锁定用户完毕")
            os.chdir(d2)
            message="锁定用户成功"
            log("锁定用户成功","record/",message)
            break
        else:
            print("不存在，不可以锁定该账户")
            os.chdir(d2)
            message="锁定用户失败"
            log("锁定用户失败","record/",message)
            break
#锁定用户

#搜索用户
def search_user():
    falg=True
    while falg:
        choose=input("请输入你要查找的卡号：")
        choose=choose.strip()
        os.chdir(d3)
        if os.path.exists(choose):
            print("你输入的卡号存在，可以查看")
            os.chdir(choose)
            basic_infor=json.load(open("basic_infor","r"))
            kahao=basic_infor.get("kahao")
            user=basic_infor.get("user")
            pas=basic_infor.get("pass")
            edu=basic_infor.get("edu")
            status=basic_infor.get("status")
            createdata=basic_infor.get("createdata")
            saving=basic_infor.get("saving")
            msg="卡号:{kahao}\n用户名:{user}\n密码:{pas}\n额度:{edu}\n状态:{status}\n创建日期:{createdata}\n储存卡余额:{saving}".format(kahao=kahao,user=user,pas=pas,edu=edu,status=status,createdata=createdata,saving=saving)
            print(msg)
            os.chdir(d2)
            message="查看{kahao}用户成功".format(kahao=kahao)
            log("查看用户成功","record/",message)
            break
        else:
            print("你输入你卡号不存在，不可以被查看")
            os.chdir(d2)
            message="卡号不存在，查看用户失败"
            log("查看用户失败","record/",message)
            break
#搜索用户






#登录入口
def longin():
    flag=True
    os.chdir(d2)
    while flag:
        if os.path.exists("admin_info"):   #用户第一次登录，判断是否有管理员密码文件
            user=input("这里是管理员登录通道，请输入管理员用户名: ")
            pas=input("请输入密码： ")
            user=user.strip()
            pas=pas.strip()
            os.chdir(d2)
            user_infor=json.load(open("admin_info","r"))
            old_user=user_infor.get("user")
            old_pas=user_infor.get("pass")
            if  old_user==user and old_pas==pas:
                print("成功登录")
                os.chdir(d2)
                message="admin用户成功登陆系统"
                log("管理员登陆","record/",message)
                current_user["longing_user"]="admin"
                current_user["stat"]=True
                return True
            else:
                os.chdir(d2)
                print("登录失败,重新登录")
                message="admin用户登陆不成功"
                log("管理员登陆","record/",message)
        else:   #用户第一次登录，判断是否有管理员密码文件，假设没有，就创建一个密码文件
            admininfor={"user":"admin","pass":"admin"}
            os.chdir(d2)
            json.dump(admininfor,open("admin_info","w"))
            if os.path.exists("record"):
                continue
            else:
                os.mkdir("record")
#登录入口












def run():
    r=longin()
    if r==True:
        main()

