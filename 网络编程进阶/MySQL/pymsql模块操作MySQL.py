import pymysql
conn=pymysql.connect(host="10.0.0.25",port=3306,user="xiaoyong",passwd="1")
cursor=conn.cursor(cursor=pymysql.cursors.DictCursor)
sql="select * from {path}".format(path="s13.t10")
sql2="select * from {path}".format(path="s13.t11")
cursor.execute(sql)


result=cursor.fetchall()
print(result)

cursor.execute(sql2)
result=cursor.fetchall()
print(result)

conn.commit()
cursor.close()
conn.close()