import requests
from bs4 import BeautifulSoup

URL = input("Enter the string to the amazon page you want to track:")

headers = {"USer-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"}


page = requests.get(URL,headers = headers)

soup = BeautifulSoup(page.content,'html.parser')

title = soup.find(id = "productTitle").get_text()
price = soup.find(id = "priceblock_ourprice").get_text()
priceLength = len(price)
realprice = price[1:priceLength]
realprice= int(realprice.replace(",", ""))



print(realprice)

