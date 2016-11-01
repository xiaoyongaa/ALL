from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine
engine=create_engine("mysql+pymysql://xiaoyong:1@10.0.0.25:3306/s13",max_overflow=5)  #链接数据库
Base=declarative_base()

class Users(Base):
#一对一
    __tablename__="users"  #表名
    id=Column(Integer,primary_key=True)
    name=Column(String(32))
    extra=Column(String(16))

    __table_args__=(
        UniqueConstraint("id","name",name="uix_id_name"),
        Index("ix_id_name","name","extra")
    )

#一对多
class Favor(Base):
    __tablename__="favor"
    nid=Column(Integer,primary_key=True)
    caption=Column(String(50),default="red",unique=True)


class Person(Base):
    __tablename__="person"
    nid=Column(Integer,primary_key=True)
    name=Column(String(32),index=True,nullable=True)
    favor_id=Column(Integer,ForeignKey("favor.nid"))

# 多对多
class ServerToGroup(Base):
    __tablename__="servertogroup"
    nid=Column(Integer,primary_key=True,autoincrement=True)
    server_id=Column(Integer,ForeignKey("server.id"))
    group_id=Column(Integer,ForeignKey("group.id"))

class Group(Base):
    __tablename__="group"
    id=Column(Integer,primary_key=True)
    name=Column(String(64),unique=True,nullable=False)

class server(Base):
    __tablename__="server"
    id=Column(Integer,primary_key=True,autoincrement=True)
    hostname=Column(String(64),unique=True,nullable=False)





#unique=true是指这个字段的值在这张表里不能重复，所有记录值都要唯一，就像主键那样
#nullable=false是这个字段在保存时必需有值

# Base.metadata.create_all(engine)  #创建表
# Base.metadata.drop_all(engine)  #删除表


#修改表
#增加
session=sessionmaker(bind=engine)  #创建增加
session=session()
#
# obj=Users(name="alex",extra="sss")   #创建表对象。传递进去字段值
# obj2=Users(name="a",extra="a")
# #session.add(obj)
# session.add_all([obj,obj2])  #增加多条数据，把对象obj，obj2放在列表里面传递
# session.commit()  #提交
# #session.add_all()


#删除数据
# session.query(Users).filter(Users.id==2).delete()
# session.commit()


#改User表数据
# session.query(Users).filter(Users.id==1).update({"name":"911","extra":"111"})
# session.commit()


#查
obj=session.query(Users).all()
obj2=session.query(Users).filter(Users.name=="alex").all()
#print(obj[0].id,obj[0].name)
print(obj2[0].name)







