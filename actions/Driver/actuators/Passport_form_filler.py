from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from actions.Driver.actuators.Multibooking_form_filler import *


class Passport_form_filler :
    def __init__(self, driver, set_state_app) :
        self.driver = driver
        self.set_state_app = set_state_app
        self.multibooking_form_filler = Multibooking_form_filler(driver, set_state_app)

    def to_complete(self, user_info) :
        self.set_state_app('Llenando formulario de pasaporte...')

        # Complete reservation type
        print("Buscando boton selector de tipo de formulario")        
        if (user_info["booking_type"].get() == 1) :
            booking_type_opc = WebDriverWait(self.driver, 3).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="typeofbookingddl"]/option[@value="1"]'))
                    )
            booking_type_opc.click()
        elif (user_info["booking_type"].get() == 2) :
            booking_type_opc = WebDriverWait(self.driver, 3).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="typeofbookingddl"]/option[@value="2"]'))
                    )
            booking_type_opc.click()
            additional_applicants_quantity_opc = WebDriverWait(self.driver, 3).until(
                    EC.presence_of_element_located((By.XPATH, f'//*[@id="ddlnumberofcompanions"]/option[@value="{user_info["additional_applicants_quantity"].get()}"]'))
                    )
            additional_applicants_quantity_opc.click()
            
        print('Se encontro el boton de reserva multiple y se selecciono')

        

        # Complete the address of the resident
        address_input = self.driver.find_element('id', 'DatiAddizionaliPrenotante_0___testo')
        address_input.send_keys(user_info["address"].get())

        # Indicate if the user has children
        print("Buscando boton selector de si tiene hijos")
        if (user_info["children"].get()) :
            children_input = WebDriverWait(self.driver, 3).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="ddls_1"]/option[@value="11"]'))
                    )
        elif (not user_info["children"].get()) :
            children_input = WebDriverWait(self.driver, 3).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="ddls_1"]/option[@value="12"]'))
                    )
        children_input.click()
        print('Se encontro el boton de hijo')

        # Indicate number of children
        children_quantity_input = self.driver.find_element('id', 'DatiAddizionaliPrenotante_2___testo')
        children_quantity_input.send_keys(user_info["children_quantity"].get())

        # Select marital status
        # Aca se armo un diccionario con el 'value' que tiene la opcion en el html
        civil_status_opcions = {
            "Casado/a": 13,
            "Divorciado/a": 14,
            "Viudo/a": 15,
            "Soltero/a": 16,
            "Separado/a": 17,
            "Unido/a civilmente": 18,
            "Separado/a da Un. Civ.": 19,
            "Divorciado/a da Un. Civ.": 20,
            "Viudo/a da Un. Civ.": 21
        }

        # Se itera en por cada 'key' del diccionario y 
        # se compara con la opcion seleccionada en la UI
        for opcion in civil_status_opcions.keys() :
                if opcion == user_info["civil_status"].get() :
                    civil_status_value = civil_status_opcions[opcion]
                    
        # Se extrae el valor de la 'key' que coincide y se arma el xpath
        civil_status_opcion_xpath = '//*[@id="ddls_3"]/option[@value="' + str(civil_status_value) + '"]'
        civil_status_input = WebDriverWait(self.driver, 3).until(
                    EC.presence_of_element_located((By.XPATH, civil_status_opcion_xpath))
                    )
        civil_status_input.click()
        
        # Complete name of spouse
        complete_name_spouse_input = self.driver.find_element('id', 'DatiAddizionaliPrenotante_4___testo')
        complete_name_spouse_input.send_keys(user_info["complete_name_spouse"].get())

        # Indicate if the user has an passport
        print("Buscando boton selector de si tiene pasaporte")
        if (user_info["country_passport"].get()) :
            country_passport_input = WebDriverWait(self.driver, 3).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="ddls_5"]/option[@value="1"]'))
                    )
        elif (not user_info["country_passport"].get()) :
            country_passport_input = WebDriverWait(self.driver, 3).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="ddls_5"]/option[@value="2"]'))
                    )
        country_passport_input.click()
        print('Se encontro el boton de pasaporte y se hizo click')
        
        # Indicate passport number
        country_passport_number_input = self.driver.find_element('id', 'DatiAddizionaliPrenotante_6___testo')
        country_passport_number_input.send_keys(user_info["country_passport_number"].get())

        # Indicate height
        height_input = self.driver.find_element('id', 'DatiAddizionaliPrenotante_7___testo')
        height_input.send_keys(user_info["height"].get())

        # Indicate eye color
         # Aca se armo un diccionario con el 'value' que tiene la opcion en el html
        eye_color_opcions = {
            "Celeste": 22, 
            "Marron": 23, 
            "Gris": 24, 
            "Negro": 25, 
            "Verde": 26
        }

        # Se itera en por cada 'key' del diccionario y 
        # se compara con la opcion seleccionada en la UI
        for opcion in eye_color_opcions.keys() :
                if opcion == user_info["eye_color"].get() :
                    eye_color_value = eye_color_opcions[opcion]

        # Se extrae el valor de la 'key' que coincide y se arma el xpath
        eye_color_opcion_xpath = '//*[@id="ddls_8"]/option[@value="' + str(eye_color_value) + '"]'
        eye_color_input = WebDriverWait(self.driver, 3).until(
                    EC.presence_of_element_located((By.XPATH, eye_color_opcion_xpath))
                    )
        eye_color_input.click()

        # Upload DNI file
        document_pdf_input = self.driver.find_element('id', 'File_0')
        if (user_info["document_pdf"] != "") :
            document_pdf_input.send_keys(user_info["document_pdf"])

        # Upload passport file
        passport_pdf_input = self.driver.find_element('id', 'File_1')
        if (user_info["passport_pdf"] != "") :
            passport_pdf_input.send_keys(user_info["passport_pdf"])


        # Accept privacy conditions
        privacy_conditions_check_btn = self.driver.find_element('id', 'PrivacyCheck')
        privacy_conditions_check_btn.click()

        if (user_info["booking_type"].get() == 2) :
             self.multibooking_form_filler.to_complete(user_info["additional_applicants_quantity"].get(), user_info["additional_applicants_info"])

        # Submit form
        submit_btn = self.driver.find_element('id', 'btnAvanti')
        submit_btn.click()
        
        # # Accept alert
        self.driver.switch_to.alert.accept()


        


        