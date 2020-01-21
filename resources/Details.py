from flask import request
from flask_restful import Resource
from Model import db, DetailesSchema, Detailes
import json

details_schema = DetailesSchema(many=True)
detail_schema = DetailesSchema()


class DetailsResource(Resource):
    @staticmethod
    def get():
        datails = Detailes.query.all()
        detailes = details_schema.dump(datails)
        return {'status': 'success', 'data': detailes}, 200

    @staticmethod
    def post():
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate data and deserialize inputs
        response = json.dumps(json_data)
        data = detail_schema.loads(response)
        detail = Detailes.query.filter_by(address=data['address']).first()
        if detail:
            return {'message': 'Location already exists'}, 400
        detail = Detailes(
            age=data['age'],
            address=data['address'],
            country_origin=data['country_origin']
        )

        db.session.add(detail)
        db.session.commit()

        result = detail_schema.dump(detail)

        return {'status': 'success', 'data': result}, 201