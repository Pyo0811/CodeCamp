from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('https://gabrielecirulli.github.io/2048/')
link_elem = browser.find_element_by_link_text('New Game')
link_elem.click()
html_elem = browser.find_element_by_tag_name('html')
for i in range(20) :
    html_elem.send_keys(Keys.UP)
    html_elem.send_keys(Keys.DOWN)
