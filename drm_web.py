from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver

product_url = 'url'
user_agent = 'user-agent'
open_time = ['10시', '00분', '00초']
my_id = 'id'
my_pw = 'pw'
size = 'size'

driver = webdriver.Chrome()
driver.set_window_size(1920, 1080)
wait = WebDriverWait(driver, 10)
options = Options()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument('user-agent=%s' % user_agent)
time_driver = webdriver.Chrome(chrome_options=options)


def wait_click(xpath):
    wait.until(EC.presence_of_element_located((By.XPATH, xpath))).click()


def wait_send(xpath, keys):
    wait.until(EC.presence_of_element_located(
        (By.XPATH, xpath))).send_keys(keys)


def wait_get_elem(xpath):
    return wait.until(EC.presence_of_element_located((By.XPATH, xpath)))


def wait_get_elems(xpath):
    return wait.until(EC.presence_of_all_elements_located((By.XPATH, xpath)))


def check_time():
    sound_btn = '//*[@id="playAlram"]'
    time_area = '//*[@id="time_area"]'
    time_driver.get('https://time.navyism.com/?host=%s' % product_url)
    while True:
        try:
            time_driver.find_element(By.XPATH, sound_btn).click()
            break
        except:
            continue
    while True:
        server_time = time_driver.find_element(
            By.XPATH, time_area).text.split()[3:]
        if server_time == open_time:
            driver.get(product_url)
            break


def login():
    login_url = 'https://www.drmartens.co.kr/member/login'
    id_input = '//*[@id="vue-body"]/div/div/article/div/div[1]/form/div[1]/div/input'
    pw_input = '//*[@id="vue-body"]/div/div/article/div/div[1]/form/div[2]/div/input'
    submit_btn = '//*[@id="vue-body"]/div/div/article/div/div[1]/form/button'

    driver.get(login_url)
    wait_send(id_input, my_id)
    driver.find_element(By.XPATH, pw_input).send_keys(my_pw)
    driver.find_element(By.XPATH, submit_btn).click()


def purchase():
    option_btns = '//*[@id="vue-body"]/div/div[2]/div[2]/div/div/div[2]/div[1]/button/p'
    purchase_btn1 = '//*[@id="vue-body"]/div/div[2]/div[2]/div/div/div[3]/div[1]/button[2]'
    skip_btn = '//*[@id="wrap"]/main/div[3]/div[2]/div[3]/div/div/button'
    agree_btn = '//*[@id="vue-body"]/form/div/div/div/div[2]/fieldset/div/label'
    purchase_btn2 = '#vue-body > form > div > div > div > div > button.SettlePayButton'
    agree_btn2 = '//*[@id="frmObj"]/div[1]/div[2]/div[1]/div[2]/div[1]/label'
    bank_btn = '//*[@id="select_bank"]/option[3]'  # 기업은행
    next_btn = '//*[@id="spayNext"]'

    sizes = wait_get_elems(option_btns)
    for x in sizes:
        if x.text == size:
            x.click()
            break
    driver.find_element(By.XPATH, purchase_btn1).click()

    while True:
        if driver.find_elements(By.XPATH, skip_btn):
            driver.find_element(By.XPATH, skip_btn).click()
            break
        if driver.find_elements(By.XPATH, agree_btn):
            break
    wait_click(agree_btn)
    while True:
        try:
            driver.find_element(
                By.CSS_SELECTOR, purchase_btn2).send_keys(Keys.ENTER)
            break
        except:
            continue
    while True:
        try:
            driver.switch_to.frame('naxIfr')
            break
        except:
            continue
    wait_click(agree_btn2)
    driver.find_element(By.XPATH, bank_btn).click()
    driver.find_element(By.XPATH, next_btn).click()


login()
check_time()
driver.get(product_url)
purchase()
