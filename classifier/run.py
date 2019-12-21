from configuration.config_class import getConfig
from config_class_example.example_config_class import Example1
from config_class_example.example2_config_class import Example2

modules_dict={}
modules_dict['Example1']=Example1
modules_dict['Example2']=Example2


pipeline=[]

for module in getConfig().sections():
    if modules_dict.get(module):
        pipeline.append(modules_dict.get(module)())

for element in pipeline:
    print("Initializing {}".format(element.__class__.__name__))
    element.setup()

print("\n")

for element in pipeline:
    print("Executing {}".format(element.__class__.__name__))
    element.exec()
    print("\n")

if __name__ == '__main__':
    pass