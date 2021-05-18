from ariadne import MutationType
from controllers.register import register
from controllers.createTask import createTask
from controllers.deleteTask import deleteTask
from controllers.editTask import editTask
from controllers.login import login

mutation = MutationType()

def setMutations(mongo):
  @mutation.field("register")
  def registerResolver(_, __, name, email, password):
    return register(name, email, password, mongo)

  @mutation.field('login')
  def loginResolver(_, __, email, password):
    return login(email, password, mongo)
  
  @mutation.field('createTask')
  def createTaskResolver(_, __, title, description, time, token): 
    return createTask(title, description, time, token, mongo)
  
  @mutation.field('editTask')
  def editTaskResolver(_, __, _id, token, title, description, createdAt, done): 
    return editTask(_id, title, description, createdAt, token, mongo)
  
  @mutation.field('deleteTask')
  def deleteTaskResolver(_, __, _id, token): 
    return deleteTask(_id, token, mongo)
  
  return mutation