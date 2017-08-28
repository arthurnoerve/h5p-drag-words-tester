
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

from PrahaTest import *

class DragWord(PrahaTest):
    name = "drag-word"

    def perform(self):
        self.driver.get("https://h5p.org/drag-the-words")

        assert "Drag" in self.driver.title

        self.driver.switch_to_frame("h5p-iframe-1399");
        blue   = self.driver.find_elements_by_xpath("//*[contains(text(), 'blue')]")[0]
        red    = self.driver.find_elements_by_xpath("//*[contains(text(), 'red')]")[0]
        orange = self.driver.find_elements_by_xpath("//*[contains(text(), 'orange')]")[0]

        drops = self.driver.find_elements_by_css_selector(".ui-droppable")

        blue_drop = drops[0]
        red_drop = drops[1]
        orange_drop = drops[2]


        blue_chain = ActionChains(self.driver)
        red_chain = ActionChains(self.driver)
        orange_chain = ActionChains(self.driver)

        self.screenshot()

        blue_chain.drag_and_drop(blue,blue_drop).perform()
        self.screenshot()

        red_chain.drag_and_drop(red,red_drop).perform()
        self.screenshot()

        orange_chain.drag_and_drop(orange,orange_drop).perform()
        self.screenshot()

        check_button = self.driver.find_element_by_class_name("h5p-question-check-answer")

        check_button.click()
        self.screenshot()

        self.completion()
