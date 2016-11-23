from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine
import pymysql

connect="mysql+pymysql://root:1@192.168.1.10:3306/s13"
engine=create_engine(connect)
Base=declarative_base()
###
session=sessionmaker(bind=engine)
session=session()
##

#单表
class Users(Base):   #只能创建
    __tablename__="users"
    id=Column(Integer,primary_key=True)
    name=Column(String(32))
    extra=Column(String(16))

#一对多
class Favor(Base):
    __tablename__="favor"
    nid=Column(Integer,primary_key=True)
    caption=Column(String(50),default="red",unique=True)

class Person(Base):
    __tablename__="person"
    nid=Column(Integer,primary_key=True)
    name=Column(String(32),index=True,nullable=True)
    f_id=Column(Integer,ForeignKey("favor.nid"))

#多对多
class Group(Base):
    __tablename__="group"
    id=Column(Integer,primary_key=True)
    name=Column(String(64),unique=True,nullable=False)


class Server(Base):
    __tablename__="server"
    id=Column(Integer,primary_key=True,autoincrement=True)
    hostname=Column(String(64),unique=True,nullable=False)
    port=Column(Integer,default=22)

class servertogroup(Base):
    __tablename__="servertogroup"
    nid=Column(Integer,primary_key=True,autoincrement=True)
    server_id=Column(Integer,ForeignKey("server.id"))
    group_id=Column(Integer,ForeignKey("group.id"))

Base.metadata.create_all(engine)
#Base.metadata.drop_all(engine)

#obj=Users(name="xiaoyong")  #增加


# session.query(Users).filter(Users.id==7).update({"name":"321321"})   #修改
# session.commit()
# session.add(obj)
# session.query(Users).filter(Users.id==6).delete  #删除

# result=session.query(Users).all()  #查所有
# print(result[0].name,result[0].extra)


result=session.query(Users).all()

for i in result:
    print(i.id,i.name)


if (True,) in result:
    print("ok")
