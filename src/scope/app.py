#!/usr/bin/python3 

from flask import Flask, jsonify, request
import json

from scope.infrastructure import orm
from scope.domain.model import Feature
from scope.application import services, unit_of_work

app = Flask(__name__)
orm.start_mappers()

@app.route("/")
def index():
    return "index"

# @app.route("/init", methods=["GET"])
# def init():
#     orm.init_database()
#     return "init_database_success"


@app.route("/tasks", methods=["GET"])
def get_all_tasks():
    features = services.get_all_features(unit_of_work.SqlAlchemyUnitOfWork())
    #TO_DO serialize object response
    #return jsonify(features)
    return "get_all_response"

@app.route("/task/<id>", methods=["GET"])
def get_task_by_id(id):
    feature = services.get_feature(id, unit_of_work.SqlAlchemyUnitOfWork())
    return f"{feature.title} | {feature.link} | {feature.state.name}"

@app.route("/task", methods=["POST"])
def add_task():

    services.add_feature(
        request.json['title'],
        request.json['link'],
        unit_of_work.SqlAlchemyUnitOfWork()
    )
    #print(JSONEncoder.default({},task))
    # return jsonify({request}), 201
    #return jsonify({"titulo": "Hola 1", "genero": "Terror", "anio": "1989"})
    #return jsonify({"result": task.__dict__}), 201
    return "OK", 201

if __name__ == '__main__':
    app.run(debug=True)