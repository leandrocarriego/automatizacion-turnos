import threading
from actions.Driver.Driver import *



class ThreadClass:
    def __init__(self, set_state_app):
        self.thread = ""
        self.driver = ""
        self.set_state_app = set_state_app
        self.procedure = ""
        self.user_info = ""

    def start(self, procedure, user_info):
        if procedure == "":
            self.stop()
            self.set_state_app('ERROR. Debe seleccionar el tramite a realizar')

        else:
            self.set_state_app('Iniciando tramite...')
            self.procedure = procedure
            self.user_info = user_info
            self.thread = threading.Thread(target=self.thread_action)
            self.thread.start()

    def thread_action(self) -> None:
        #self.driver = Driver(self.set_state_app)
        print("En thread_action ")
        #self.driver.start_driver(self.procedure, self.user_info)

    def return_driver(self):
        return self.driver

    def stop(self):
        self.set_state_app('Finalizando busqueda...')

        if self.driver == "":
            print("Hilo.stop() - El driver esta vacio")
        else:
            #self.driver.stop_driver()
            self.driver = ""

        self.thread = ""
        if self.driver == "" and self.thread == "":
            self.set_state_app('Búsqueda finalizada')

    # def restart(self) :
    #     self.stop()
    #     time.sleep(3)
    #     self.start()
