while True:
    p1=input("请输入第一个数字：")
    p2=input("请输入第二个数字：")
    try:
        p1=int(p1)
        p2=int(p2)
        print(p1+p2)
        li=[]
        li[100]
    except ValueError as ex:
        print(ex)    #捕获了错误信息
    except IndexError as ex:
        print(ex)
    except Exception as all:  #ex是Exception的对象.ex封装了所有错误信息
        print(all())