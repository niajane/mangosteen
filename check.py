import requests
import time
from bs4 import BeautifulSoup
import smtplib, ssl
import os, json
from email.mime.text import MIMEText
from dotenv import load_dotenv
from datetime import datetime


def sendemail():
    #load_dotenv()
    sender = os.environ['SENDER']
    receivers = os.environ['RECEIVERS']
    body = "<span style='color:purple'>Mangosteen</span> is in stock at <a href='"+os.environ['WEBSITE']+"'>Robinsons</a>!"
    msg = MIMEText(body, 'html')
    msg['Subject'] = 'Mangosteen alert!'
    msg['From'] = sender
    msg['To'] = receivers
    s = smtplib.SMTP_SSL(host = 'smtp.gmail.com', port = 465)
    s.login(user = os.environ['USERNAME'], password = os.environ['PASSWORD'])
    s.sendmail(sender, receivers.split(','), msg.as_string())
    s.quit()

load_dotenv()
r = requests.get(os.environ['WEBSITE'])
soup = BeautifulSoup(r.text, 'html.parser')
items = soup.find_all("a","grid-product__title")
for item in items:
    if 'mangosteen' in item.findAll(text=True)[1].lower():
        sendemail()
        break
print('successfully ran check.py on '+datetime.today().strftime('%Y-%m-%d'))