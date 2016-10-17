import threading
import time
def f1(i):
    time.sleep(1)
    print(i)


for j in range(10):
    t1=threading.Thread(target=f1,args=(j,))
    t1.start()

#多线程add
#master
