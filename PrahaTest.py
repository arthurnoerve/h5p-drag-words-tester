


# Superclass for tests 


from selenium import webdriver


from enum import Enum

def LogType(Enum):
    ERROR = 1
    COMMENT = 2
    INFO = 3


# TODO:
# + fetch store file path root from somewhere? env???
# + 

class PrahaTest:

    driver
    i = 0
    filenames = []

    def __init__(self):
        self.driver = webdriver.Firefox()
        
        # Create run folder in store, store manager class?
        # Create run description json file: description.json
        # Create run log file: run.log

        # Store now date, name of run, name of test, person running it, completion/error status,



    def completion(self):
        
        # Complete run description json file
        # Move stuff into folder with run hash or similar as name
        
        self.generate_gif()

        driver.quit()
    
    # Log given text to run log
    # unsure about kwarg syntax here.... NONFUNCTIONING!!!
    def log(self, text, type=LogType.INFO):
        pass
    


    # Saves a screenshot
    def screenshot(self):
        self.driver.save_screenshot(str(i)+".png") # Save screenshot from current context (page, iframe, ...)
        self.filenames.append(i) # Add to filename list
        i++ # Increment image index

    # Generates a gif
    def generate_gif(self):
        images = []
        for filename in self.filenames:
            images.append( imageio.imread(str(filename)+".png") )

        imageio.mimsave('run.gif', images,duration=0.5)








