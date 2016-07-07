import json
from flask import Flask
from flask_restful import Resource, Api
from flask_rest_service import app, api

from websites import jokesdotcc

class Blond(Resource):
    def get(self):
        joke = jokesdotcc.getJoke('blonde')
        return { "joke"  : joke }
#Create REST Resources here



# finally add these resources like so
api.add_resource(Blond, '/blond')