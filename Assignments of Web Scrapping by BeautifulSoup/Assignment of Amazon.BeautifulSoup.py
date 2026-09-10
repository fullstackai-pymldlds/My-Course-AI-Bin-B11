#Python program to scrape Amazon website 
#and save Smart Home products from website
import requests
from bs4 import BeautifulSoup
import csv
 
URL = "https://www.amazon.com/gp/browse.html?node=6563140011&ref_=nav_em_amazon_smart_home_0_2_8_2"
r = requests.get(URL)
 
soup = BeautifulSoup(r.content, 'html5lib')
 
products=[]  # a list to store products
 
table = soup.find('div', attrs = {'class':'s-main-slot'}) 
 
for row in table.find_all('div',
                         attrs = {'data-component-type':'s-search-result'}):
    product = {}
    product['name'] = row.find('span', attrs = {'class':'a-size-base-plus'}).text
    product['url'] = 'https://www.amazon.com' + row.a['href']
    product['img'] = row.img['src']
    product['price'] = row.find('span', attrs = {'class':'a-price-whole'}).text
    product['rating'] = row.find('span', attrs = {'class':'a-icon-alt'}).text
    products.append(product)
 
filename = 'ASSIGNMENTS/amazon_smarthome_beautifulsoup.csv'
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f,['name','url','img','price','rating'])
    w.writeheader()
    for product in products:
        w.writerow(product)