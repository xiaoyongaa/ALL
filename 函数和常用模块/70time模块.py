import time
import datetime
#print(time.time())  #时间戳1970年开始到现在的时间戳
#print(time.ctime())
#print(time.ctime(time.time()-86400))
#time=time.gmtime() #获取国际时间的信息
#print(time)
#print(time.tm_year)
#print(time.tm_wday)
#print(time.tm_min)
#######
#t=time.localtime()  #本地时间对象
#print(time.localtime())  #获取本地服务器时间
#print(time.mktime(t))  #查看对象时间的时间戳
#time.sleep(4)  #暂停4秒
#t1=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()) #把时间换成字符串形式
#print(t1)
#t2=time.strptime("2016-05-6 15:06:21","%Y-%m-%d %H:%M:%S") #struct_time对象
#print(t2)
#print(time.mktime(t2))  #把struct_time对象转换成时间戳

##########################################
#print(datetime.date.today())  #输出当前日期
#now_time=datetime.datetime.now()  #查看当前时间，用字符串形式表示
#print(now_time)
#print(datetime.datetime.now()+datetime.timedelta(days=-10))   #现在的时间增加10天
#print(datetime.datetime.now()+datetime.timedelta(hours=+3))    #现在的时间增加3小时
'''
now_time=datetime.datetime.now()
print(now_time)
print(type(now_time))
time=now_time.replace(2014,9,12)
print(type(time))
if now_time>time:
    print("ok")
    '''
##############################
time=time.localtime() #获取本地时间的信息
huanqian_date=time.tm_mday
huanqian_date=int(huanqian_date)
#每月15号还钱




time=datetime.date.today()
time=str(time)
time=time.replace("-","_")
print(time,type(time))








