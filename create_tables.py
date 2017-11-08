import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

create_table = "CREATE TABLE users (id INTEGER PRIMARY KEY , name char , password char)"
cursor.execute(create_table)

create_table = "CREATE TABLE items (id INTEGER PRIMARY KEY , name char , price int)"
cursor.execute(create_table)



connection.commit()
connection.close()
