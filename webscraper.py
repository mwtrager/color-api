from requests import get
from time import sleep
import re
from bs4 import BeautifulSoup

# soupify me captain!
def soupify(html):
    # r = get(webpage)
    # html = r.text
    soup =  BeautifulSoup(html, 'html.parser')
    return soup

# list of lists (each inner list is a palette)
def get_palettes(soup):
    palettes = []
    palette_divs = soup('div', 'palette')
    for div in palette_divs:
        palette = []
        for span in div('span'):
            palette.append(span.get_text())
        palettes.append(palette)
    return palettes
