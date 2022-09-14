import sqlite3

connection =sqlite3.connect("Data.db")
cursor = connection.cursor()



# if i would like to create autoincrement column i need to use INTEGER fully
create_table = "CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username text, password TEXT)"
cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS items(name Text , price real)"
cursor.execute(create_table)

#cursor.execute("insert into items values('test' , 10.99)")

connection.commit()
connection.close()
