from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver


purchase_time = ['10시', '00분', '00초']
url = 'url'
user_agent = 'user-agent'
options = ['op1', 'op2']

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)


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
            driver.get(url)
            return


def purchase():
    for i in range(len(options)):
        ops = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#option%d > option' % (i+1))))
        for op in ops:
            if options[i] in op.text:
                op.click()
                break
    driver.find_element(
        By.CSS_SELECTOR, '#product_order_info > div.explan_product.option_select_section.opt-select-box > div.box-btn-buy.wrap-btn-buy > div.btn_buy > a').send_keys(Keys.ENTER)
    wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, '#payment_info_area > ul:nth-child(9) > li.cell_discount_detail.last > p:nth-child(1) > label > span'))).click()
    driver.find_element(By.CSS_SELECTOR, '#btn_pay').send_keys(Keys.ENTER)
    driver.switch_to.frame(wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#naxIfr'))))
    wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, '#frmObj > div.content > div.con > div.agree_new.form_row > div.agree_chk_bg > div.chk_box.chk_agree_all > label'))).click()
    driver.find_element(By.CSS_SELECTOR, '#spayNext').click()
    wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, '#frmObj > div.content > div.con > div:nth-child(5) > div.chk_box.chk_cash.ma_t20 > label'))).click()
    driver.find_element_by_css_selector('#spayNext').click


checkTime()
purchase()
