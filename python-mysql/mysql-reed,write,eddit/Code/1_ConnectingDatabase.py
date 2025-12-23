import mysql.connector 
db = mysql.connector.connect(host="localhost",user="root",password="your_passwowd",database="store")
if db:
  print("Connection successful")
else:
  print("Connection Failed")
