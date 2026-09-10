#Python program to scrape eBay website 
#and save Smart Phone products from website
import requests
from bs4 import BeautifulSoup
import csv
 
URL = "https://www.ebay.com/b/Cell-Phones-Smartphones/9355/bn_320094"
r = requests.get(URL)
 
soup = BeautifulSoup(r.content, 'html5lib')
 
products=[]  # a list to store products
 
table = soup.find('ul', attrs = {'class':'b-list__items_nofooter'}) 
 
for row in table.find_all('li',
                         attrs = {'class':'s-item'}):
    product = {}
    product['name'] = row.find('div', attrs = {'class':'s-item__title'}).text
    product['url'] = row.a['href']
    product['img'] = row.img['src']
    product['price'] = row.find('span', attrs = {'class':'s-item__price'}).text
    product['condition'] = row.find('span', attrs = {'class':'SECONDARY_INFO'}).text
    products.append(product)
 
filename = 'ASSIGNMENTS/ebay_smartphones_beautifulsoup.csv'
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f,['name','url','img','price','condition'])
    w.writeheader()
    for product in products:
        w.writerow(product)