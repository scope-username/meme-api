from flask_restx import fields

search_request_data_model = {
    "search_query": fields.String(description="Query for search", required=True, example='dogs', type=str),
    "cursor": fields.Integer(description="cursor count", required=True, example='10', type=int)
}

homepage_request_data_model = {
    "homepage_query": fields.String(description="Query for homepage. ex:hot, trending, fresh", required=True, example='hot', type=str),
    "cursor": fields.Integer(description="cursor count", required=True, example='10', type=int)
}

response_data_model = {
    "meta": fields.Raw(description="Meta data", type=object),
    "data": fields.Raw(description="Posts, tags, next cursor data, ", type=object)
}

input_error_response = {
    "Message": "Something went wrong. Please check the inputs and try again"
}

origin_error_response = {
    "Message": "origin extract failure. Please contact the dev"
}
