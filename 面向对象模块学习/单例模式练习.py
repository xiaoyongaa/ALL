class f:
    stat=None
    def __init__(self,name):
        self.name=name
    @classmethod
    def add(cls):
        if cls.stat==None:
            obj=cls("zxxx")
            cls.stat=obj
            return obj
        else:
            return cls.stat


obj1=f.add()
obj2=f.add()
print(obj1)
print(obj2)