from jwt import decode
from os import environ
from bson.json_util import dumps
import json

def getTasks(token, mongo):
  user = decode(token, environ['TOKEN_SECRET'], algorithms=['HS256'])

  tasks = mongo.db[user['_id']].find()

  tasks = dumps(tasks)
  tasks = json.loads(tasks)

  for i in range(len(tasks)):
    tasks[i]['_id'] = tasks[i]['_id']['$oid']
  
  return tasks