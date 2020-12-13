import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
  database_name="mypythondb"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mypythondb")

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x) 
