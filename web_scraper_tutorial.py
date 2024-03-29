# -*- coding: utf-8 -*-
"""Web_Scraper_Tutorial.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15HaUNF_gc7lAGro9XSK9LB_UUN_BbIvT
"""

import requests
import pandas as pd
# These libraries are essentially borrowed code with classes and methods you can use.
# When you do "requests." or "pd." you're creating an object and when you're using .text
# or .read_html you're calling a method of that object's class

# send an HTTP GET request to the Wikipedia page
url = 'https://en.wikipedia.org/wiki/List_of_NHL_scoring_leaders_by_season'
response = requests.get(url)
print(response.status_code)
# 200 means the request was successful and the server is returning the requested data

print(type(response), type(response.text)) #class object converted to string

print(response.text)

tables = pd.read_html(response.text) # or .context
# .text would be preferred for textual responses, such as an HTML or XML document,
# and .content would be preferred for "binary" filetypes, such as an image or PDF file
# The method read_html takes in a string of HTML code and parses it into tables.
# This is a list of pandas dataframes
print('tables:',type(tables), '\ntables[0]:', type(tables[0]))

print('How many tables:', len(tables))

print(tables)

tables[0].to_csv('hockeytable.csv', index = False, sep = ',', encoding='utf-8')
# Microsoft Excel is unable to properly display UTF-8 compliant CSV files when they contain non-English characters
# Reads fine in R when you do read_csv('hockeytable.csv')

import requests
import pandas as pd

# send an HTTP GET request to the Wikipedia page
url = 'https://en.wikipedia.org/wiki/Season_structure_of_the_NHL'
response = requests.get(url)
print(response.status_code)

print(response.text)

tables = pd.read_html(response.text) # or .context
# .text would be preferred for textual responses, such as an HTML or XML document,
# and .content would be preferred for "binary" filetypes, such as an image or PDF file
# This is a list of pandas dataframes
print('tables:',type(tables), '\ntables[0]:', type(tables[0]))

print('How many tables:', len(tables))

print(tables)

# Print the tables to console
for i, table in enumerate(tables):
    print(f"Table {i}:")
    print(table)

# If the output is too large for the console, you can write the output to txt.
with open("output.txt", "w", encoding='utf-8') as file:
    for i, table in enumerate(tables):
        file.write(f"\nTable {i}:\n")
        file.write(str(table))

# Pick the table index you are interested in. We are interested in index 0 and 1.
print(tables[0])
print(tables[1])

# Export the pandas dataframe to csv.
tables[0].to_csv('hockeydivisions.csv', index = False, sep = ',', encoding='utf-8')
tables[1].to_csv('hockeytable.csv', index = False, sep = ',', encoding='utf-8')
# Make sure this file isn't open when you rerun the code

import requests
from bs4 import BeautifulSoup

url = "https://www.pointzero.ca/collections/fw22-sweaters-chandails"

# This creates a requests object with the HTML info
response = requests.get(url)
print(type(response))

# This creates a Beautiful Soup object that can parse the HTML
soup = BeautifulSoup(response.text, 'html.parser')
print(type(soup))

print(soup)

print(response.text)

# But now we have a beautiful soup object that can parse the HTML

# The method ".find_all" is used on the soup object which finds all 
# the <span class='price-item price-item--regular'> THIS IS TEXT <span>

#  the method ".find" finds the first one and it isn't in a list
list = soup.find_all('span', {'class': 'price-item price-item--regular'})
print(list)

print(list[0])

print(list[0].text)

print(list[0].text.strip())

print(list[0].text.strip().lstrip('$'))

prices = []
for price_item in soup.find_all('span', {'class': 'price-item price-item--regular'}):
    price = price_item.text.strip().lstrip('$')
    prices.append(price)
print(prices)

# Get the first element
element = soup.find('product-card', {'product-handle': 'joseph-soft-mock-micro-polar-fleece'})
print(element)

