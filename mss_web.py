from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

my_id = 'id'
my_pw = 'pw'
purchase_time = ['10시', '00분', '00초']
url = 'url'
options = ['op1', 'op2']

options = Options()
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
options.add_argument('headless')
options.add_argument('user-agent=%s' % user_agent)
time_driver = webdriver.Chrome()
driver = webdriver.Chrome()


def login():
    driver.get(
        'https://my.musinsa.com/login/v1/login?referer=https%3A%2F%2Fstore.musinsa.com%2Fapp%2F')
    driver.find_element_by_css_selector(
        'body > div.musinsa-wrapper.wrapper-member.devicePC > div.n-member-area > form > input:nth-child(5)').send_keys(my_id)
    driver.find_element_by_css_selector(
        'body > div.musinsa-wrapper.wrapper-member.devicePC > div.n-member-area > form > input:nth-child(6)').send_keys(my_pw)
    driver.find_element_by_css_selector(
        'body > div.musinsa-wrapper.wrapper-member.devicePC > div.n-member-area > form > button').click()
    driver.get(url)


def checkTime():
    time_driver.get('https://time.navyism.com/?host=store.musinsa.com')
    time_driver.find_element_by_css_selector(
        '#navyismMainContainer > div:nth-child(15) > div:nth-child(1) > div:nth-child(1) > label:nth-child(2)').click()
    time_driver.find_element_by_css_selector(
        '#navyismMainContainer > div:nth-child(15) > div:nth-child(1) > div:nth-child(2) > label:nth-child(4)').click()
    while True:
        server_time = time_driver.find_element_by_css_selector(
            '#time_area').text.split()[3:]
        if server_time == purchase_time:
            driver.get(url)
            break


def purchase():
    for i in range(len(options)):
        ops = driver.find_elements_by_css_selector(
            '#option%d > option' % (i+1))
        for op in ops:
            if options[i] in op.text:
                op.click()
                break
    driver.find_element_by_css_selector(
        '#product_order_info > div.explan_product.option_select_section.opt-select-box > div.box-btn-buy.wrap-btn-buy > div.btn_buy > a').send_keys(Keys.ENTER)
    while True:
        try:
            driver.find_element_by_css_selector(
                '#payment_info_area > ul:nth-child(9) > li.cell_discount_detail.last > p:nth-child(1) > label > span').click()
        except:
            continue
        else:
            break
    driver.find_element_by_css_selector(
        '#btn_pay').send_keys(Keys.ENTER)
    while True:
        try:
            driver.switch_to.frame(
                driver.find_element_by_css_selector('#naxIfr'))
        except:
            continue
        else:
            break
    while True:
        try:
            driver.find_element_by_css_selector(
                '#frmObj > div.content > div.con > div.agree_new.form_row > div.agree_chk_bg > div.chk_box.chk_agree_all > label').click()
        except:
            continue
        else:
            break
    driver.find_element_by_css_selector('#spayNext').click()
    while True:
        try:
            driver.find_element_by_css_selector(
                '#frmObj > div.content > div.con > div:nth-child(5) > div.chk_box.chk_cash.ma_t20 > label').click()
        except:
            continue
        else:
            break


login()
checkTime()
purchase()
