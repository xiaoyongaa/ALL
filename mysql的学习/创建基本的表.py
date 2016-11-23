create table s13.t10(
id int not null auto_increment PRIMARY key,
name varchar(255),
price int,
type_id int,
constraint t10_t0_t11 FOREIGN key(type_id) references t11(id)
)




SELECT * FROM t10 LEFT JOIN t11 on t10.type_id=t11.id