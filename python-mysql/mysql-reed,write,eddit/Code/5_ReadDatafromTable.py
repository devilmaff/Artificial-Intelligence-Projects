import mysql.connector
db = mysql.connector.connect(host="localhost",user="root",password="your_passwowd",database="grocery")

dbCursor = db.cursor()
query="SELECT * FROM grocery.product"
dbCursor.execute(query)

result = dbCursor.fetchall()

for i in result:
    print(i)
