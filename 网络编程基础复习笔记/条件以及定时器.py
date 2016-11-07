import threading
from threading import Timer


def tiaojian():
    r=input(">>>").strip()
    if r.isdigit():
        print(r)
        return int(r)
    else:
        return False






def run(i,c):
    print(i)
    c.acquire()
    c.wait_for(tiaojian)
    print(i+100)
    c.release()




c=threading.Condition()
for i in range(10):
    t=threading.Thread(target=run,args=(i,c,))
    t.start()








# #定时器
# def  test():
#     print("hi")
#
#
#
# t=Timer(1,test)
# t.start()

