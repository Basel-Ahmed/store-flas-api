import sqlite3
from flask_restful import Resource, reqparse

class User():
    def __init__(self, _id,username ,password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        connection =sqlite3.connect('Data.db')
        cursor =connection.cursor()

        query ="select * from users where username=?"
        result = cursor.execute(query , (username,)) # not liek(5&l)*5
        row = result.fetchone() # if no rows return none froms result set
        if row:
            user = cls(*row) #==row[0] row[1]
        else:
            user =None

        connection.close()
        return user



    @classmethod
    def find_by_id(cls, _id):
        connection =sqlite3.connect('Data.db')
        cursor =connection.cursor()

        query ="select * from users where id=?"
        result = cursor.execute(query , (_id,)) # not liek(5&l)*5
        row =result.fetchone() # if no rows return none froms result set
        if row:
            user = cls(*row) #==row[0] row[1]
        else:
            user =None

        connection.close()
        return user
        

        
        
class UserRegister(Resource):
    # this http verb i will use to push my data for user to sign up not noly log in
    parser =reqparse.RequestParser()
    parser.add_argument("username" , type = str , required = True , help = "There is no user without username")
    parser.add_argument("password" , type = str , required = True , help = "There is no user without password")

    def post(self):
        data = UserRegister.parser.parse_args()
        if User.find_by_username(data['username']):
            return {"message":"user with that name already exist."}
        

        connection =sqlite3.connect('Data.db')
        cursor = connection.cursor()
        

        query = "INSERT INTO users VALUES (NULL ,? ,?)"
        cursor.execute(query , (data['username'] , data['password'],))

        connection.commit()
        connection.close()

        return {"message" : "User created successfully"} , 201
    
