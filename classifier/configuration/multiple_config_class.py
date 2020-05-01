from configparser import ConfigParser
import sys




def getConfig(config_path):
    try:
        config = ConfigParser()
        config_file = config_path
        config.read(config_file)
        config.eval = lambda sec, key: eval(config.get(sec, key))
        config.getfilename = lambda: config_file
        return config
    except:
        raise ValueError("Usage: %s <path to config .ini file>".format((sys.argv[0])))
