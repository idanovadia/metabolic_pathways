from classifier.code_tools.Abstract_config_class import AbstractConfigClass
import json
import shutil
import os
import glob

class Cleaner(AbstractConfigClass):

    def __init__(self):
        AbstractConfigClass.__init__(self)

    def setup(self):
        self.directories_to_delete=json.loads(self.config_parser.get(self.__class__.__name__, 'delete_directories'))
        self.print=self.config_parser.eval(self.__class__.__name__, 'print')

    def exec(self):
        self.delete_directories()


    def delete_directories(self):
        for name,path in self.directories_to_delete.items():
            try:
                self.delete_folder_contents(self.getPath(relative_path=path))
                if self.print:
                    print('\t'+"Deleting {} contents".format(path))
            except OSError:
                    print("was unable to delete contents of {}".format(path))

    def delete_folder_contents(self,path):
        r = glob.glob(path+os.sep+'*')
        for i in r:
            os.remove(i)