from configuration.config_class import getConfig

## Abstract class for classes that support config files operations and needs setUp and exec functions
class AbstractConfigClass:

    def __init__(self):
        self.config_parser=getConfig()


    def setup(self):
        raise NotImplementedError("Please Implement {} method".format(AbstractConfigClass.exec.__name__))


    def exec(self):
        raise NotImplementedError("Please Implement {} method".format(AbstractConfigClass.exec.__name__))
