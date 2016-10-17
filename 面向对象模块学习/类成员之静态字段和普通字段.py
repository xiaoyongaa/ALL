class p:
    c="中国"
    #静态字段
    def __init__(self,name):
        self.name=name
        #普通字段

#一把情况下，自己访问自己的字段。
hn=p("湖南")
#规则，普通字段只能用对象访问
#静态字段用类访问(万不得已可以用对象访问)
#静态字段在代码加载时候已经创建
print(hn.c)
print(p.c)
