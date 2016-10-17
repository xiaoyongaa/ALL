class mydict(dict):
    def __init__(self):
        self.li=[]
        super(mydict,self).__init__()   #执行父类的构造方法
    def __setitem__(self, key, value):
        self.li.append(key)
        super(mydict,self).__setitem__(key,value)
    def __str__(self):
        temp_list=[]
        for key in self.li:
            value=self.get(key)
            msg="'{key}':{value}".format(key=key,value=value)
            temp_list.append(msg)
        temp_str="{"+",".join(temp_list)+"}"
        return temp_str


obj=mydict()
obj["k1"]=123
obj["k2"]=234

print(obj)

'''
l={1:2,2:3}
l=mydict(l)
l[1]="xxxx"
print(l)
'''
