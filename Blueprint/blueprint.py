from flask import Blueprint, jsonify
from flask_restx import Api

from Blueprint.v1.v1 import namespace as v1_namespace

blueprint = Blueprint('Meme APIs', __name__, url_prefix='/meme')


@blueprint.errorhandler(404)
def route_not_found(e):
    return jsonify(error=str(e)), 404


api = Api(blueprint, title='Meme APIs', description='9GAG Web Extractor APIs Application')

api.add_namespace(v1_namespace, path='/v1')
