
from flask.globals import request
from flask_restx import Namespace, Resource, fields, cors
from flask_restx.reqparse import LOCATIONS
from sqlalchemy.sql.sqltypes import Integer

from scope.application import services, unit_of_work

api = Namespace("task", description="Tasks related operations", decorators=[cors.crossdomain(origin="*")])

task_parser = api.parser() \
    .add_argument(
        "title", type=str, required=True, help="The task title", location="form"    
    ) \
    .add_argument(
        "link", type=str, required=False, help="The task link", location="form"
    ) \
    .add_argument(
        "parent_id", type=str, required=False, help="The task parent relationship", location="form"
    )

task_fields = api.model('Task', {
    'id': fields.Integer,
    'title': fields.String,
    'link': fields.String,
    'state': fields.String
})

@api.route("/")
class TaskList(Resource):
    @api.marshal_list_with(task_fields)
    def get(self):
        features = services.get_all_features(unit_of_work.SqlAlchemyUnitOfWork())

        return features

    @api.doc(parser=task_parser)
    def post(self):
        args = task_parser.parse_args()
        
        services.add_feature(
            args['title'],
            args['link'],
            args['parent_id'],
            unit_of_work.SqlAlchemyUnitOfWork()
        )

        return 'OK', 201

@api.route("/<int:id>")
class Task(Resource):
    @api.marshal_with(task_fields)
    def get(self, id):
        feature = services.get_feature(id, unit_of_work.SqlAlchemyUnitOfWork())
        
        return feature

    @api.marshal_with(task_fields)
    def put(self):
        NotImplementedError

@api.route("/<int:id>/childs")
class Task(Resource):
    @api.marshal_list_with(task_fields)
    def get(self, id):
        features = services.get_feature_childs(id, unit_of_work.SqlAlchemyUnitOfWork())

        return features