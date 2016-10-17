import datetime
import time
import os
import json
import sys
t=datetime.date.today()
t=str(t)
##############################
#每月15号还钱
time=time.localtime() #获取本地时间的信息
huanqian_date=time.tm_mday
huanqian_date=int(huanqian_date)  #把现在时间的天数取出
#每月22号出账单
d3=os.getcwd()
d3=d3.replace("bin","")
d3=d3.replace("\\","/")
sys.path.append(d3)
d3=d3+"db/user/"


#还款主逻辑
def huankuan(path):
    os.chdir(d3)
    #取值
    os.chdir(path)
    basic_infor=json.load(open("basic_infor","r"))
    kahao=basic_infor.get("kahao")
    user=basic_infor.get("user")
    saving=basic_infor.get("saving")
    benyueedu=basic_infor.get("benyueedu")
    edu=basic_infor.get("edu")
    edu=int(edu)
    benyueedu=int(benyueedu)
    saving=int(saving)
    #取值完毕
    huan_qian=edu-benyueedu   #该还的钱
    if edu==benyueedu:
        print("你没有欠费，不需要还款")
    else:
        if saving>=huan_qian:
            print("你有余额还钱,现在开始扣款")
            saving=saving-huan_qian
            benyueedu=benyueedu+huan_qian
            basic_infor["saving"]=saving
            basic_infor["benyueedu"]=benyueedu
            json.dump(basic_infor,open("basic_infor","w"))
        else:
            print("你的余额不足，无法还钱")
            message=["you are {time} yuqi".format(time=t)]
            basic_infor["yuqirecored"]=message
            json.dump(basic_infor,open("basic_infor","w"))
#还款主逻辑

#还款定时
def crontab_huankuan():
    if huanqian_date=="15":
        user_list=os.listdir(d3)
        os.chdir(d3)
        for path in user_list:
            huankuan(path)
    else:
        print("没到还款日期，不能自动检测扣款!!!")
#还款定时

#账单
def zhangdan(path):
    os.chdir(d3)
    #取值
    os.chdir(path)
    basic_infor=json.load(open("basic_infor","r"))
    kahao=basic_infor.get("kahao")
    user=basic_infor.get("user")
    saving=basic_infor.get("saving")
    benyueedu=basic_infor.get("benyueedu")
    yuqirecored=basic_infor.get("yuqirecored")
    status=basic_infor.get("status")
    edu=basic_infor.get("edu")
    edu=int(edu)
    benyueedu=int(benyueedu)
    saving=int(saving)
    #取值完毕
    if status==0:
        status="正常"
    else:
        status="冻结"
    msg = '''
    ++++++++++++++++++++++
    卡号:%s
    用户名:%s
    规定额度:%d
    当月额度:%d
    状态:%s
    储存卡余额:%d
    不良记录:%s
    ++++++++++++++
    '''%(kahao,user,edu,benyueedu,status,saving,yuqirecored)
    print(msg)
    os.chdir("record")
    with open("zhangdan.log","w") as zhang:
         zhang.write(msg)

#账单定时
def crontab_zhangdan():
    if huanqian_date=="22":
        user_list=os.listdir(d3)
        os.chdir(d3)
        for path in user_list:
            zhangdan(path)
    else:
        print("没到出账单日期，不能出账单!!!")
#账单定时




def run():
    crontab_huankuan()
    crontab_zhangdan()