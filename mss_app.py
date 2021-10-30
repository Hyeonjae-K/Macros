from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pyautogui as pag
import numpy as np
from mss import mss
import time

first_like = [1400, 300]
purchase1 = {'left': 1400, 'top': 980, 'width': 1880, 'height': 1030}
choose_option = {'left': 1330, 'top': 815, 'width': 1875, 'height': 880}
purchase1_btn = [1700, 1000]
purchase2 = {'left': 1325, 'top': 975, 'width': 1510, 'height': 1030}
purchase3 = {'left': 1640, 'top': 975, 'width': 1880, 'height': 1030}
agree_all1 = {'left': 1335, 'top': 810, 'width': 1465, 'height': 835}
agree_all2 = {'left': 1780, 'top': 310, 'width': 1865, 'height': 330}
cash_bill_option = {'left': 1340, 'top': 560, 'width': 1865, 'height': 605}
cash_bill_none = [1500, 480]
next_btn = [1350, 980]
purchase_time = ['10시', '00분', '00초']

options = Options()
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
options.add_argument('headless')
options.add_argument('user-agent=%s' % user_agent)
driver = webdriver.Chrome()
driver.get('https://time.navyism.com/?host=store.musinsa.com')


def checkTime():
    while True:
        server_time = driver.find_element_by_css_selector(
            '#time_area').text.split()[3:]
        if server_time == purchase_time:
            break


def getColor(location):
    img = np.array(mss().grab(location))[:, :, :3]
    return np.mean(img)


def click(location):
    if type(location) == type(dict()):
        x = (location['left'] + location['width']) // 2
        y = (location['top'] + location['height']) // 2
    else:
        x = location[0]
        y = location[1]
    pag.moveTo(x=x, y=y, duration=0.0)
    pag.mouseDown()
    pag.mouseUp()


def checkLocation():
    while True:
        x, y = pag.position()
        print('X:', x, 'Y:', y)
        time.sleep(1)


def checkColor(location):
    color = 0
    while True:
        temp = getColor(location)
        if temp != color:
            color = temp
            print(color)


checkTime()
click(first_like)

while True:
    if 3 < getColor(purchase1) < 3.5:
        click(purchase1)
        break

while True:
    if 29.5 < getColor(choose_option) < 30:
        click(choose_option)
        break
pag.scroll(-150)
time.sleep(0.1)
click(choose_option)
click(purchase1_btn)

while True:
    if 4.5 < getColor(purchase2) < 5:
        click(purchase2)
        break

while True:
    if 33 < getColor(agree_all1) < 33.5:
        click(agree_all1)
        break
click(purchase2)

while True:
    if 142 < getColor(agree_all2) < 142.5:
        click(agree_all2)
        break

while True:
    if 142 < getColor(agree_all2) < 142.5:
        click(agree_all2)
        break

while True:
    if 118 < getColor(cash_bill_option) < 119:
        click(cash_bill_option)
        break
click(cash_bill_none)
click(next_btn)

driver.close()
