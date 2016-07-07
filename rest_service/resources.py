import json
import random

from flask import Flask
from flask_restful import Resource, Api

from rest_service import app, api
from src import DRIVER

#Create REST Resources here
class Blond(Resource):
    def get(self):
        joke = DRIVER.trigger('Blond')
        return {"category" : "Blond", "joke"  : joke }

class Dark(Resource):
    def get(self):
        joke = DRIVER.trigger('Dark')
        return {"category" : "Dark", "joke"  : joke }

class Dirty(Resource):
    def get(self):
        joke = DRIVER.trigger('Dirty')
        return {"category" : "Dirty", "joke" : joke }

class Gross(Resource):
    def get(self):
        joke = DRIVER.trigger('Gross')
        return {"category" : "Gross", "joke"  : joke }

class Gender(Resource):
    def get(self):
        joke = DRIVER.trigger('Gender')
        return {"category" : "Men/Women", "joke"  : joke }

class WalksIntoABar(Resource):
    def get(self):
        joke = DRIVER.trigger('Walks into a bar')
        return {"category" : "Walks into a bar", "joke"  : joke }

class YoMama(Resource):
    def get(self):
        joke = DRIVER.trigger('Yo mama')
        return {"category" : "Yo mama", "joke"  : joke }

class Random(Resource):
    def get(self):
        joke = DRIVER.trigger('Random')
        return {"category" : "Random", "joke"  : joke }


# finally add these resources like so
api.add_resource(Blond, '/blond')
api.add_resource(Dark, '/dark')
api.add_resource(Dirty, '/dirty')
api.add_resource(Gross, '/gross')
api.add_resource(Gender, '/gender')
api.add_resource(WalksIntoABar, '/walks-into-a-bar')
api.add_resource(YoMama, '/yo-mama')
api.add_resource(Random, '/random')