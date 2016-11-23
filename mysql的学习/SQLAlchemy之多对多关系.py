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

class Host(Base):
    __tablename__="host"
    nid=Column(Integer,primary_key=True,autoincrement=True)
    hostname=Column(String(32))
    port=Column(String(32))
    ip=Column(String(32))

class Host_User(Base):
    __tablename__="host_user"
    nid=Column(Integer,primary_key=True,autoincrement=True)
    username=Column(String(32))


class Host_to_HostUser(Base):
    __tablename__="host_to_hostuser"
    nid=Column(Integer,primary_key=True,autoincrement=True)
    host_id=Column(Integer,ForeignKey("host.nid"))
    host_user_id=Column(Integer,ForeignKey("host_user.nid"))

def init_db():
    Base.metadata.create_all(engine)




init_db()
# session.add_all([
#     Host(hostname="c1",port="22",ip="1.1.1.1"),
#     Host(hostname="c2",port="22",ip="1.1.1.2"),
#     Host(hostname="c3",port="22",ip="1.1.1.3"),
#     Host(hostname="c4",port="22",ip="1.1.1.4"),
#     Host(hostname="c5",port="22",ip="1.1.1.5"),
# ])
#
# session.commit()
# session.add_all([
#     Host_User(username="root"),
#     Host_User(username="db"),
#     Host_User(username="nb"),
#     Host_User(username="sb"),
# ])
#
# session.commit()

# session.add_all([
#     Host_to_HostUser(host_id=1,host_user_id=1),
#     Host_to_HostUser(host_id=1,host_user_id=2),
#     Host_to_HostUser(host_id=1,host_user_id=3),
#     Host_to_HostUser(host_id=2,host_user_id=2),
#     Host_to_HostUser(host_id=2,host_user_id=4),
#     Host_to_HostUser(host_id=2,host_user_id=3),
# ])
#
# session.commit()
#
# host=session.query(Host).filter(Host.hostname=="c1").first()   #取出第一个hostname=c1的数据
# print(host.nid)
#
# result=session.query(Host_to_HostUser.host_user_id).filter(Host_to_HostUser.host_id==host.nid).all()  #拿到host表中对应的nid的服务器信息
# print(result)
# #[(1,), (2,), (3,)]
# #[1,2]
# new_list=[]
# for i in result:
#     i=str(i)
#     i=i.replace("(","")
#     i=i.replace(")","")
#     i=i.replace(",","")
#     new_list.append(i)
# print(new_list)
#
# r=zip(*result)
# #print(list(r)[0])
# result=session.query(Host_User.username).filter(Host_User.nid.in_(new_list)).all()
# print(result)
#

# host_nid=session.query(Host.nid).filter(Host.hostname=="c1").all()
# host_nid=str(host_nid)
# host_nid=host_nid.replace("[(","")
# host_nid=host_nid.replace(",)]","")
# hsot_to_hostuser_id=session.query(Host_to_HostUser.host_user_id).filter(Host_to_HostUser.host_id==host_nid).all()
# new_list=[]
# for i in hsot_to_hostuser_id:
#     i=str(i)
#     i=i.replace("(","")
#     i=i.replace(",)","")
#     new_list.append(i)
# hsot_user_username=session.query(Host_User.username).filter(Host_User.nid.in_(new_list)).all()
# print(hsot_user_username)











result=session.query(Host.hostname).filter(Host.ip.in_(["1.1.1.1"])).all()
print(result)




















































































































