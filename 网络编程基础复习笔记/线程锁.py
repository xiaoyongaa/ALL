import threading
import time
NUM=10
#lock=threading.Lock()
lock=threading.RLock()  #多层锁
def func(lock):
    global NUM
    lock.acquire() #上锁
    NUM=NUM-1
    #lock.acquire() #上锁
    time.sleep(2)
    #lock.release() #开锁
    print(NUM)
    lock.release() #开锁



for i in range(10):
    t=threading.Thread(target=func,args=(lock,))
    t.start()