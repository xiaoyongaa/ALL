class f:
    def __getitem__(self, item):
        if type(item)==str:
            print(type(item))
        elif type(item)==slice:
            print(item.start)
            print(item.stop)
            print(item.step)

    def __setitem__(self, key, value):
        if type(key)==str:
            print(type(key))
        elif type(key)==slice:
            print("ok")
            print(type(value))

    def __delitem__(self, key):
        print("del")

obj=f()

#obj[1:2:1111]   #取值
#print(r)

#obj["1"]=212    #加中括号会自动执行xxxxxxtitem
obj[1:2]=[1,2,3]

#el obj["ewqeq"]