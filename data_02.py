import mysql.connector

conn= mysql.connector.connect(
 host="localhost",
 user="root",
 password="Hari@2002",
 database="student")
mycursor = conn.cursor()
if conn.is_connected():
      print("!!!! Now we connected to the mysql database  !!!!")

#mycursor.execute("CREATE TABLE DETAILS(ROLL_NO INT PRIMARY KEY, NAME VARCHAR(20) NOT NULL,TOTAL_MARKS INT NOT NULL)")
# r=int(input("Enter the roll number: "))
# n=input("Enter the name: ")
# m=int(input("Enter the total marks: "))
# s="INSERT INTO DETAILS VALUES(%S,%S,%s)"
# t=(r,n,m)
# mycursor.execute(s,t)
# conn.commit()
