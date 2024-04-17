from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

service = Service(executable_path="geckodriver")
driver = webdriver.Firefox(service=service)

driver.get("https://google.com")

time.sleep(15)

driver.quit()
