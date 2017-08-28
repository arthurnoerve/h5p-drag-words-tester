
#from PrahaTest import *
from StoreManager import *


import imp
import os

PluginFolder = "./tests"


def getPlugins():
    plugins = []
    possibleplugins = os.listdir(PluginFolder)
    for i in possibleplugins:
        filename, file_extension = os.path.splitext(i)

        location = os.path.join(PluginFolder, i)

        info = imp.find_module(filename, [location])

        plugins.append({"name": i, "info": info})
    return plugins

def loadPlugin(plugin):
    return imp.load_module(MainModule, *plugin["info"])

tests = getPlugins()

print(tests)


#test = Test.DragWord()
#test.perform()
