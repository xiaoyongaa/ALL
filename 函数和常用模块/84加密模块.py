import hashlib
jiami=hashlib.md5(bytes("d312",encoding="utf-8"))  #双重加密，先把一个对象加密,给一个对象保存
print(type(jiami))
jiami.update(bytes("123",encoding="utf-8")) #保存的对象加密密码
zhi=jiami.hexdigest() #加密完成给对象值
print(zhi,type(zhi))
