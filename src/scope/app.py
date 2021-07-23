#!/usr/bin/python3 

from flask import Flask
from flask_restx import Api

from scope.infrastructure import orm
from scope.infrastructure.resources import api as task

app = Flask(__name__)
api = Api(app, title='Scope', version='1.0')
api.add_namespace(task)

orm.start_mappers()

if __name__ == '__main__':
    app.run(debug=True)