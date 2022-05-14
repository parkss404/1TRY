from selenium import webdriver
from selenium.webdriver.common.keys import Keys

my_place = input("지역을 입력하세요 : ")

driver = webdriver.Chrome()
driver.get("https://www.yogiyo.co.kr/")

driver.maximize_window()
time.sleep(1)

xpath = '''//*[@id="search"]/div/form/input'''
element = driver.find_element(By.XPATH, xpath)
element.clear()
time.sleep(1)

element.send_keys(my_place)
time.sleep(1)

search_button = '''//*[@id="button_search_address"]/button[2]'''
driver.find_element(By.XPATH, search_button).click()
time.sleep(1)

search_selector = '#search > div > form > ul > li:nth-child(3) > a'
search = driver.find_element(By.CSS_SELECTOR, search_selector)
search.click()
time.sleep(1)

input_box_xpath='''//*[@id="category"]/ul/li[1]/a'''
input_box=driver.find_element(By.XPATH, input_box_xpath)
time.sleep(1)
input_box.click()


