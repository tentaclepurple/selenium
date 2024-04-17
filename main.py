from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

service = Service(executable_path="/Users/imontero/cursus/selenium/chromedriver")
drive = webdriver.Chrome(service=service)

driver.get("https://google.com")

time.sleep(15)

driver.quite()
