import mysql.connector

conn= mysql.connector.connect(
 host="localhost",
 user="root",
 password="Hari@2002",
 database="project")
mycursor = conn.cursor()
if conn.is_connected():
      print("now we connected to the mysql database")

#mycursor.execute("CREATE DATABASE project")
#mycursor.execute("SHOW DATABASES")

#for x in mycursor:
#  print(x)
#mycursor.execute("CREATE TABLE NODE(NODE_ID INT PRIMARY KEY, ENERGY INT NOT NULL,F_RATE INT NOT NULL, C_NODE INT NOT NULL,T_INDEX INT NOT NULL)")
'''sql = "INSERT INTO NODE(node_id,energy,f_rate,c_node,t_index) VALUES (%s, %s,%S,%S,%s)"
val = (546549,13,14,15,32)
conn.commit()

print(mycursor.rowcount, "record inserted.")'''

mycursor.execute("SELECT * FROM node")

result = mycursor.fetchall()

for x in result:
  print(x)
