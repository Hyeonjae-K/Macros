from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
import pyautogui as pag
from mss import mss
import numpy as np

purchase_time = ['00시', '00분', '00초']
item_btn = (2700, 400)
buy_area = {'left': 2700, 'top': 985, 'width': 3100, 'height': 1020}
buy_btn = (3000, 1000)
agree1_btn = (2610, 840)
agree2_area = {'left': 3040, 'top': 310, 'width': 3060, 'height': 3030}
agree2_btn = (3050, 320)
bill_opt_area = {'left': 2600, 'top': 560, 'width': 3120, 'height': 600}
bill_opt_btn = (2800, 580)
bill_non_btn = (2800, 480)
user_agent = 'User-Agent'
DEBUG = False


def checkTime():
    chrome_options = Options()
    chrome_options.add_argument('headless')
    chrome_options.add_argument('user-agent=%s' % user_agent)
    time_driver = webdriver.Chrome(chrome_options=chrome_options)
    alarm_box = '#navyismMainContainer > div:nth-child(15) > div:nth-child(1) > div:nth-child(1) > label:nth-child(2)'
    time_area = '#time_area'

    time_driver.get('https://time.navyism.com/?host=store.musinsa.com')
    time_driver.find_element(By.CSS_SELECTOR, alarm_box).click()
    while True:
        server_time = time_driver.find_element(
            By.CSS_SELECTOR, time_area).text.split()[3:]
        if purchase_time == server_time:
            return


def purchase():
    pag.moveTo(buy_btn)
    while True:
        if 1.4 < np.mean(np.array(mss().grab(buy_area))[:, :, :3]) < 1.5:
            pag.click(clicks=2)
            break

    while True:
        if 1.6 < np.mean(np.array(mss().grab(buy_area))[:, :, :3]) < 1.7:
            pag.click()
            pag.moveTo(agree1_btn)
            pag.click()
            pag.moveTo(buy_btn)
            pag.click()
            break

    pag.moveTo(agree2_btn)
    while True:
        if 2.1 < np.mean(np.array(mss().grab(agree2_area))[:, :, :3]) < 2.2:
            pag.click()
            pag.moveTo(bill_opt_btn)
            break
    while True:
        if 32.2 < np.mean(np.array(mss().grab(bill_opt_area))[:, :, :3]) < 32.3:
            pag.click()
            pag.moveTo(bill_non_btn)
            pag.click()
            pag.moveTo(buy_btn)
            pag.click()
            break


if DEBUG:
    import time
    while True:
        print()
        print('Mouse Position:', pag.position())
        print('buy_area:', np.mean(np.array(mss().grab(buy_area))[:, :, :3]))
        print('agree2_area:', np.mean(
            np.array(mss().grab(agree2_area))[:, :, :3]))
        print('bill_opt_area:', np.mean(
            np.array(mss().grab(bill_opt_area))[:, :, :3]))
        time.sleep(1)

checkTime()
purchase()
