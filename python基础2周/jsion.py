import json
user_infor={"user":1,"password":2}
print(user_infor,type(user_infor))
h=json.dumps(user_infor)  #变成字符串了写进h
print(h,type(h))