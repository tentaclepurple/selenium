from selenium import webdriver
from selenium.webdriver.firefox.service import Service
#from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

""" service = Service(executable_path="/Users/imontero/cursus/selenium/chromedriver")
driver = webdriver.Chrome(service=service) """

options = webdriver.FirefoxOptions()
service = Service(executable_path="/Users/imontero/cursus/selenium/geckodriver")
driver = webdriver.Firefox(service=service, options=options)

driver.get("https://google.com")

#espera 5s a encontrar el elemento
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, "whatever"))
)

# input.element = driver.find_element(By.CLASS_NAME, "whatever") o puede ser UID, ID...
# encuentra la primera ocurrencia 
input_element = driver.find_element(By.CLASS_NAME, "whatever")
input_element.clear() #limpiar campos
input_element.send_keys("whatever" + Keys.ENTER)

link = driver.find_element(By.PARTIAL_LINK_TEXT, "whatever") #testo parcial
#link = driver.find_element(By.LINK_TEXT, "whatever") #texto exacto
# links = []
# links = driver.find_elements(By.LINK_TEXT, "whatever") #devuelve una lista con las ocurrencias




link.click()




time.sleep(150)

driver.quit()
