import mysql.connector
db = mysql.connector.connect(host="localhost",user="root",password="your_passwowd",database="grocery")

dbCursor = db.cursor()

dbCursor.execute("Update bookdetail SET Price=500 WHERE Rating>4")

db.commit()
