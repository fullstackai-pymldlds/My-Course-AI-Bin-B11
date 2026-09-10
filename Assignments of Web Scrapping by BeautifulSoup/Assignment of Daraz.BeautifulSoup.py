#Python program to scrape Daraz website 
#and save Smart Phone products from website
import requests
from bs4 import BeautifulSoup
import csv
 
URL = "https://www.daraz.pk/catalog/?spm=a2a0e.tm80331704.cate_5.5.77cc5aa7fPImi7&q=Smart%20Phones&from=hp_categories&src=all_channel"
r = requests.get(URL)
 
soup = BeautifulSoup(r.content, 'html5lib')
 
products=[]  # a list to store products
 
table = soup.find('div', attrs = {'class':'products-list'}) 
 
for row in table.find_all('div',
                         attrs = {'class':'product-card'}):
    product = {}
    product['name'] = row.a.text
    product['url'] = row.a['href']
    product['img'] = row.img['src']
    product['price'] = row.find('span', attrs = {'class':'currency--GVKjl'}).text
    product['rating'] = row.find('span', attrs = {'class':'ratig-num--KNake'}).text
    products.append(product)
 
filename = 'ASSIGNMENTS/daraz_smartphones_beautifulsoup.csv'
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f,['name','url','img','price','rating'])
    w.writeheader()
    for product in products:
        w.writerow(product)