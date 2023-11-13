# This application consists of three parts: Flask, Graphene, and SQLAlchemy
# This file is the Flask support.


from flask import Flask
from flask_graphql import GraphQLView as View
from schema import schema
from db import session

app = Flask(__name__)
app.debug = True
app.add_url_rule("/", view_func=View.as_view("graphql", graphiql=True, schema=schema))

@app.teardown_appcontext
def shutdown_session(Error=None):
    session.remove()

def main():
    app.run()

if __name__ == "__main__":
    main()
