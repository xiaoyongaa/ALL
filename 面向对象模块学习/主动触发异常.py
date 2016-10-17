try:
    raise Exception("主动错误")  #主动触发异常
    li=[]
    li[1000]
except ValueError as ex:
    print(ex)
except Exception as ex:
    print(ex)
else:     #如果不出错会执行
    print("pp")
finally:   #都会执行
    print("finally")