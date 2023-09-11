from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

"""
Esta clase se encarga de navegar sobre el calendario y 
verificar si hay dias y horarios disponibles.
find_date(): Busca los dias que esten en en color verde, 
esto devuelve un array y lo guarda en la variable available_days.
Luego se recorren los dias disponibles, se hace click en cada uno
se guarda un array con los horarios disponibles de ese dia en available_times 
y se los comienza a recorrer, se hace click en el primero y se intenta reservar el horario
"""

class Calendar_navigator:
    def __init__(self, driver, set_state_app):
        self.driver = driver
        self.set_state_app = set_state_app
        self.time = time

    def find_date(self):
        self.set_state_app("Buscando turno en calendario...")
        self.time.sleep(5)

        while True:
            try:
                # Look for an available dates and click
                available_days = self.driver.find_elements(
                    By.XPATH, '//td[@class="day availableDay"]'
                )
                cant_dias_disponibles = len(available_days)
                if cant_dias_disponibles == 0:
                    self.set_state_app("No se encontraron días disponibles en este mes")
                    # Click on next button
                    self.driver.find_element(
                        By.CLASS_NAME, 'dtpicker-next'
                    ).click()
                    self.set_state_app("Buscando en el mes siguiente...")
                    continue
                self.set_state_app("Se encontraron " + str(cant_dias_disponibles) + " días en verde")

                for day in available_days:
                    print("Empezando a recorrer array de días en verde")
                    day.click()
                    self.set_state_app("Se seleccionó un día")
                    self.time.sleep(5)

                    available_times = self.driver.find_elements(
                        By.XPATH, '//div[@class="fascia act"]'
                    )
                    cant_horarios_disponibles = len(available_times)
                    if cant_horarios_disponibles == 0:
                        self.set_state_app("No se encontraron horarios disponibles en este día")
                        self.set_state_app("Buscando en el día siguiente...")
                        continue

                    self.set_state_app("Se encontraron " + str(cant_horarios_disponibles) + " horarios disponibles")

                    # Search if there is a schedule available and click
                    for time in available_times:
                        print("Empezando a recorrer el array de horarios")
                        time.click()
                        self.set_state_app("Se seleccionó un horario")
                        submit_btn = self.driver.find_element(By.ID, 'btnPrenota')
                        print("Se encontró el botón de prenota")
                        submit_btn.click()

                        # Check if the booking was successful
                        if self.is_booking_successful():
                            return

            except Exception as e:
                self.set_state_app("ERROR: al encontrar días en verde u horario libre")
                print(str(e))
                break

    # def is_booking_successful(self):
        # tODO: Implementar la lógica para verificar si la reserva fue exitosa
        # Puedes utilizar los métodos y atributos del driver para verificar si la reserva se realizó correctamente
        # Por ejemplo, puedes buscar elementos en la página que indiquen que la reserva fue exitosa y retornar True
        # si los encuentras, o retornar False si no los encuentras o si ocurre algún error.
        # Aquí puedes agregar tu lógica personalizada para verificar si la reserva fue exitosa.
        # Si la reserva fue exitosa, puedes realizar las acciones necesarias y retornar True.
        # Si la reserva no fue exitosa o si ocurre algún error, puedes retornar False.
        # return False



# class Calendar_navigator :
#     def __init__(self, driver, set_state_app) :
#         self.driver = driver
#         self.set_state_app = set_state_app
#         self.time = time

#     def find_date(self) :
#         self.set_state_app("Buscando turno en calendario...")
#         self.time.sleep(5)

#         while True :
#             try:
#                 # Look for an available dates and click
#                 available_days = self.driver.find_elements(
#                     "xpath", '//td[@class="day availableDay"]'
#                 )
#                 cant_dias_disponibles = len(available_days)
#                 if cant_dias_disponibles == 0 :
#                     self.set_state_app("No se encontraron dias disponibles en este mes")
#                     # Click on next button
#                     self.driver.find_element(
#                             "class", 'dtpicker-next'
#                         ).click()
#                     self.set_state_app("Buscando en el mes siguiente...")
#                     pass
#                 self.set_state_app("se encontraron " + str(cant_dias_disponibles) + " dias en verde")

#                 for day in available_days:
#                     print("empezando a recorrer array de dias en verde")
#                     day.click()
#                     self.set_state_app("Se selecciono un dia")
#                     self.time.sleep(5)

#                     available_times = self.driver.find_elements(
#                         "xpath", '//div[@class="fascia act"]'
#                     )
#                     cant_horarios_disponibles = len(available_times)
#                     if cant_horarios_disponibles == 0 :
#                         self.set_state_app("No se encontraron horarios disponibles en este dia")
#                         self.set_state_app("Buscando en el dia siguiente...")
#                         pass

#                     self.set_state_app("se encontraron " + str(cant_horarios_disponibles) + " horarios en disponibles")
                    
#                     # Search if there is a schedules available and click
#                     for time in available_times :
#                         print("empezando a recorrer el array de horarios")
#                         time.click()
#                         self.set_state_app("Se selecciono un horario")
#                         submit_btn = self.driver.find_element('id', 'btnPrenota')
#                         print("se encontro el boton de prenota")
#                         submit_btn.click()
                        
#                 # break

#             except:
#                 self.set_state_app("ERROR: al encontrar dias en verde u horario libre")
#                 break




                # Click on next button
                # self.driver.find_element(
                #         "class", 'dtpicker-next'
                #     ).click()
