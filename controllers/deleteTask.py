from jwt import decode
from os import environ
from bson import json_util, ObjectId
from ast import literal_eval

def deleteTask(_id, token, mongo):
  user = decode(token, environ['TOKEN_SECRET'], algorithms=['HS256'])

  deletion = mongo.db[user['_id']].find_one_and_delete({"_id": ObjectId(_id)})
  deletion = json_util.dumps(deletion)

  if deletion == 'null': return {
      "done": False
    }
  
  return {
    "done": True
  }