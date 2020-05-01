from classifier.configuration.config_class import config_class
import os
## Abstract class for classes that support config files operations and needs setUp and exec functions
class AbstractConfigClass:

    def __init__(self):
        self.config_parser=config_class.getConfig()
        self.path = os.path.dirname(__file__).split('classifier')[0]

    def setup(self):
        raise NotImplementedError("Please Implement {} method".format(AbstractConfigClass.exec.__name__))


    def exec(self):
        raise NotImplementedError("Please Implement {} method".format(AbstractConfigClass.exec.__name__))

    def getPath(self, relative_path):
        return os.path.join(self.path,relative_path)