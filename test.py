import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

create_table = "CREATE TABLE users (id int , name char , password char)"

cursor.execute(create_table)

user=(1,'mahmoud','456789')

insert_table = "INSERT INTO users VALUES (?,?,?)"
cursor.execute(insert_table,user)

select_query = "SELECT * FROM users"

for data in cursor.execute(select_query):
    print(data)

connection.commit()
connection.close()
