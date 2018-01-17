from requests import get
from time import sleep
import re
from bs4 import BeautifulSoup

# soupify me captain!
def soupify(webpage):
    r = get(webpage)
    html = r.text
    soup =  BeautifulSoup(html, 'html.parser')
    return soup

def find_colors(soup):
    # taking in a soup... get some colors!
    return 0
