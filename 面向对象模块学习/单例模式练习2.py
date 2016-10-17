class test:
    stat=None
    def __init__(self,name):
        self.name=name
    @classmethod
    def add(cls):
        if cls.stat==None:
            obj=cls("xiaoyong")
            cls.stat=obj
            return cls.stat
        else:
            return cls.stat

u=test.add()
print(u)
y=test.add()
print(y)