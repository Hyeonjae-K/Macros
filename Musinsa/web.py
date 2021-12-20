from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver


purchase_time = ['00시', '00분', '00초']
url = 'URL'
user_agent = 'User_Agent'
options = []

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
    time_driver.find_element(By.CSS_SELECTOR, alarm_box).click()  # 정각 알람 비활성화

    while True:
        server_time = time_driver.find_element(
            By.CSS_SELECTOR, time_area).text.split()[3:]
        if purchase_time == server_time:
            return


def purchase():
    option_tag = '#option%d > option'
    buy_btn = '#product_order_info > div.explan_product.option_select_section.opt-select-box > div.box-btn-buy.wrap-btn-buy > div.btn_buy > a'
    agree_all1 = '#payment_info_area > ul:nth-child(9) > li.cell_discount_detail.last > p:nth-child(1) > label > span'
    pay_btn = '#btn_pay'
    frame_id = '#naxIfr'
    agree_all2 = '#frmObj > div.content > div.con > div.agree_new.form_row > div.agree_chk_bg > div.chk_box.chk_agree_all > label'
    next_btn = '#spayNext'
    bill_btn = '#frmObj > div.content > div.con > div:nth-child(5) > div.chk_box.chk_cash.ma_t20 > label'

    # 옵션 선택창
    driver.get(url)
    for idx, option in enumerate(options):
        item_options = driver.find_elements(
            By.CSS_SELECTOR, option_tag % (idx+1))
        for item_option in item_options:
            if option in item_option.text:
                item_option.click()
                break
    driver.find_element(By.CSS_SELECTOR, buy_btn).click()

    # 주문 정보창
    wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, agree_all1))).click()
    driver.find_element(By.CSS_SELECTOR, pay_btn).click()

    # 가상계좌 결제 요청창
    driver.switch_to.frame(wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, frame_id))))
    wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, agree_all2))).click()
    driver.find_element(By.CSS_SELECTOR, next_btn).click()

    wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, bill_btn))).click()
    driver.find_element(By.CSS_SELECTOR, next_btn).click()


driver.get('https://store.musinsa.com/app/')
checkTime()
purchase()
