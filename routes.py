from ariadne import graphql_sync
from ariadne.constants import PLAYGROUND_HTML
from flask import request, redirect, jsonify

def loadRoutes(app, schema):
  @app.route('/appas', methods=['GET'])
  def appas():
    return "Hello appas"

  @app.route('/')
  def home():
      return redirect('/graphql', 302)


  @app.route("/graphql", methods=["GET"])
  def graphql_playground():
      return PLAYGROUND_HTML, 200


  @app.route("/graphql", methods=["POST"])
  def graphql_server():
      data = request.get_json()
      success, result = graphql_sync(schema,
                                    data,
                                    context_value=request,
                                    debug=app.debug)

      status_code = 200 if success else 400
      return jsonify(result), status_code