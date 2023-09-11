from tkinter import Frame, LabelFrame
from tkinter.ttk import Button

from schemas.schemas import Controls

'''
Esta clase se encarga de ejecutar las acciones principales de la app
Los métodos de control pertenecen a 'App', están instanciados en el schema 'Controls'
Esta clase se instancia en 'Header'
'''


class ControlButtons:
    def __init__(self, parent_frame: LabelFrame, controls: Controls) -> None:
        self.frame = Frame(parent_frame, border=1)

        open_button = Button(
            self.frame, text="Abrir navegador", command=controls.init
        )

        start_button = Button(
            self.frame, text="Iniciar carga", command=controls.load_data
        )

        search_button = Button(
            self.frame,
            text="Buscar en calendario",
            command=controls.search_calendar,
        )

        stop_button = Button(
            self.frame, text="Finalizar", command=controls.finish
        )

        open_button.grid(row=0, column=0, padx=20, pady=10)
        start_button.grid(row=0, column=1, padx=20, pady=10)
        search_button.grid(row=0, column=2, padx=20, pady=10)
        stop_button.grid(row=0, column=3, padx=20, pady=10)

    def get_frame(self) -> Frame:
        return self.frame
