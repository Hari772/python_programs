
import mysql.connector

conn= mysql.connector.connect(
 host="localhost",
 user="root",
 password="Hari@2002",
 database="project")
mycur.issor = conn.cursor()
if conn_connected():
      print("!!!! Now we connected to the mysql database  !!!!")

#n=int(input("How many nodes do you want to insert: "))
#for i in range(1,n+1):
a=int(input("Enter the node id: "))
b=int(input("Enter the energy: "))
c=int(input("Enter the forward rate: "))
d=int(input("Enter the consistency: "))
f=int((b+c+d)/3)
sql ="INSERT INTO NODE(node_id,energy,f_rate,c_node,t_index) VALUES (%s, %s,%S,%S,%s)"
val = (a,b,c,d,f)
mycursor.execute(sql,val)
print("Rows inserted successfully!!!")
conn.commit()


'''mycursor.execute("SELECT * FROM node")

result = mycursor.fetchall()

for x in result:
  print(x)'''
