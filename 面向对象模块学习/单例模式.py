class f:
    stat=None
    def __init__(self,name):
        self.name=name

    @classmethod
    def get_inst(cls):
        if cls.stat==None:
            obj=cls("xiaoyong")
            cls.stat=obj
            return obj
        else:
            return cls.stat

obj1=f.get_inst()
print(obj1)
obj2=f.get_inst()
print(obj2)