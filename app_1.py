#first create end pont host:4000/auth take care of http not https 
#header content type   application/json

#then in body write the username and password in dictionary 
# send then copy the token without "" goto the end point that i decorized
# header authoriztion value JWT token

# all other not decorized will not get affected
# jwt will be expired each period






# status code 200 for get request ok
# 201 fo post request created successfully
#202 item created but delayed
# 404 item you would like to access is not found
# 400 mean bad request that for example https https  or coding items of name as items already exist
# internal server error mean that there is error in syntaax of the code 

from flask import Flask, request
from flask_restful import Resource, Api  # to parse the request and josn payload
# api from restful allow us to add these resource very easily to api
# that for exmapl for this resource you can get and post and for this you can 



#authorization
from flask_jwt import JWT

from security import authenticate, identity

from user import UserRegister
from item import Item, ItemList
app = Flask(__name__)
app.secret_key = 'beso' # must be long, complicated and not visible
api = Api(app)
jwt = JWT(app, authenticate, identity)



# determine the resources that a user will need to get or create
# informaion he may need to know or may need to create
# think in OOP resource as class

# for each one define a classs that inheret from Resource
# Deine the methods that the use can use to access the resource
# GET and Post
#the error code i need to show if resource can not be found 404

# finally don't forget to add reource to the api class, and the end point +info passed to the end point 
# api.add_resource(Student, '/student/name')
# creating properly use request variable and get json this require content based and application/josn header if not raise and error
# how to prevent error 1 - force = True mean that i am gonna to process the text if it's not correct
# 2 -  use silent = True it will not raise and error jsut return none
# always return dictionary
#error codes
# getting a resource does not exist 404 if exist 200
# creating item already exist it's a bad request 400

# tell our api that this resource is now can be accessible through get but where is the end point the route how we gonna access what i should write after the host to access this resource
api.add_resource(Item , '/item/<string:name>')  # same as @app.route()
api.add_resource(ItemList , '/items')
api.add_resource(UserRegister , '/register')
app.run("0.0.0.0")

