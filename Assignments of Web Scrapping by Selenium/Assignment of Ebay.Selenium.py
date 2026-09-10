from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv

url = "https://www.ebay.com/b/Cell-Phones-Smartphones/9355/bn_320094"

cService = webdriver.ChromeService(executable_path='C:\\Users\\HP\\Downloads\\chromedriver-win64 (1)\\chromedriver-win64\\chromedriver.exe')
driver = webdriver.Chrome(service=cService)

driver.get(url)

productsList=[]
productsDiv = driver.find_elements(By.XPATH, "//li[contains(@class, 's-item')]")
for p in range(len(productsDiv) -1):
    product = {}
    innerImg = productsDiv[p+1].find_element(By.TAG_NAME, "img")
    innera = productsDiv[p+1].find_element(By.TAG_NAME, "a")
    innerName = productsDiv[p+1].find_element(By.XPATH, ".//div[contains(@class, 's-item__title')]")
    innerPrice = productsDiv[p+1].find_element(By.XPATH, ".//span[contains(@class, 's-item__price')]")
    product["name"] = innerName.text
    product["img"] = innerImg.get_attribute('src')
    product["url"] = innera.get_attribute('href')
    product['price'] = innerPrice.text
    productsList.append(product)

filename = 'ASSIGNMENTS/ebay_smartphones_selenium.csv'
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f,['name','url','img','price'])
    w.writeheader()
    for product in productsList:
        w.writerow(product)

driver.close()
