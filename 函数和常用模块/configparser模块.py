import configparser
config=configparser.ConfigParser()  #创建个对象
config.read("zhi.txt","utf-8")   #告诉对象加载什么
ret=config.sections()
print(ret)













