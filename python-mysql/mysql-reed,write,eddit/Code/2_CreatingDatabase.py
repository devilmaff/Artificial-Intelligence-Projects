import mysql.connector
db = mysql.connector.connect(host="localhost",user="root",password="your_passwowd")

dbCursor = db.cursor()
dbCursor.execute("Create database daMastersBooklist") #Create Database

dbCursor.execute("Show databases")#Show Database
for i in dbCursor:
  print(i)
