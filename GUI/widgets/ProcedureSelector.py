from tkinter import Frame, LabelFrame, StringVar
from tkinter.ttk import Radiobutton

'''
Esta clase se encarga de seleccionar el tipo de tramite a completar 
y de habilitar/deshabilitar el formulario de pasaporte
Recibe la variable procedure_var y el método set_state_passport_forms pertenecen a 'Window'
Esta clase se instancia en 'Header'
'''


class ProcedureSelector:
    def __init__(self, parent_frame: LabelFrame, procedure_var: StringVar, set_state_passport_forms: callable) -> None:
        self.frame = Frame(parent_frame, border=1)

        procedure1_radio = Radiobutton(
            self.frame,
            text="Ciudadanía 1",
            variable=procedure_var,
            value="ciudadania1",
            command=lambda: set_state_passport_forms("disable"),
        )

        procedure2_radio = Radiobutton(
            self.frame,
            text="Passaporto",
            variable=procedure_var,
            value="pasaporte",
            command=lambda: set_state_passport_forms("normal"),
        )

        procedure_var.set('ciudadania1')

        procedure1_radio.grid(row=1, column=0, padx=10, pady=10)
        procedure2_radio.grid(row=1, column=2, padx=10, pady=10)

    def get_frame(self) -> Frame:
        return self.frame
