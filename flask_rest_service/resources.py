import json
from flask import Flask
from flask_restful import Resource, Api
from flask_rest_service import app, api

class Root(Resource):
    def get(self):
        return {
            'status': 'OK',
            'hello': 'world'
        }

class Blond(Resource):
    def get(self):
        return {
            'status': 'OK',
            'blond': 'dumb'
        }

''' Add REST Resources here '''

# finally add these resources like so

api.add_resource(Root, '/')
api.add_resource(Blond, '/blond')