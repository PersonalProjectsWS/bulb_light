from yeelight import Bulb
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import os
import time
import subprocess

BULB_IP = '192.168.1.134'
BULB_IP_2 = '192.168.1.119'
BULB = Bulb(BULB_IP)
BULB_2 = Bulb(BULB_IP_2)

BITCOIN = 'https://es.tradingview.com/symbols/BTCUSD/'
PALANTIR = 'https://es.tradingview.com/symbols/NYSE-PLTR/'

ALERT_DOWN = 'yoursuffer.mp3'


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(BITCOIN)

def getCurrentPrice():
     soup = BeautifulSoup(driver.page_source,"lxml")
     currentPrice = soup.find("div", class_="tv-symbol-price-quote__value js-symbol-last").getText()
     return float(currentPrice)

def update():
    price = float(0)
    while True:
        if(getCurrentPrice() >= price):
            BULB.set_rgb(56, 218, 73)
            BULB_2.set_rgb(56, 218, 73)
        else: 
            BULB.set_rgb(217, 54, 22)
            BULB_2.set_rgb(217, 54, 22)
            subprocess.call(['afplay', ALERT_DOWN])
        price = getCurrentPrice()
        print(price)
        time.sleep(6)

BULB.turn_on()
BULB_2.turn_on()
update()

#driver.quit()