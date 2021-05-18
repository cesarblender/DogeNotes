from jwt import decode
from os import environ
from bson import ObjectId

def editTask(_id, title, description, time, token, mongo):
  user = decode(token, environ['TOKEN_SECRET'], algorithms=['HS256'])

  task = {
    "title": title,
    "description": description,
    "createdAt": time,
    "done": False,
  }

  mongo.db[user['_id']].find_one_and_replace({"_id": ObjectId(_id)}, task)

  return {
    "done": True
  }