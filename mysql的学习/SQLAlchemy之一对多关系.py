from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine
connect="mysql+pymysql://root:1@192.168.1.10:3306/s13"
engine=create_engine(connect)
Base=declarative_base()
###
session=sessionmaker(bind=engine)
session=session()
######


#单表
class Test(Base):
    __tablename__="test"
    nid=Column(Integer,primary_key=True,autoincrement=True)
    name=Column(String(32))
#单表

#1对多链表
class Group(Base):
    __tablename__="group"
    nid=Column(Integer,primary_key=True,autoincrement=True)
    caption=Column(String(32))

class User(Base):
    __tablename__="user"
    nid=Column(Integer,primary_key=True,autoincrement=True)
    username=Column(String(32))
    group_id=Column(Integer,ForeignKey("group.nid"))  #建立外键
    #group=relationship("Group", backref='uuu')

    # def __repr__(self):
    #     temp="nid:{nid},username:{username},gouup_id:{group}".format(nid=self.nid,username=self.username,group=self.group_id)
    #     return  temp

def init_db():
    Base.metadata.create_all(engine)

def drop_db():
    Base.metadata.drop_all(engine)

#init_db()

# session.add_all([
#     User(username="alex1",group_id=1),
#     User(username="alex2",group_id=1)
# ])
# session.commit()

# result=session.query(User).filter(User.username=="alex1").all()
# print(result[0].nid,result[0].username)

#连表查询
# sql=session.query(User,Group).join(Group)
# print(sql)
# result=session.query(User.nid,User.username,User.group_id,Group.caption).join(Group).all()
# print(result)

# result=session.query(User).all()
# print(result)
# for i in result:
#     print(i.nid,i.username,i.group_id,i.group.nid,i.group.caption)
# result=session.query(User.username,User.group_id,Group.caption).join(Group).filter(Group.caption=="dba").all()
# print(result,len(result))


#reslut=session.query(Group).filter(Group.caption=="dba").all()




result=session.query(User.username,User.group_id,Group.caption).join(Group).filter(Group.caption=="dba").all()
print(result)


