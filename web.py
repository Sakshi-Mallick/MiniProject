import requests
from bs4 import BeautifulSoup
import smtplib

# here we have to put the url of product
URL = 'https://www.amazon.in/Apple-MacBook-Pro-8th-Generation-Intel-Core-i5/dp/B0883KXHG3/ref=sr_1_1_sspa?d' \
      'child=1&keywords=macbook&qid=1604493584&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyNE5SUk1MS' \
      '0JCR1RCJmVuY3J5cHRlZElkPUEwMDg3ODY0MlI4N1ZUMVdGQzE2UiZlbmNyeXB0ZWRBZElkPUEwNTQ5NDMzMkN' \
      'RSzVRM0ZMU09FNyZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='

# The user agent of every browser is different and should be changed
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}


# function to compare current price and previous rice
def check_price():
    page = requests.get(URL,headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id='productTitle').get_text()
    price = soup.find(id='priceblock_ourprice').get_text()
    convert = ''
    for i in price:
        if ord(i) in range(48,58):
            convert = convert+i
        elif i == '.':
            break
    converted_price = float(convert)
    if converted_price < 110000:
        send_mail()
    print(converted_price)
    print(title.strip())

    if converted_price < 110000:
        send_mail()

# to send mail every time price satisfy
def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('Email_Id','Password') #Email id and passsword should be changed with existing one


    subject = 'Price fell down'
    body = 'Check the amazon link https://www.amazon.in/Apple-MacBook-Pro-8th-Generation-Intel-Core-i5/dp/B0883KXHG3/ref=sr_1_1_sspa?d' \
      'child=1&keywords=macbook&qid=1604493584&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyNE5SUk1MS' \
      '0JCR1RCJmVuY3J5cHRlZElkPUEwMDg3ODY0MlI4N1ZUMVdGQzE2UiZlbmNyeXB0ZWRBZElkPUEwNTQ5NDMzMkN' \
      'RSzVRM0ZMU09FNyZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='

    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(
        'Senders email',     # Sender's email id should be entered
        'Receiver email',   # Receiver's email id should be entered
        msg
    )

    print("Email has sent")

    server.quit()

check_price()