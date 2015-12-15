from flask import Blueprint, session
from flask_restful import Api, Resource, marshal_with, reqparse
import models
import abc
import api.controllers as controllers

controls = Blueprint('controls', __name__, url_prefix='/v1.0/controls')
api = Api(controls)