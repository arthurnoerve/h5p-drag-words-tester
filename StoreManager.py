# Manages the store

import datetime
import os

class StoreManager:

    store_root = "./"


    def __init__(self,root):
        self.store_root = root

    def get_run(self, name):
        pass

class RunStore:
    # store_manager
    # id # can be anything we use the moment of init ie. the current datetime

    def __init__(self,store_man,name):
        self.store_manager = store_man
        self.id = datetime.datetime.now().isoformat()
        self.name = name

        os.makedirs( self.path )
    @property
    def path(self):
        return self.store_manager.store_root + self.name + "/" + self.id + "/"

    def  path_to(self,name):
        return self.path + name

    def log(self,text):
        fh = open(self.path_to("run.log"), 'a')
        fh.write(text+"\n")
