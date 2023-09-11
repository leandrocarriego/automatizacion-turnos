from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Esta clase se encarga de encarga de llenar el form de ciudadania
class Citizenship1_form_filler :
    def __init__(self, driver, set_state_app) :
        self.driver = driver
        self.set_state_app = set_state_app

    def to_complete(self) :
        self.set_state_app('Llenando formulario de pasaporte...')

        # Accept privacy conditions
        privacy_conditions_check_btn = self.driver.find_element('id', 'PrivacyCheck')
        privacy_conditions_check_btn.click()

        # Submit form
        submit_btn = self.driver.find_element('id', 'btnAvanti')
        submit_btn.click()

        # Accept alert
        self.driver.switch_to.alert.accept()

         # Submit form
        submit_btn.click()

