import threading

lock=threading.Condition()



def fun(i,lock):
    print(i)
    lock.acquire()   #获得
    lock.wait()
    print(i+100)
    lock.release()




for i in range(10):
    t=threading.Thread(target=fun,args=(i,lock))
    t.start()


while True:
    inp=input(">>>:").strip()
    if len(inp)==0:continue
    lock.acquire()
    lock.notify(int(inp))  #通知
    lock.release()

