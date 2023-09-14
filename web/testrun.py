from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import os, sys, json, time


json_name = sys.argv[1]
BROWSERSTACK_USERNAME = "rathilvasani"
BROWSERSTACK_ACCESS_KEY = "p3ce7vYbpXMiTldi29l4YPTFmULBTVPEeM1C8TLG6znigwzlPn"

with open(json_name, "r") as f:
    obj = json.loads(f.read())

instance_caps= obj[int(sys.argv[2])]
print ("Test "+sys.argv[2]+" started")

#------------------------------------------------------#
# Mention any other capabilities required in the test

#------------------------------------------------------#

caps = dict(instance_caps.items())
# caps = Merge(dict(caps.items()),dict(instance_caps.items()))

#------------------------------------------------------#
# THE TEST TO BE RUN PARALLELY GOES HERE

driver1 = webdriver.Remote(command_executor='https://%s:%s@hub.lambdatest.com/wd/hub' % (BROWSERSTACK_USERNAME, BROWSERSTACK_ACCESS_KEY),desired_capabilities=caps)


driver1.get('https://www.amazon.in')
driver1.maximize_window()


# get the input elements
input_search = driver1.find_element_by_xpath("//*[@id='twotabsearchtextbox']")
time.sleep(3)  
search_button = driver1.find_element_by_xpath("//*[@id='nav-search-submit-button']")
# input_search = browser.find_element_by_id("//*[@id='twotabsearchtextbox']")
# search_button = browser.find_element_by_xpath("(//input[@type='submit'])[1]")


# send the input to the webpage
input_search.send_keys("iphone 13")
time.sleep(1)
search_button.click()


products = []

prices = []

product = driver1.find_elements_by_xpath("//span[@class='a-size-medium a-color-base a-text-normal']")
price = driver1.find_elements_by_xpath("//span[@class='a-price-whole']")   #a-offscreen

#     print (product)
for p in product:
    products.append(p.text)
    print(p.text)        
        
for q in price:        
    prices.append(q.text)   
    print(q.text)    


"""
    Quit selenium driver1
"""
driver1.quit()
