from flask import request
from flask_restx import Namespace, Resource

from Blueprint.v1.models.models import *
from Blueprint.v1.services.search import search
from Blueprint.v1.services.homepage import homepage

namespace = Namespace('v1', description='Version 1.0')

search_request_data = namespace.model("search_request_data", search_request_data_model)
homepage_request_data = namespace.model("homepage_request_data", homepage_request_data_model)
response_data = namespace.model("response_data", response_data_model)


class DefaultErrorHandle(Exception):
    pass


@namespace.errorhandler(DefaultErrorHandle)
def default_error_handle():
    return input_error_response, 500


@namespace.route("/search")
@namespace.doc(search_request_data)
class Search(Resource):
    @namespace.expect(search_request_data)
    @namespace.response(200, 'Success Response Received', response_data)
    def post(self):
        try:
            post_data = request.json
            search_query = post_data['search_query']
            cursor = post_data['cursor']
            return search(search_query, cursor)
        except:
            return default_error_handle()


@namespace.route("/homepage")
@namespace.doc(homepage_request_data)
class Homepage(Resource):
    @namespace.expect(homepage_request_data)
    @namespace.response(200, 'Success Response Received', response_data)
    def post(self):
        try:
            post_data = request.json
            homepage_query = post_data['homepage_query']
            cursor = post_data['cursor']
            if homepage_query in {'hot', 'trending', 'fresh'}:
                outpit = homepage(homepage_query, cursor)
                return outpit
            else:
                return default_error_handle()
        except:
            return default_error_handle()
