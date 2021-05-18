from jwt import encode
from os import environ
from werkzeug.security import generate_password_hash
from libs.registerAuth import validatePassword, checkEmail
from bson.json_util import dumps
from ast import literal_eval

def register(name, email, password, mongo):
  passwordValidation = validatePassword(password)
  emailChecking = checkEmail(email)

  if passwordValidation != True: return passwordValidation
  if emailChecking != True: return emailChecking
  if len(name) < 2: return { "error": "The name is too short." }

  hashedPassword = generate_password_hash(password)

  user = {
    "name": name,
    "email": email,
    "password": hashedPassword,
  }
  existentUser = mongo.db.users.find({
    "email": email
  })
  existentUser = dumps(existentUser)

  if len(existentUser.split()) > 2:
    return {
      "error": "This email is already registered."
    }

  mongo.db.users.insert_one(user)

  newUser = mongo.db.users.find_one(user)
  newUser = dumps(newUser)

  newUser = literal_eval(newUser)

  del newUser['password']
  newUser['_id'] = newUser['_id']['$oid']

  token = encode(newUser, environ['TOKEN_SECRET'], algorithm='HS256')

  return {
    "token": token,
    "user": newUser,
  }