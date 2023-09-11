from selenium.webdriver.common.by import By
import time

class Login :
    def __init__(self, driver, state_text) :
        self.driver = driver
        self.state_text = state_text

    def login(self, user, password) :
        self.state_text('Iniciando sesión...')
        input_user = self.driver.find_element(by=By.NAME, value="Email")
        input_password = self.driver.find_element(by=By.NAME, value="Password")
        login_btn = self.driver.find_element(by=By.XPATH, value='//button[contains(text(), "Avanti")]')
        input_user.send_keys(user)
        input_password.send_keys(password)
        time.sleep(2)
        login_btn.click()
        
            