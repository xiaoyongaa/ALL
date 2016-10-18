import threading
def f1(a):
    print(a)

# #创建线程方法一
# t=threading.Thread(target=f1,args=(123,))
# t.start()

#创建线程方法二，因为thread创建线程之前会执行run方法
#t.run()
class MyThraed(threading.Thread):
    def __init__(self,fun,args):
        self.fun=fun
        self.args=args
        super(MyThraed,self).__init__()

    def run(self):
        #print("run")
        self.fun(self.args)



obj=MyThraed(f1,123)
obj.start()
