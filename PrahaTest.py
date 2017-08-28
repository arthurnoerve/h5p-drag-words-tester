# Superclass for tests

from selenium import webdriver
import imageio
from enum import Enum
from StoreManager import *


def LogType(Enum):
    ERROR = 1
    COMMENT = 2
    INFO = 3


# TODO:
# + fetch store file path root from somewhere? env???
# +

class PrahaTest:
    i = 0
    filenames = []
    name = "default"

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.store = StoreManager("store/") #fetch from env
        self.run = RunStore(self.store, self.name)

        self.log("Setup complete")

        # Create run description json file: description.json
        # Store now date, name of run, name of test, person running it, completion/error status,



    def completion(self):
        self.generate_gif()
        self.driver.quit()
        self.log("Test finished")


    # Log given text to run log
    # unsure about kwarg syntax here.... NONFUNCTIONING!!!
    #def log(self, text, type=LogType.INFO):
    def log(self, text):
        self.run.log("INFO: "+text)



    # Saves a screenshot
    def screenshot(self):
        filename = str(self.i)+".png"
        self.driver.save_screenshot(self.run.path_to(filename)) # Save screenshot from current context (page, iframe, ...)
        self.filenames.append(filename) # Add to filename list

        self.log("Took screenshot: "+ filename)

        self.i += 1 # Increment image index

	# Generates a gif
    def generate_gif(self):
        images = []
        for filename in self.filenames:
            images.append( imageio.imread(self.run.path_to(filename)) )

        imageio.mimsave(self.run.path_to('run.gif'), images,duration=0.5)

        self.log("Created run gif: run.gif")
