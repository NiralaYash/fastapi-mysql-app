import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="danksql",
    database="tunes"
)

mycursor = db.cursor()
mycursor.execute("SELECT * From Songs")

result = mycursor.fetchall()
for x in result:
    print(x)

db.close()