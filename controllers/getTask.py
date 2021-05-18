from jwt import decode
from os import environ
from bson.json_util import dumps
from bson import ObjectId
import json

def getTask(_id, token, mongo):
  user = decode(token, environ['TOKEN_SECRET'], algorithms=['HS256'])

  task = mongo.db[user['_id']].find_one({"_id": ObjectId(_id)})

  task = dumps(task)
  
  print(type(task))

  if task == 'null':
    return {
      "error": "The task does not exist."
    }

  task = json.loads(task)

  print(task)

  task['_id'] = task['_id']['$oid']
  
  return task