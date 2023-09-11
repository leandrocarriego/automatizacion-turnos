from tkinter import LabelFrame, StringVar
from tkinter.ttk import Label

'''
Esta clase se encarga de mostrar los mensajes de estado de la app
La variable que representa el estado pertenece a 'Window' 
Esta clase se instancia en 'Header'
'''


class AppState:
    def __init__(self, parent_frame: LabelFrame, app_state: StringVar) -> None:
        self.frame = LabelFrame(parent_frame, border=1, text="")

        state_app_label = Label(
            self.frame, width=50, textvariable=app_state
        )

        state_app_label.grid(row=0, column=0, padx=50, pady=5)

    def get_frame(self) -> LabelFrame:
        return self.frame
