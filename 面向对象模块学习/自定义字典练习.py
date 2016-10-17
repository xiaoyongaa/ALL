class mydict(dict):
    def __init__(self):
        self.li=[]
        super(mydict,self).__init__()
    def __setitem__(self, key, value):
        self.li.append(key)
        super(mydict,self).__setitem__(key,value)
    def __str__(self):
        temo_list=[]
        for key in self.li:
            value=self.get(key)
            msg="{key}:{value}".format(key=key,value=value)
            temo_list.append(msg)
        r_str="{"+",".join(temo_list)+"}"
        return r_str



obj=mydict()
obj["k1"]=123
obj["k2"]=3213
print(obj)