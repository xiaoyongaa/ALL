import threading



class MyThread(threading.Thread):
    def __init__(self,func,args):
        self.func=func
        self.args=args
        super(MyThread,self).__init__()


    def run(self):
        self.func(self.args)

def f2(arg):
    print(arg)


obj=MyThread(f2,123)
obj.start()

