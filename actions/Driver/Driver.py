from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from actions.Driver.actuators.Login import *
from actions.Driver.actuators.Procedure_selector import *
from actions.Driver.actuators.Passport_form_filler import *
from actions.Driver.actuators.Citizenship1_form_filler import *
from actions.Driver.actuators.Calendar_navigator import *
import time


class Driver:
    def __init__(self, set_state_app):
        # self.latestchromedriver = ChromeDriverManager().install()
        self.service = Service(ChromeDriverManager().install())
        self.options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=self.service, options=self.options)
        # self.driver = webdriver.Chrome(service=self.service, options=self.options)
        self.procedure_selector = Procedure_selector(self.driver)
        self.passport_form_filler = Passport_form_filler(self.driver, set_state_app)
        self.citizenship1_form_filler = Citizenship1_form_filler(self.driver, set_state_app)
        self.calendar_navigator = Calendar_navigator(self.driver, set_state_app)


    def start_driver(self, procedure, user_info):
        # Login process
        self.driver.get("https://prenotami.esteri.it/")
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()

        # while True :
        #     self.driver.get("https://prenotami.esteri.it/")
        #     self.driver.implicitly_wait(15)
        #     self.driver.maximize_window()
        #     self.driver.implicitly_wait(15)
        #     self.start_login.login(user_info['user'].get(), user_info['password'].get())
        #     try :
        #         WebDriverWait(self.driver, 1).until(
        #             EC.presence_of_element_located((By.XPATH, '//body[contains(text(), "Unavailable")]'))
        #         )
        #         self.set_state_app("ERROR EN lOGIN: Unavailable")
        #         pass
        #     except :
        #         self.set_state_app("Se inicio sesion correctamente")
        #         break
        # self.driver.get("https://prenotami.esteri.it/Language/ChangeLanguage?lang=13")

        # # Process of navigating to prenote
        # while True :
        #     self.driver.get("https://prenotami.esteri.it/Services")
        #     try :
        #         WebDriverWait(self.driver, 3).until(
        #             EC.presence_of_element_located((By.XPATH, '//body[contains(text(), "The service is unavailable.")]')))
        #         self.set_state_app("ERROR NAVIGATE TO PRENOTA: The service is unavailable.")
        #         pass
        #     except :
        #         self.set_state_app("Se navego a la seccion de Prenota")
        #         break

        # Process of selecting procedure
        # self.set_state_app("Seleccionando tramite...")
        # if procedure == 'ciudadania1' :
        #     self.procedure_selector.go_to('xpath', '/html/body/main/div[3]/div/table/tbody/tr[2]/td[4]/a/button', procedure)
        # # elif procedure == 'ciudadania2' :
        # #     self.procedure_selector.go_to('xpath', '/html/body/main/div[3]/div/table/tbody/tr[4]/td[4]/a/button', procedure)
        # elif procedure == 'pasaporte' :
        #     self.procedure_selector.go_to('xpath', '/html/body/main/div[3]/div/table/tbody/tr[5]/td[4]/a/button', procedure)
        # else :
        #     self.set_state_app("ERROR: Al seleccionar tramite")
        #     self.stop_driver() 

    def start_search(self, procedure, user_info):
        if procedure == 'ciudadania1':
            self.citizenship1_form_filler.to_complete()
        elif procedure == 'pasaporte':
            # while True:
            # self.passport_form_filler.to_complete(user_info)
            try:
                self.passport_form_filler.to_complete(user_info)
                # WebDriverWait(self.driver, 3).until(
                # EC.presence_of_element_located((By.XPATH, '//section[@class="error-page"]'))
                # )
                # self.set_state_app("ERROR: Al enviar el formulario de pasaporte")
                # pass
                self.set_state_app("Se completo el formulario de pasaporte")

            except:
                self.set_state_app("Error al completar el formulario de pasaporte")
                # break

    def start_calendar_navigator(self):
        try:
            self.calendar_navigator.find_date()
        except:
            self.set_state_app("ERROR: Durante el recorrido del calendario")
            self.stop_driver()

    def stop_driver(self):
        self.driver.quit()
