#Connection
import sqlite3
connection=sqlite3.connect('databasec.db')
cursor=connection.cursor()

#Create
# cursor.execute('create table student(name varchar(20),id int,fee number(10,2))')
print('Table created successfully')
# cursor.execute("insert into student (name,id,fee) values('Rajesh',1,10.45)")
# cursor.execute("insert into student values('Ibrahim',2,11.234)")
# cursor.execute("insert into student values('Sahastra',3,12.23)")
# cursor.execute("insert into student values('Harsh',4,13.2)")
# connection.commit()
# cursor.execute("delete from student where id=3")
# cursor.execute("insert into student values('vishnu',3,15.2)")
cursor.execute("update student set name='vishnupriya' where id=3")
connection.commit()
cursor.close()