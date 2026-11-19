import pymysql
mydb = pymysql.connect(host = "localhost",user = "root",password="")
mycursor = mydb.cursor()


mycursor.execute("create database if not exists python")
mydb.commit()


mydb = pymysql.connect(host = "Localhost",user="root",password="",database="python")
mycursor = mydb.cursor()

mycursor.execute("create table if not exists python (id int primary key auto_increment, name varchar(50),mobile bigint)")
mydb.commit()