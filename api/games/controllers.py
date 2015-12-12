from flask import Blueprint, session
from flask_restful import Api, Resource, marshal_with, reqparse
import models

games = Blueprint('games', __name__, url_prefix='/v1.0')
api = Api(games)

parser = reqparse.RequestParser()
parser.add_argument('bitboard')
parser.add_argument('board_id')


class Game(Resource):

    pass