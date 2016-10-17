'''
def  kancai(name,age,sex):
    p="{name},{age},{sex},上山去砍柴".format(name=name,age=age,sex=sex)
    print(p)
def  kaiche(name,age,sex):
    p="{name},{age},{sex},开车去东北".format(name=name,age=age,sex=sex)
    print(p)
def  dabaojian(name,age,sex):
    p="{name},{age},{sex},最爱大保健".format(name=name,age=age,sex=sex)
    print(p)

kancai(1,2,3)
kaiche(1,2,3)
dabaojian(1,2,3)
'''
class f:
    def __init__(self,n,a,s):
        self.n=n
        self.a=a
        self.s=s
    def  kancai(self):
        name=str(self.n)
        age=str(self.a)
        sex=str(self.s)
        p="{name},{age},{sex},上山去砍柴".format(name=name,age=age,sex=sex)
        print(p)
    def  kaiche(self):
        name=str(self.n)
        age=str(self.a)
        sex=str(self.s)
        p="{name},{age},{sex},开车去东北".format(name=name,age=age,sex=sex)
        print(p)
    def  dabaojian(self):
        name=str(self.n)
        age=str(self.a)
        sex=str(self.s)
        p="{name},{age},{sex},最爱大保健".format(name=name,age=age,sex=sex)
        print(p)
obj1=f(12,2,3)
obj1.kancai()


obj2=f(3213123,2,3)
obj2.kancai()