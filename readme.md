# Selenium training


### imports
        from selenium import webdriver
        from selenium.webdriver.firefox.service import Service
        from selenium.webdriver.chrome.service import Service
        from selenium.webdriver.common.by import By
        from selenium.webdriver.common.keys import Keys
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        import time

### for Chrome
        service = Service(executable_path="/Users/imontero/cursus/selenium/chromedriver")
        driver = webdriver.Chrome(service=service)

### for Firefox
        options = webdriver.FirefoxOptions()
        service = Service(executable_path="/Users/imontero/cursus/selenium/geckodriver")
        driver = webdriver.Firefox(service=service, options=options)

### open browser window in url
        driver.get("https://google.com")

### espera 5s a encontrar el elemento
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "whatever"))
        )

### encontrar elementos
            # encuentra la primera ocurrencia 
            # o puede ser UID, ID... en vez de CLASS_NAME
        input_element = driver.find_element(By.CLASS_NAME, "whatever")
        
            # texto parcial
        link = driver.find_element(By.PARTIAL_LINK_TEXT, "whatever") 
            
            # texto exacto
        link = driver.find_element(By.LINK_TEXT, "whatever") 

            # links = []
            # links = driver.find_elements(By.LINK_TEXT, "whatever") #devuelve una lista con las ocurrencias

### limpiar campos
        input_element.clear()

### enviar un input y enter
        input_element.send_keys("whatever" + Keys.ENTER)
        
### clickar
        link.click()






time.sleep(150)

driver.quit()

