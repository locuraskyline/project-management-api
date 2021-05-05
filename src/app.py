#!/usr/bin/python3 

from flask import Flask, jsonify, request
import json


from src.infrastructure import orm
from src.domain.model import Feature
from src.application import services, unit_of_work

app = Flask(__name__)
orm.start_mappers()

@app.route("/")
def index():
    return "index"

@app.route("/tasks", methods=["GET"])
def get_all_tasks():
    return "get_all_response"

@app.route("/task/<id>", methods=["GET"])
def get_task_by_id(id):
    return "get_task_by_id(%s)" %(id)

@app.route("/task", methods=["POST"])
def add_task():
    #task = Feature(request.json['title'], request.json['link'])
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