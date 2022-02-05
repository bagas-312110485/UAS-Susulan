from cgitb import text
import requests
page = requests.get('https://www.worldometers.info/coronavirus/country/indonesia/')
from bs4 import BeautifulSoup

after_bs = BeautifulSoup(page.content, 'html.parser')

find_data = after_bs.find_all(id="maincounter-wrap")

for x in find_data:
    print(x.text)
