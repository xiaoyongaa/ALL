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

Base.metadata.create_all(engine)  #创建表
#Base.metadata.drop_all(engine)  #删除表




