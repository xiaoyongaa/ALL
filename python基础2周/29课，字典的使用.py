'''
id_db={
    32028319910128:{
        "name":"xiaoyong",
        "age":22,
        "addr":"shandong"
    },
    32028319910132132132128:{
        "name":"shanpao",
        "age":22,
        "addr":"shandong"
    },
    32132132132028319910128:{
        "name":"dashanpao",
        "age":22,
        "addr":"shandong"
    },
 }
print(id_db)
'''
#id_db[32028319910128]["name"]="yy"   #修改字典里面的值
#[32028319910128]["qq"]=23213444  #增加字典里面的值
#del id_db[32028319910128]["qq"]       #删除字典里面的值
#v=id_db.get(320283199101281)           #取出字典里面的值，假设没有，返回None
#print(v)
'''
dict2={
    1:"n",
        32028319910128:{
        "name":"xiaoyong",
        "age":27,
        "addr":"shandong"
    },
}
#id_db.update(dict2)     #字典的update方法，把原来数据覆盖了
#print(id_db)
#print(id_db.items())   #把字典转换成列表或者元组
#print(id_db.values())
#print(id_db.keys())     #常用，把资料里面的key取出来
print(id_db.setdefault(32028319910129,213))   #取出一个key，如果有就取出 没有就创建key并给valuse位None
print(id_db)
#print(dict.fromkeys([1,2,3,4],'ddd'))
#id_db.popitem()  随机删除一个元素
'''
l={
    11:{
      "name":"x",
       "age":22
    },
    22:{
        "name":"y",
        "age":23
    }
}
for key in l:
    print(key)



