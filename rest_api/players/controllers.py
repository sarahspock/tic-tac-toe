from flask import Blueprint, session
from flask_restful import Api, Resource, marshal_with, reqparse
import abc
import rest_api.controllers as controllers

players = Blueprint('players', __name__, url_prefix='/v1.0/players')
api = Api(players)