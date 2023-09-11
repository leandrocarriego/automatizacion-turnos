from tkinter import Tk, StringVar

from GUI.frames.Users import Users
from GUI.frames.Header import Header
from schemas.schemas import Controls, UsersInfo
from threads.ThreadClass import *


# Window APP
class App:
    def __init__(self) -> None:
        self.window = Tk()

        self.app_controls = Controls(
            self.set_user_init,
            self.start_search,
            self.start_calendar_search,
            self.stop_window,
        )

        self.users_info = UsersInfo()

        self.thread1 = ThreadClass(self.set_state_app)
        self.thread2 = ThreadClass(self.set_state_app)
        self.thread3 = ThreadClass(self.set_state_app)
        self.thread4 = ThreadClass(self.set_state_app)

        self.user1_driver = None
        self.user2_driver = None
        self.user3_driver = None
        self.user4_driver = None

        self.procedure_var = StringVar()
        self.state_app = StringVar(value="")

        # USERS FRAME
        self.users_frame = Users(self.window, self.users_info)
        self.set_state_passport_forms("disabled")

        # HEADER FRAME
        header_frame = Header(
            self.window,
            self.procedure_var,
            self.state_app,
            self.set_state_passport_forms,
            self.app_controls,
        ).get_frame()

        self.window.title("Bot de turnos")
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        self.window.geometry(f"{screen_width}x{screen_height}")

        header_frame.grid(row=0, column=0, padx=20, pady=0)
        self.users_frame.get_frame().grid(row=1, column=0, padx=0, pady=5)

        self.window.mainloop()

    def set_user_init(self) -> None:
        for i in range(1, 5):
            current_user = getattr(self.users_info, f"user{i}")  
            current_thread = getattr(self, f"thread{i}") 
            
            if current_user.user.get() != "" and current_user.password.get() != "":
                current_thread.start(self.procedure_var.get(), current_user)
            else:
                self.set_state_app("ERROR. Debe ingresar un usuario y contraseña")


    def start_search(self) -> None:
        try:
            self.user1_driver = self.thread1.return_driver()
            self.user1_driver.start_search(
                self.procedure_var.get(), self.users_info.user1
            )
        except Exception as e:
            print("ERROR: ", e)
            # print(
            #     "ERROR: Debe abrir el navegador, hacer login y abrir el formulario de pasaporte o "
            #     "ciudadania primero, luego iniciar busqueda"
            # )
            # self.set_state_app("ERROR: Debe abrir el navegador y hacer login primero")

    def start_calendar_search(self) -> None:
        self.user1_driver.start_calendar_navigator()

    def set_state_passport_forms(self, new_state) -> None:
        users_from_list = [
            self.users_frame.user1_form,
            self.users_frame.user2_form,
            self.users_frame.user3_form,
            self.users_frame.user4_form,
        ]
        for form in users_from_list:
            form.set_state_form(new_state)

    def set_state_app(self, text) -> None:
        self.state_app.set(text)

    def stop_window(self) -> None:
        self.thread1.stop()
        self.thread2.stop()
        self.thread3.stop()
        self.thread4.stop()
