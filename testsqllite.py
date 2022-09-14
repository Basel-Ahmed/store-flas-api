import sqlite3
import os
# initialize the connection
#put the unified reosurce identifier URI
if os.path.exists('data.db'):
    os.remove('data.db')

connection = sqlite3.connect('data.db')

#sqlite actually store all data in a file this file i can call it anywhere 
# is reposnsible for executing the queries
#that where to select and where to insert
#put the cursor on top of database 
cursor = connection.cursor()
#run the quesry and store results
create_table = "Create Table users(ID int,username text , password text)"# sxhema
cursor.execute(create_table)

#user = (1,'jose' , 'asdf')

users = [(2,'role' ,'asdf') , (3 , 'hanah' , 'asf') ]   # autoincrementing sequence  >>>>
insert_query = "Insert into users values (? ,? ,?)"
#cursor.execute(insert_query , users)

cursor.executemany(insert_query ,users) # will be executed many times one for each user 

select_query = "select * from users"
for row in cursor.execute(select_query):
    print(row)


connection.commit() # to save all changes to the disc
connection.close()
