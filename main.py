import webscraper as ws
from selenium import webdriver
import time
import os

print('making webdriver...')
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=chrome_options)

print('getting page...')
driver.get('http://colorhunt.co')
before_source = driver.page_source

print('try scrolling...')
driver.execute_script('window.scrollTo(0,document.querySelector("#container").scrollHeight)')
time.sleep(3) # NOTE without this sleep, the source doesn't get updated quick enough
after_source = driver.page_source

print('get the 1 palettes...')
soup = ws.soupify(after_source)
palettes = ws.get_palettes(soup)
print(len(palettes[:-1]))
for palette in palettes[:-1]:
    print(palette)

print('get the 2 palettes...')
driver.execute_script('window.scrollTo(0,document.querySelector("#container").scrollHeight)')
time.sleep(3) # NOTE without this sleep, the source doesn't get updated quick enough
soup = ws.soupify(driver.page_source)
palettes = ws.get_palettes(soup)
print(len(palettes[:-1]))
for palette in palettes[:-1]:
    print(palette)

print('get the 3 palettes...')
driver.execute_script('window.scrollTo(0,document.querySelector("#container").scrollHeight)')
time.sleep(3) # NOTE without this sleep, the source doesn't get updated quick enough
soup = ws.soupify(driver.page_source)
palettes = ws.get_palettes(soup)
print(len(palettes[:-1]))
for palette in palettes[:-1]:
    print(palette)

print('get the 4 palettes...')
driver.execute_script('window.scrollTo(0,document.querySelector("#container").scrollHeight)')
time.sleep(3) # NOTE without this sleep, the source doesn't get updated quick enough
soup = ws.soupify(driver.page_source)
palettes = ws.get_palettes(soup)
print(len(palettes[:-1]))
for palette in palettes[:-1]:
    print(palette)

print('get the 5 palettes...')
driver.execute_script('window.scrollTo(0,document.querySelector("#container").scrollHeight)')
time.sleep(3) # NOTE without this sleep, the source doesn't get updated quick enough
soup = ws.soupify(driver.page_source)
palettes = ws.get_palettes(soup)
print(len(palettes[:-1]))
for palette in palettes[:-1]:
    print(palette)




driver.close()
