import os
from flask import Flask, make_response
from flask_restful import Resource, Api
import json

app = Flask(__name__)
api = Api(app)

@api.representation('application/json')
def output_json(data, code, headers=None):
    resp = make_response(json.dumps(data, indent=4), code)
    resp.headers.extend(headers or {})
    return resp

import rest_service.resources