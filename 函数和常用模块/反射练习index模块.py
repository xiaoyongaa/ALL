#import commad

def run():
    choose=input("请输入你要访问的页面: ")
    m,f=choose.split("/")
    print(m,f)
    m=__import__("commad",fromlist=True)   #导入所有路径的模块
    if hasattr(m,f)==True:
        fun=getattr(m,f)
        fun()
    else:
        print("404")


run()
