class xiaoyong(Exception):
    def __init__(self,msg):
        self.msg=msg
    def __str__(self):
        return self.msg


'''
try:
    raise xiaoyong("晓勇的异常")
except xiaoyong as ex:
    print(ex)
'''



#断言   assert 1==2
#断言相当于if else不满足条件主动抛异常
#assert 1==2
if 1==2:
    print("ok")
else:
    try:
        raise xiaoyong("dsadsad")
    except xiaoyong as ex:
        print(ex)