from flask.views import View
import abc
from flask import render_template
import requests


class BaseView(View):
    __metaclass__ =  abc.ABCMeta

    def dispatch_request(self, **args):
        """
        This is called when the view is called
        :param args: arbitrary number of arguments to pass data into the template
        """
        self.args = args
        return self.display_template()

    def context(self):
        """
        :return: Data to pass into the template, in the form of a dictionary
        """
        return {}

    def display_template(self):
        """
        :return: The final template
        """
        return render_template(self.template_location(), **self.context())

    @abc.abstractmethod
    def template_location(self):
        raise NotImplementedError()


class IndexView(BaseView):

    def template_location(self):
        return 'games/index.html'

    def context(self):
        self.game_state = requests.get("http://127.0.0.1/api/v1.0/")

