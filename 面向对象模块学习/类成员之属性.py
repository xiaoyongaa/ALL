class f:
    def __init__(self,count):
        self.count=count
    @property   #只想取值
    def all_paper(self):
        a1,a2=divmod(self.count,10)
        if a2==0:
            return a1
        else:
            return a1+1
    @all_paper.setter    #设置
    def all_paper(self,value):
        print(value)
    @all_paper.deleter   #删除
    def all_paper(self):
        print("1")


p=f(101)
#r=p.all_paper  #去掉括号，以访问字段的形式执行方法  执行@property
#print(r)
#p.all_paper=11  #执行设置方法@all_paper.setter

del p.all_paper   #执行@all_paper.deleter   #删除

'''
属性
不伦不类的东西
具有方法的写作模式，具有字段的访问形式

'''
