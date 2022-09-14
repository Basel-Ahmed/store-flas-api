################
#he send #########
# how authentication happen
#when user access auth endpoint he send username and apssword with request payload
#these data is passed to the authenticaete method so that to make suere they are correct
#compare password give with password in database

#if correct it return the user object that used to generate token for this user object
#so if  iam trying to access an end point that need to be authenticated decorated
#i will get teh payload
#get the identity value and compre the user id in ti with user id in the data base





#######################
import hmac
from user import User
#users = [User(1,'bob' , 'asdf')]

#username_mapping = {u.username:u for u in users}
#userid_mapping = {u.id:u for u in users}



#if user gave me the correct username and apssword
#i will send the all inofrmation to him 
def authenticate(username,password):
    user = User.find_by_username(username)
    #user = username_mapping.get(username,None)
    if user and hmac.compare_digest(user.password, password):
        return user


def identity(payload):
    user_id = payload['identity']
    user = User.find_by_id(user_id)
    return user
