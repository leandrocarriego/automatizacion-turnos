from tkinter import Tk, LabelFrame, StringVar

from GUI.widgets.AppState import AppState
from GUI.widgets.ControlButtons import ControlButtons
from GUI.widgets.ProcedureSelector import ProcedureSelector
from schemas.schemas import Controls


class Header:
    def __init__(self, parent_frame: Tk, procedure_var: StringVar, app_state: StringVar,
                 set_state_passport_forms: callable, app_controls: Controls) -> None:
        self.frame = LabelFrame(
            parent_frame, text="Buscador de turnos", font=("Arial", 15)
        )

        procedures_frame = ProcedureSelector(self.frame, procedure_var,
                                             set_state_passport_forms).get_frame()

        app_state_frame = AppState(self.frame, app_state).get_frame()

        control_buttons_frame = ControlButtons(self.frame, app_controls).get_frame()

        procedures_frame.grid(row=0, column=0, padx=20, pady=10)
        app_state_frame.grid(row=0, column=1, padx=20, pady=10)
        control_buttons_frame.grid(row=0, column=2, padx=20, pady=10)

    def get_frame(self) -> LabelFrame:
        return self.frame
