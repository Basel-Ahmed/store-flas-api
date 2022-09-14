
import sqlite3
from flask_restful import Resource,reqparse
from flask_jwt import JWT,jwt_required



class Item(Resource):
    # name of student

    parser =reqparse.RequestParser()
    parser.add_argument("price" , type = float , required = True , help = "There is no item without price")
    #data = parser.parse_args() #is dictionary
        


    # i don't have to use jsonify flaskrestful do it for us
    #@jwt_required()
    def get(self , name):
        item = self.find_by_name(name)
        if item:
            return item
        

        return {"Message" : "Item not found"} , 404
        
    @classmethod    
    def find_by_name(cls,name):
        connection = sqlite3.connect("Data.db")
        cursor = connection.cursor()
        query = "select * from items where name=?"
        result = cursor.execute(query,(name,))
        row =result.fetchone()
        connection.close()
        if row:
            return {"item":{"name" : row[0] , "price" : row[1]}}
        
        
        

# Also instead of sending the name of store i would like to create in the
# payload  instead it will be based as a parameter
    def post(self ,name):
        
        
        data = Item.parser.parse_args() #is dictionary
        if self.find_by_name(name):
            return {"Message" : "This item already exist"},400

        else:
            item = {"name":name , "price":data['price']}
            #try:
                
            self.insert(item)
            return {"item":item},201
            #except:
             #   return {"Message" : "An error occured during insertion"} , 500
                    
            
            


    @classmethod
    def insert(cls ,item):
        connection = sqlite3.connect("Data.db")
        cursor = connection.cursor()
        
        query = "insert into items values(?,?)"
        result = cursor.execute(query ,(item['name'] , item['price']))
        
        connection.commit()
        connection.close()
    
    def delete(self,name):
        
        if self.find_by_name(name):
            
            connection = sqlite3.connect("Data.db")
            cursor = connection.cursor()
            query = "delete from items where name=?"
            cursor.execute(query , (name,))
            connection.commit()
            connection.close()
            return {"Message" :"item deleted successfully"}
        else:
            return {"Message" : "There is no item with this name exist"}





    @classmethod
    def update(self,item):
        connection = sqlite3.connect("Data.db")
        cursor = connection.cursor()
        query = "update items set price=? where name=?"
        cursor.execute(query , (item['price'] , item['name']))
        connection.commit()
        connection.close()
        
    def put(self,name):

        data = Item.parser.parse_args() # dictionary contain name of argument value
        # if i tried to access any key rather than price it will raise key error
        # because data i didn't determined that i will pass value or argument i only say i will
        # send value for price argumnet
        # controlling fileds exist in request this fieldmuts exist , you are giving me data not related  
        #data = request.get_json()
        # check if item exist or not
        item=self.find_by_name(name)
        updated_item = {'name':name , 'price':data['price']}
        
        #item = next(filter(lambda x:x['item']['name']==name , items),None)
        # if exist update it
        if item:
            self.update(updated_item)
        else:
            self.insert(updated_item)
            #items.append(item)
        return updated_item

class ItemList(Resource):
    def get(self):

        connection = sqlite3.connect("Data.db")
        cursor = connection.cursor()

        query = "Select * from items"
        result = cursor.execute(query)

        items = []
        for row in result:
            items.append({'name':row[0] , 'price': row[1]})
        
        connection.close()
        return {'items' : items}
