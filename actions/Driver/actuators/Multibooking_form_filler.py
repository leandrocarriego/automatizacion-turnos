from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class Multibooking_form_filler:
    def __init__(self, driver, set_state_app) :
        self.driver = driver
        self.set_state_app = set_state_app
        

    def to_complete(self, additional_applicants_quantity, additional_applicants_info) :
        
        for i in range(additional_applicants_quantity):
            # Obtener los datos del aplicante actual
            applicant_info = additional_applicants_info[f"applicant{i+1}"]

            # Completar los campos para el aplicante actual
            self.complete_fields(i, applicant_info)

    def complete_fields(self, i, applicant_info):
        # Ejemplo: completar el campo last_name con el valor del diccionario
        last_name_input = self.driver.find_element(By.ID, f"Accompagnatori_{i}__CognomeAccompagnatore")
        last_name_input.send_keys(applicant_info["last_name"].get())

        # Completar el campo first_name con el valor del diccionario
        first_name_input = self.driver.find_element(By.ID, f"Accompagnatori_{i}__NomeAccompagnatore")
        first_name_input.send_keys(applicant_info["first_name"].get())

        # Completar el campo date_of_birth con el valor del diccionario
        date_of_birth_input = self.driver.find_element(By.ID, f"Accompagnatori_{i}__DataNascitaAccompagnatore")
        date_of_birth_input.send_keys(applicant_info["date_of_birth"].get())

        # # Completar el campo family_relationship si es True en el diccionario
        # if applicant_info["family_relationship"].get():
        #     family_relationship_input = self.driver.find_element(By.ID, f"ddlRelation_{i}")
        #     family_relationship_input.send_keys("Sí")  # Suponiendo que "Sí" es la opción para indicar relación

        # Completar el campo de direccion
        adress_input = self.driver.find_element(By.ID, f"Accompagnatori_{i}__DatiAddizionaliAccompagnatore_0___testo")
        adress_input.send_keys(applicant_info["address"].get())

        # Completar el campo de selección has_minor_children si es True en el diccionario
        # has_minor_children_input = self.driver.find_element(By.ID, f"ddlsAcc_{i}_1")
        # has_minor_children_select = Select(has_minor_children_input)
        # if applicant_info["has_minor_children"].get():
        #     # Seleccionar la opción correspondiente para "Sí"
        #     has_minor_children_select.select_by_value("1")
        # else:
        #     # Seleccionar la opción correspondiente para "No"
        #     has_minor_children_select.select_by_value("0")

        # Completar campos enteros si tienen valor en el diccionario
        number_of_minor_children_input = self.driver.find_element(By.ID, f"Accompagnatori_{i}__DatiAddizionaliAccompagnatore_2___testo")
        number_of_minor_children_input.send_keys(str(applicant_info["number_of_minor_children"].get()))

        # Select marital status
        # Aca se armo un diccionario con el 'value' que tiene la opcion en el html
        marital_status_opcions = {
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

        # # Se itera en por cada 'key' del diccionario y 
        # # se compara con la opcion seleccionada en la UI
        # for opcion in marital_status_opcions.keys() :
        #         if opcion == applicant_info["marital_status"].get() :
        #             civil_status_value = marital_status_opcions[opcion]
                    
        # # Se extrae el valor de la 'key' que coincide y se arma el xpath
        # marital_status_opcion_xpath = '//*[@id="ddls_3"]/option[@value="' + str(civil_status_value) + '"]'
        # marital_status_input = WebDriverWait(self.driver, 3).until(
        #             EC.presence_of_element_located((By.XPATH, marital_status_opcion_xpath))
        #             )
        # marital_status_input.click()

        # Completar el campo de nombre de conyugue
        spouse_name_input = self.driver.find_element(By.ID, f"Accompagnatori_{i}__DatiAddizionaliAccompagnatore_4___testo")
        spouse_name_input.send_keys(applicant_info["spouse_name"].get())

         # Completar campos de selección según corresponda a su tipo
        # has_italian_passport_input = self.driver.find_element(By.ID, f"Accompagnatori_{i}__DatiAddizionaliAccompagnatore_5___testo")
        # if applicant_info["has_italian_passport"].get():
        #     has_italian_passport_input.send_keys("Sí")
        # else:
        #     has_italian_passport_input.send_keys("No")

        # Completar el campo de numero de pasaporte
        passport_number_input = self.driver.find_element(By.ID, f"Accompagnatori_{i}__DatiAddizionaliAccompagnatore_6___testo")
        passport_number_input.send_keys(str(applicant_info["passport_number"].get()))

        # Completar el campo de numero de altura
        height_input = self.driver.find_element(By.ID, f"Accompagnatori_{i}__DatiAddizionaliAccompagnatore_7___testo")
        height_input.send_keys(str(applicant_info["height"].get()))

        # Completar el campo de color de ojos
        # eye_color_input = self.driver.find_element(By.ID, f"Accompagnatori_{i}__DatiAddizionaliAccompagnatore_8___testo")
        # eye_color_input.send_keys(applicant_info["eye_color"].get())
       
        # Completar campos de archivo adjunto si es necesario
        identification_document_input = self.driver.find_element(By.ID, f"Accompagnatori_{i}__DocumentiAccompagnatore_0___File")
        if (applicant_info["identification_document"] != ""):
            identification_document_input.send_keys(applicant_info["identification_document"])

        passport_document_input = self.driver.find_element(By.ID, f"Accompagnatori_{i}__DocumentiAccompagnatore_1___File")
        if (applicant_info["passport_document"] != "") :
            passport_document_input.send_keys(applicant_info["passport_document"])



