import psycopg2

url = "postgres://qisdhdof:V3lMvlfdWzbO4-TLl-6M_vEWfUVlAvJQ@tai.db.elephantsql.com:5432/qisdhdof"
connection = psycopg2.connect(url)

cursor = connection.cursor()
cursor.execute("SELECT * FROM users;")
first_user = cursor.fetchone()

print(first_user)

connection.close()
