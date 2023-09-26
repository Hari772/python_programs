import mysql.connector as c
import random as r

con= c.connect(
               host="localhost",
               user="root",
               password="Hari@2002",
               database="project")

cursor = con.cursor()
if con.is_connected():
      print("!!!! Now we connected to the mysql database  !!!!")

#if x=1
while True:
      
      node_id=input("Enter the value of node_id: ")
      energy=float(input("Enter the value of energy: "))
      f_rate=float(input("Enter the value of f_rate: "))
      c_node=float(input("Enter the value of c_node: "))
      t_index=float((energy+f_rate+c_node)/3)
      
      query="insert into node values({},{},{},{},{})".format(node_id,energy,f_rate,c_node,t_index)
      cursor.execute(query)                              
      con.commit()
      print("data inserted into successfully ")
      