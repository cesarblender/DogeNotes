from os import environ
from ariadne import make_executable_schema
from flask import Flask
from ariadne import load_schema_from_path
from resolvers.mutations import setMutations
from resolvers.queries import setQueries
from routes import loadRoutes
from database_controllers.loader import loadDatabase

uri = environ['DB_URI']

type_defs = load_schema_from_path('schema.graphql')

app = Flask(__name__)
app.config["MONGO_URI"] = uri
mongo = loadDatabase(app)
query = setQueries(mongo)
mutation = setMutations(mongo)

schema = make_executable_schema(type_defs, query, mutation)

loadRoutes(app, schema)

app.run(port=8080, host="0.0.0.0", debug=True)
