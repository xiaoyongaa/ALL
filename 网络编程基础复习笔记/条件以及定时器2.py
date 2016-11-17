import threading


def condition():
    ret=False
    r=input(">>>")
    if r=="ture":
        ret=True
    else:
        ret=False
    return ret



def run(i,c):
    print(i)
    c.acquire()
    c.wait_for(condition)
    print(i+100)
    c.release()





c=threading.Condition()  #条件

for i in range(10):
    t=threading.Thread(target=run,args=(i,c))
    t.start()


