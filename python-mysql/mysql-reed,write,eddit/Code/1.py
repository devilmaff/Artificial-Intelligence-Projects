import mysql.connector

cnx = mysql.connector.connect(
    host="localhost",user="root",password="your_passwowd",database="grocery"
)

cursor = cnx.cursor()   
query="SELECT * FROM grocery.product"
cursor.execute(query)
for (product_id,Name,uom_id,price_per_unit) in cursor:
    print(product_id,Name,uom_id,price_per_unit)
cnx.close()
