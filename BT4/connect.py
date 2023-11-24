import psycopg2

conn = psycopg2.connect(
    host = "localhost",
    database = "dbbt4",
    user = "kai",
    port = "5432",
    password = "1234"
)

sele = conn.cursor()

query = "SELECT * FROM student;"

sele.execute(query)

result = sele.fetchall()

for row in result:
    print(row)

sele.close()
conn.close()


