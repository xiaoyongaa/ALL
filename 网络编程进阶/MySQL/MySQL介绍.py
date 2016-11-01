INSERT INTO s13.t2(name) VALUES('xx'),('dasdasdas');
UPDATE s13.t2 set name='77777' WHERE nid>3;
SELECT * FROM s13.t2


##连表操作

#SELECT * FROM s13.t10 LEFT JOIN s13.t11 on s13.t10.type_id=s13.t11.id
#SELECT * FROM s13.t10 	RIGHT JOIN  s13.t11 on s13.t10.type_id=s13.t11.id
#SELECT * FROM s13.t10 	INNER JOIN  s13.t11 on s13.t10.type_id=s13.t11.id



#组合
#SELECT name FROM s13.t10 UNION SELECT NAME FROM s13.t11  #去重
#SELECT name FROM s13.t10 UNION ALL SELECT NAME FROM s13.t11  #不去重
