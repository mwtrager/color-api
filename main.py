import webscraper as ws
from selenium import webdriver
import time
import os

# NOTE not necessary?
print('setting up chrome options...')
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.binary_location = '/usr/local/bin/chromedriver'

print('making webdriver...')
driver = webdriver.Chrome()

print('getting page...')
driver.get('http://colorhunt.co')
print(driver.page_source)

driver.close()
