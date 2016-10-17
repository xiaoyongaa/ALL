class f:
    def __getitem__(self, item):
        return 123
    def __setitem__(self, key, value):
        print("set")
    def __delitem__(self, key):
        print("del")

obj=f()

#r=obj["1"]
#print(r)

obj["1"]=212    #加中括号会自动执行xxxxxxtitem

del obj["ewqeq"]