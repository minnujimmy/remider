import pymysql
import datetime

currentDT = datetime.datetime.now()

#DataBase Connection
db = pymysql.connect("localhost","root","admin","MYDATABASE")

#Cursor Object
cursor = db.cursor()

#Create And Showing DataBase
"""
cursor.execute("CREATE DATABASE MYDATABASE")
cursor.execute("SHOW DATABASES")
for db in cursor:
	print(db)
"""

#Create Table
#Date Format - 'YYYY/MM/DD'
"""
sqltable = "CREATE TABLE BIRTHDAY (ID INT(2), NAME VARCHAR(20), DATE VARCHAR(20))"
cursor.execute(sqltable)
"""

#Insert into Table
#sqlinsert2 = "INSERT INTO BIRTHDAY (ID, NAME, DATE) VALUES (1,'JOYAL','2019/12/20')"
#cursor.execute(sqlinsert2)

#Delete Full Table Entries
"""
sqldelete = "TRUNCATE TABLE BIRTHDAY"
cursor.execute(sqldelete)
"""

#Get CurrentDate

currentdate =  (currentDT.strftime("%Y/%m/%d"))
st = str(currentdate)
print (st)


# "SELECT NAME FROM BIRTHDAY WHERE DATE = DATE_FORMAT(date,'%Y/%m/%d') "
#Select Names from Table

#cursor.execute("select CURDATE()")

sqldate = "SELECT NAME FROM BIRTHDAY WHERE DATE = CURDATE()"
cursor.execute(sqldate)

row = cursor.fetchall()
if row:
    for raw in row:
        print(raw)

#Commiting
db.commit()

#Closing Connection
db.close