# Search for elements h2 that have 'p product-card__title' as their class
elements = soup.find_all('h2', {'class': 'p product-card__title'})
print(elements[0])

# You can use the method .<element> to get the html inside that element.
print(elements[0].a)

# You can use the .text method to only get the text inside the element, removing the <> tags
print(elements[0].a.text)

print(elements[0].a.text.strip())

# now you can loop through all the elements in the list and get all the titles
titles = []
for card in elements:
    titles.append(card.a.text.strip())
    print(card.a.text.strip())
# You can either store the data in a list of titles or just print it like this

print(soup.find_all('img'))

# Find all the img elements"
img_elements = soup.find_all('img')

# Extract the src attribute of each img element to get the image URL
image_urls = []
for img_element in img_elements:
    image_url = img_element['src']
    image_urls.append(image_url)

# Print the image URLs
print(image_urls)

# Let's see if we can use our tools on this website. This is the website I was 
# tasked to scrape for my Major Analytics Project

import requests

url = "https://www.levantineceramics.org/petrographics"

response = requests.get(url)
print(response.text)

with open(f'levantine.txt', mode='w', encoding='utf-8') as file:
    file.write(response.text)

# This doesn't look like we are getting any of the table info from this url

import pandas as pd
import requests

url = 'https://www.levantineceramics.org/petrographics.json'

params = {
    "sEcho": "2",
    "iColumns": "12",
    "sColumns": ",,,,,,,,,,,",
    "iDisplayStart": "0",
    "iDisplayLength": "100",
}
data = requests.get(url, params).json()
type(data)

print(data)

dataframe = pd.DataFrame.from_records(data)
print(dataframe)

print(dataframe['aaData'][2])

def strip_quotes(s):
    return s.rstrip('"')

frames = []
for i in range(1):
    params['iDisplayStart'] = str(i*100)
    data = requests.get(url, params).json()
    dataframe = pd.DataFrame.from_records(data)
    dataframe_with_ids = dataframe["aaData"].str.get(0).str[40:44].apply(strip_quotes).str.strip('-')
    frames.append(dataframe_with_ids)
petrographic_ids = pd.concat(frames)
print(petrographic_ids)

import requests
import json
import pandas as pd
from bs4 import BeautifulSoup

# Make a GET request to the webpage
url = "https://www.levantineceramics.org/map?petrographic_id=5040-017"
response = requests.get(url)

# Parse the HTML using Beautiful Soup
soup = BeautifulSoup(response.content, "html.parser")

# Find the <div> element containing the latitude and longitude information
map_div = soup.find("div", {"id": "map"})

default_markers = map_div.get("data-default-markers")

# Extract the latitude and longitude from the "data-default-markers" attribute
default_markers = json.loads(default_markers.replace('&quot;', '"'))
marker_id = next(iter(default_markers[0]))
marker = default_markers[0][marker_id]

lat, lng = marker['coordinate']
print(lat, lng)

print(marker)

# This script will allow you to download any photo from a URL to your working directory
import pandas as pd
import requests

# You could have a csv with photo urls and you can use pd.read_csv to load them in.
# Or just put them in a list
urls = ['https://media-cldnry.s-nbcnews.com/image/upload/t_fit-1240w,f_auto,q_auto:best/rockcms/2022-08/220805-domestic-cat-mjf-1540-382ba2.jpg',
           'https://www.alleycat.org/wp-content/uploads/2019/03/FELV-cat.jpg']

def download_image(url, path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(path, 'wb') as f:
            f.write(response.content)

for url in urls:
    filename = url.split("/")[-1]
    download_image(url, filename)

# Let's try putting in the list of Image URLs from the pointzero website which we stored earlier into 
# a variable named image_urls

# The urls need https: added to the start of the string and the filename needs the jpg extension
import pandas as pd
import requests

def download_image(url, path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(path, 'wb') as f:
            f.write(response.content)

for url in image_urls:
    url = 'https:' + url
    filename = url[-6:-1] + '.jpg'
    download_image(url, filename)

