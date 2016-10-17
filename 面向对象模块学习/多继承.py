class c0:
    def f2(self):
        print("c0")

class c1(c0):
    def f3(self):
       print("c1")

class c2:
    def f2(self):
        print("c2")
class c3(c1,c2):
    def f3(self):
        pass


obj=c3()

obj.f2()