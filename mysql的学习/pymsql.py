import pymysql
conn=pymysql.connect(host="192.168.1.10",port=3306,user="root",passwd="1")
cursor=conn.cursor(cursor=pymysql.cursors.DictCursor)

sql="select * from s13.t10"
sql="UPDATE s13.t10 set price=1000 WHERE id=1"
sql="INSERT INTO s13.t10(name,price,type_id) VALUES(\"c4\",\"2000\",\"2\")"
sql="SELECT * FROM s13.t10"

hangshu=cursor.execute(sql)
print(hangshu)

date=cursor.fetchall()
#ursor.scroll(-2)
# date=cursor.fetchall()  #相对位置向上移动2个位置
# print(date)
print(date)

conn.commit()
cursor.close()
conn.close()
# new_id=cursor.lastrowid
# print(new_id)  #获取自增列