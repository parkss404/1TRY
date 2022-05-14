from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get("https://www.yogiyo.co.kr/")

driver.maximize_window()
time.sleep(1)

