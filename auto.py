
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains


driver = webdriver.Firefox()


driver.get("https://h5p.org/drag-the-words")


assert "Drag" in driver.title



driver.switch_to_frame("h5p-iframe-1399");


blue   = driver.find_elements_by_xpath("//*[contains(text(), 'blue')]")[0]
red    = driver.find_elements_by_xpath("//*[contains(text(), 'red')]")[0]
orange = driver.find_elements_by_xpath("//*[contains(text(), 'orange')]")[0]

#assert blue.isDisplayed()
#assert red.isDisplayed()
#assert orange.isDisplayed()


drops = driver.find_elements_by_css_selector(".ui-droppable")

blue_drop = drops[0]
red_drop = drops[1]
orange_drop = drops[2]


blue_chain = ActionChains(driver)
red_chain = ActionChains(driver)
orange_chain = ActionChains(driver)

blue_chain.drag_and_drop(blue,blue_drop).perform()
red_chain.drag_and_drop(red,red_drop).perform()
orange_chain.drag_and_drop(orange,orange_drop).perform()



check_button = driver.find_element_by_class_name("h5p-question-check-answer")

check_button.click()


#driver.close()




