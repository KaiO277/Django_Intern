import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Kaio2772k2@",
    database = "bb_ex3",
    port = '4800'
)

myse = db.cursor()

myse.execute("SELECT * FROM Student")

for x in myse:
    print(x)