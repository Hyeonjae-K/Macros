from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver


purchase_time = ['00시', '00분', '00초']
url = 'url'
user_agent = 'User-Agent'
size = 'size'

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)


def checkTime():
    chrome_options = Options()
    chrome_options.add_argument('headless')
    chrome_options.add_argument('user-agent=%s' % user_agent)
    time_driver = webdriver.Chrome(options=chrome_options)
    alarm_box = '#playAlram'
    time_area = '#time_area'

    time_driver.get('https://time.navyism.com/?host=grandstage.a-rt.com')
    time_driver.find_element(By.CSS_SELECTOR, alarm_box).click()

    while True:
        server_time = time_driver.find_element(
            By.CSS_SELECTOR, time_area).text.split()[3:]
        if purchase_time == server_time:
            driver.get(url)
            return


def purchase():
    sizes_selector = '#contentsWrap > div > div.contents-inner.product-detail-wrap > div.product-detail-box > div.detail-box-right > div.border-line-box.tbl-form-wrap.form-view > table > tbody > tr:nth-child(12) > td > ul > li > button'
    buy_selector = '#contentsWrap > div > div.contents-inner.product-detail-wrap > div.product-detail-box > div.detail-box-right > div.btn-wrap.col2 > button:nth-child(2)'
    agree_selector1 = '#orderForm > div.order-payment-wrap > div.order-payment-form > div:nth-child(13) > div > ul > li > div.fold-box-header > span > label'
    pay_selector = '#btnPayment'
    frame_selector = '#naxIfr'
    agree_selector2 = '#frmObj > div.content > div.con > div.agree_new.form_row > div.agree_chk_bg > div.chk_box.chk_agree_all > label'
    bank_selector = '#select_bank > option:nth-child(3)'  # 기업은행
    next_selector = '#spayNext'
    bill_selector = '#frmObj > div.content > div.con > div:nth-child(5) > div.chk_box.chk_cash.ma_t20 > label'

    # 옵션 선택 화면
    buy_btn = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, buy_selector)))
    sizes = driver.find_elements(By.CSS_SELECTOR, sizes_selector)
    for x in sizes:
        if size == x.text:
            x.click()
            buy_btn.click()
            break

    # 주문 화면
    wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, agree_selector1))).click()
    driver.find_element(By.CSS_SELECTOR, pay_selector).click()

    # 결제 화면
    driver.switch_to.frame(wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, frame_selector))))
    wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, agree_selector2))).click()
    driver.find_element(By.CSS_SELECTOR, bank_selector).click()
    driver.find_element(By.CSS_SELECTOR, next_selector).click()

    wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, bill_selector))).click()
    driver.find_element(By.CSS_SELECTOR, next_selector).click()


driver.get('https://grandstage.a-rt.com/?track=W0009')
checkTime()
purchase()
