from selenium import webdriver
from selenium.webdriver.firefox.service import Service
import time


options = webdriver.FirefoxOptions()
service = Service(executable_path="geckodriver")
driver = webdriver.Firefox(service=service, options=options)


driver.get("https://google.com")

time.sleep(15)

driver.quit()
