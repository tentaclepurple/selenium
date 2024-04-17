from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.FirefoxOptions()
service = Service(executable_path="/Users/imontero/cursus/selenium/geckodriver")
driver = webdriver.Firefox(service=service, options=options)

driver.get("https://google.com")


WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//div[text()='Rechazar todo']"))
)
element = driver.find_element(By.XPATH, "//div[text()='Rechazar todo']")

element.click()

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, "gLFyf"))
)
box = driver.find_element(By.CLASS_NAME, "gLFyf")

box.clear()
box.send_keys("asqueroso" + Keys.ENTER)


"""
# encuentra la primera ocurrencia 
input_element = driver.find_element(By.CLASS_NAME, "whatever")
input_element.clear() #limpiar campos
input_element.send_keys("whatever" + Keys.ENTER)

link = driver.find_element(By.PARTIAL_LINK_TEXT, "whatever") #testo parcial






QS5gu sy4vM

 """


time.sleep(15)

driver.quit()
