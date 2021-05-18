from jwt import decode
from os import environ
from bson.json_util import dumps
from ast import literal_eval

def createTask(title, description, time, token, mongo):
  user = decode(token, environ['TOKEN_SECRET'], algorithms=['HS256'])

  task = {
    "title": title,
    "description": description,
    "createdAt": time,
    "done": False,
  }

  id = mongo.db[user['_id']].insert(task)

  id = dumps(id)
  id = literal_eval(id)
  id = id['$oid']

  task['_id'] = id

  return task