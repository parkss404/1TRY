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
