import mysql.connector
mydb=mysql.connector.connect(host='localhost', user='pysql', passwd='1234', database='home')
mycursor = mydb.cursor()
mycursor.execute('select * from cricket;')
for i in mycursor:
    print(i)