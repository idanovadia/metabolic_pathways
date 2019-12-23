from code_tools.Abstract_config_class import AbstractConfigClass
from configparser import ConfigParser


class Example1(AbstractConfigClass):

    def __init__(self):
        AbstractConfigClass.__init__(self)


    def setup(self):
        self.example1_parameter1 = self.config_parser.eval(self.__class__.__name__,"parameter1")
        self.example1_parameter2 = self.config_parser.eval(self.__class__.__name__,"parameter2")



    def exec(self):
        #printing for the example
        members = [attr for attr in dir(self) if not callable(getattr(self, attr)) and not attr.startswith("__") and not attr.__eq__("config_parser")]
        for member in members:
            print("{}:{}".format(member,getattr(self, member)))
