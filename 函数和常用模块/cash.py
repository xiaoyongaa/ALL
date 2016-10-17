import datetime
import time
#time=datetime.date.today()
#time=str(time)
#print(time)
'''
time=time.localtime() #获取国际时间的信息
print(time.tm_mday)
huanqian_date=time.tm_mday
huanqian_date=int(huanqian_date)
print(huanqian_date)
'''
'''
##############################
time=time.localtime() #获取本地时间的信息
print(time,type(time))
#huanqian_date=time.tm_mday
#huanqian_date=int(huanqian_date)
#每月15号还钱
'''
'''
li={1:1,2:2,3:""}
print(li)

t={4:"ewqewqe"}
li.update(t)
print(li)
'''
def u():
    print("wq")
if __name__ == '__main__':
    u()
