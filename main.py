import webscraper as ws
from selenium import webdriver
import time

print('making webdriver...')
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=chrome_options)

print('getting page...')
driver.get('http://colorhunt.co/popular')
before_source = driver.page_source

print('try scrolling...')
driver.execute_script('window.scrollTo(0,document.querySelector("#container").scrollHeight)')
time.sleep(3) # NOTE without this sleep, the source doesn't get updated quick enough
after_source = driver.page_source

target = 2000
count = 0
iteration = 0
while count < target:
    driver.execute_script('window.scrollTo(0,document.querySelector("#container").scrollHeight)')
    # NOTE when I'm doing the search for palettes with selenium, i should be able to leverage:
    # http://www.seleniumhq.org/docs/04_webdriver_advanced.jsp#explicit-and-implicit-waits
    # to avoid doing this lame time.sleep()
    time.sleep(3) # NOTE without this sleep, the source doesn't get updated quick enough
    soup = ws.soupify(driver.page_source)
    palettes = ws.get_palettes(soup) # TODO rewrite with selenium
    # kinda wanna do like "if we see one, add to count"
    # that way i dont actually save it until i hit the source the bs4
    count = len(palettes[:-1])
    print('current count is:', len(palettes[:-1]), 'on iteration', iteration)
    iteration = iteration + 1


print('count is', count)
print('grabbing all of them...')
soup = ws.soupify(driver.page_source)
driver.close() # NOTE done with driver now, close it
palettes = ws.get_palettes(soup)

print('writing into palettes.csv...')
with open("palettes.csv", "w") as file:
    for palette in palettes[:-1]:
        for color in reversed(palette): # NOTE the colors in the palette come in reversed so change it back
            if color == palette[0]:
                file.write('"%s"' % color)
            else:
                file.write('"%s",' % color)
        file.write('\n')
