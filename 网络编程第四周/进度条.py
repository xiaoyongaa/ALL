import time
import sys






#生成连续的数
def range_chu():
    for i in range(0,101):
        time.sleep(0.1)
        rate=i/100
        mun=int(rate*100)
        mum="\r{n}{m}%".format(n="="*mun,m=mun)
        sys.stdout.write(mum)

range_chu()