from flask import Blueprint
from flask_restful import Api

from resources.User import UserResource
from resources.Details import DetailsResource
from resources.TemplateRender import IndexResource, AddUser, AddDetails

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

template_bp = Blueprint('template', __name__)
template = Api(template_bp)

# Route
template.add_resource(IndexResource, '/')
template.add_resource(AddUser, 'addUser')
template.add_resource(AddDetails, 'addDetails')
api.add_resource(UserResource, '/User')
api.add_resource(DetailsResource, '/Details')