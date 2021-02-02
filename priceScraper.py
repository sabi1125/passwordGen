import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = input("Enter the link to the amazon page you want to track:")
youremail = input("Enter your email address where we can contact you: " )

headers = {"USer-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"}






def check_price():
    page = requests.get(URL,headers = headers)

    soup = BeautifulSoup(page.content,'html.parser')

    title = soup.find(id = "productTitle").get_text()
    price = soup.find(id = "priceblock_ourprice").get_text()
    priceLength = len(price)


    print("The product name: " + title.strip())
    print("Current Price: " + price)

    realprice = price[1:priceLength]

    realprice= int(realprice.replace(",", ""))

    wantedPrice = input("Enter the price that you want and we will notify you when the product goes down to that amount: ")

    if(realprice < int(wantedPrice)):
        send_mail()






def send_mail():
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login("sabirscrapetest@gmail.com","sabirbarahi99")

    subject = "Wanted price"
    body = "check " + URL
    
    msg = f"Subject: {subject}\n\n{body}"


    server.sendmail(
        "make an email for yourself",
        youremail,
        msg
    )

    print("The messsage has been sent!")
    server.quit() 




while(True):
    check_price()
    time.sleep(60*60*24)