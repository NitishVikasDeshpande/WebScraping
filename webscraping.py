from selenium import webdriver
browser=webdriver.Firefox()
import time
from selenium.webdriver.common.keys import Keys
actionChains = ActionChains(browser)
browser.get('https://esc101.cse.iitk.ac.in')
l=browser.find_element_by_name('username')
l.send_keys('type_your_username')
m=browser.find_element_by_name('password')
m.send_keys('type_your_password')
n=browser.find_element_by_id('btn-submit')
n.click()
x=browser.find_element_by_partial_link_text('Scratchpad')
x.click()
time.sleep(5)
y=browser.find_element_by_partial_link_text('1.c')# type the name of ur first file
actionChains.context_click(y).perform()
z=browser.find_element_by_partial_link_text('Open')
z.click()
a=browser.find_element_by_partial_link_text('File')
a.click()
b=browser.find_element_by_partial_link_text('Download')
b.click()
import time

from selenium.webdriver.common.keys import Keys 
actionChains = ActionChains(browser)
for x in range(1,8):# here instead of 8 type the total no of files saved in your scratchpad
    s='j1_'+'%d'%(x)
    
    j=browser.find_element_by_id(s)
    actionChains.context_click(j).perform()
    z=browser.find_element_by_partial_link_text('Open')
    z.click()
    a=browser.find_element_by_partial_link_text('File')
    a.click()
    b=browser.find_element_by_partial_link_text('Download')
    b.click()
    time.sleep(5)
