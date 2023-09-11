from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Esta clase se encarga de buscar el tipo de tramite, segun lo seleccionado en la UI
class Procedure_selector :
    def __init__(self, driver):
        self.driver = driver

    def go_to(self, method, value, procedure):
        while True:
            try:
                element_to_go = WebDriverWait(self.driver, 3).until(
                    EC.presence_of_element_located((method, value))
                )
                print("Se encontro el boton de " + procedure)
                element_to_go.click()
                print("Se hizo click")
                # En el caso de que salga el pop-up de que todavia no habilitaron los turnos 
                # se hace click en 'ok' y vuelve a intentar
                try:
                    # self.driver.find_element(
                    #     "xpath",
                    #     '//div[contains(text(), "Al momento non ci sono date disponibili per il servizio richiesto")]',
                    # )
                    # print("ERROR: Pop-up 'no hay turnos habilitados'")
                    self.driver.find_element(
                        "xpath", '//button[contains(text(), "ok")]'
                    ).click()
                    
                    
                    # BORRAR SOLO EN PRUEBA
                    print("break")
                    break
                
                # Si no encuentra el pop_up significa que entro en el tramite asi que para de intentar
                except:
                    print("break")
                    break
            # Puede que no aparezca el boton porque no esta habilitado, sigue intentando
            except:
                print("No se encontro " + value)
