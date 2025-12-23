import mysql.connector
db = mysql.connector.connect(host="localhost",user="root",password="your_passwowd",database="damastersbooklist")

dbCursor = db.cursor()

dbCursor.execute("DELETE FROM bookdetail WHERE Rating=3")

db.commit()
