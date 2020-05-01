from configparser import ConfigParser
import sys


class config_class:
   __instance = None
   @staticmethod
   def getConfig():
      """ Static access method. """
      if config_class.__instance == None:
         config_class()
      return config_class.__instance
   def __init__(self,file):
      """ Virtually private constructor. """
      try:
          config = ConfigParser()
          config_file = file
          config.read(config_file)
          config.eval = lambda sec, key: eval(config.get(sec, key))
          config.getfilename = lambda: config_file
          __instance = config
          config_class.__instance = config
      except:
        raise ValueError("Usage: %s <path to config .ini file>".format((sys.argv[0])))













