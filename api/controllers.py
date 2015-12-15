from flask import Blueprint, session
from flask_restful import Api, Resource, marshal_with, reqparse
import abc

class Base(Resource):
    """
    This gets a singular object from the model
    """

    def get(self, id):
        """
        :param id: the id of the object we are getting.
        :return: the object
        """
        if len(self.model_list) > id:
            return self.model_list[id]
        else:
            return {'message': 'Invalid ID'}

    @abc.abstractmethod
    def post(self,**to_post_items):
        """
        :param: to_post_tems: dictionary to be posted
        :return: The bitboard value that was posted.
        """
        pass

    @abc.abstractproperty
    def model_list(self):
        """
        :return: A list of model objects that this controller is manipulating.
        """
        return []

class BaseList(Resource):
    """
    :return:  A list of all objects from this model type stored by the system.
    """

    def get(self):
        """
        :return: all board states
        """
        if self.name():
            return { self.name() : self.model_list() }
        return self.model_list()

    def post(self, item=0x0):
        """
        :param: item: item to post
        :return: just added bitboard
        """
        self.model_list.append(item)
        return self.model_list[-1]

    @abc.abstractproperty
    def model_list(self):
        """
        :return: A list of model objects that this controller is manipulating.
        """
        return []

    @abc.abstractproperty
    def name(self):
        """
        :return: The name of the controller to be used in the return JSON
        """
        return False