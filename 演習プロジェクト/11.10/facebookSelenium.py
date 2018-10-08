from selenium import webdriver
import time

browser = webdriver.Firefox()
browser.get('https://www.facebook.com/')
email_elem = browser.find_element_by_id('email')
email_elem.send_keys(input('emailを入力してください : '))
pass_elem = browser.find_element_by_id('pass')
pass_elem.send_keys(input('PassWordを入力してください : '))
pass_elem.submit()
time.sleep(3)
text_elem = browser.find_element_by_css_selector('._1mf._1mj')
print(text_elem)
