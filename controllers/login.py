from jwt import encode
from os import environ
from werkzeug.security import check_password_hash
from libs.registerAuth import validatePassword
from bson.json_util import dumps
from ast import literal_eval

def login(email, password, mongo):
  passwordValidation = validatePassword(password)
  
  if passwordValidation != True: return passwordValidation

  user = mongo.db.users.find_one({
    "email": email
  })
  
  if user == None: return {
    "error": "The user does not exist."
  }

  user = dumps(user)
  user = literal_eval(user)

  if check_password_hash(user['password'], password) != True: return {
    "error": "Incorrect password."
  }

  del user['password']
  user['_id'] = user['_id']['$oid']

  token = encode(user, environ['TOKEN_SECRET'], algorithm='HS256')

  return {
    "token": token,
    "user": user,
  }