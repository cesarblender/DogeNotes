from ariadne import QueryType
from controllers.getTasks import getTasks
from controllers.getTask import getTask

query = QueryType()

def setQueries(mongo):
  @query.field('getTasks')
  def getTasksResolver(_, info, token):
    return getTasks(token, mongo)

  @query.field('getTask')
  def getTaskResolver(_, info, _id, token):
    return getTask(_id, token, mongo)
  
  return query