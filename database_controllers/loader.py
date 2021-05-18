from flask_pymongo import PyMongo

def loadDatabase(app):
  return PyMongo(app)