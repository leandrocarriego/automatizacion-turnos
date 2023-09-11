from tkinter import Frame, StringVar
from tkinter.ttk import (
    LabelFrame,
    Label,
    Entry,
    Button,
    Radiobutton,
    Combobox,
    Spinbox,
    Notebook,
)

from GUI.widgets.LoginForm import LoginForm
from GUI.widgets.MultiBookingForm import MultiBookingForm
from schemas.schemas import UserInfo
from utils.select_pdf_file import select_pdf_file
from utils.change_state_notebook_tabs import enable_tabs, change_state_notebook_tabs

"""
Esta clase crea el formulario de pasaporte y actualiza con los datos ingresados 
el diccionario con los datos del usuario
user_info -> el diccionario con los datos del usuario
user_frame -> el frame del usuario dentro del cual estara el form dentro de la UI

SCHEMA
class UserInfo:
    def __init__(self):
        self.user = StringVar()
        self.password = StringVar()
        self.booking_type = IntVar()
        self.address = StringVar()
        self.children = BooleanVar()
        self.children_quantity = IntVar()
        self.civil_status = StringVar()
        self.complete_name_spouse = StringVar()
        self.country_passport = BooleanVar()
        self.country_passport_number = IntVar()
        self.height = IntVar()
        self.eye_color = StringVar()
        self.document_pdf = ''
        self.passport_pdf = ''
        self.additional_applicants_quantity = IntVar(value=1)
        self.additional_applicants_info = {
            "applicant1": AdditionalApplicantInfo(),
            "applicant2": AdditionalApplicantInfo(),
            "applicant3": AdditionalApplicantInfo(),
            "applicant4": AdditionalApplicantInfo(),
            "applicant5": AdditionalApplicantInfo(),
        }
"""


class PassportForm:
    def __init__(self, parent_frame: Frame, user_info: UserInfo) -> None:
        self.frame = LabelFrame(parent_frame, text="Formulario pasaporte")

        # Login frame
        login_frame = LoginForm(self.frame, user_info).get_frame()

        # Multiple book form frame
        multiple_booking_form_frame = LabelFrame(parent_frame, text="Reserva multiple")

        # Crear el contenedor de pestañas de formularios de aplicantes adicionales
        additional_applicant_tabs = Notebook(multiple_booking_form_frame)

        tab1 = MultiBookingForm(multiple_booking_form_frame, user_info, "1").get_frame()
        additional_applicant_tabs.add(tab1, text="Pestaña 1")
        additional_applicant_tabs.tab(0, state="normal")

        tab2 = MultiBookingForm(multiple_booking_form_frame, user_info, "2").get_frame()
        additional_applicant_tabs.add(tab2, text="Pestaña 2")
        additional_applicant_tabs.tab(1, state="normal")

        tab3 = MultiBookingForm(multiple_booking_form_frame, user_info, "3").get_frame()
        additional_applicant_tabs.add(tab3, text="Pestaña 3")
        additional_applicant_tabs.tab(2, state="normal")

        tab4 = MultiBookingForm(multiple_booking_form_frame, user_info, "4").get_frame()
        additional_applicant_tabs.add(tab4, text=f"Pestaña 4")
        additional_applicant_tabs.tab(3, state="normal")

        tab5 = MultiBookingForm(multiple_booking_form_frame, user_info, "5").get_frame()
        additional_applicant_tabs.add(tab5, text=f"Pestaña 5")
        additional_applicant_tabs.tab(4, state="normal")

        multi_booking_forms = [tab1, tab2, tab3, tab4, tab5]

        # Selector de cantidad de aplicantes adicionales
        multi_booking_selector = Combobox(
            multiple_booking_form_frame,
            values=[1, 2, 3, 4, 5],
            state="disable",
            textvariable=user_info.additional_applicants_quantity,
        )
        multi_booking_selector.bind(
            "<<ComboboxSelected>>",
            lambda event: enable_tabs(
                int(user_info.additional_applicants_quantity.get()),
                additional_applicant_tabs,
            ),
        )

        user_booking_type1_entry = Radiobutton(
            self.frame,
            text="Reserva Única",
            variable=user_info.booking_type,
            value=1,
            command=lambda: change_state_notebook_tabs(
                multi_booking_selector,
                "disable",
                additional_applicant_tabs,
            ),
        )

        user_booking_type2_entry = Radiobutton(
            self.frame,
            text="Reserva Múltiple",
            variable=user_info.booking_type,
            value=2,
            command=lambda: change_state_notebook_tabs(
                multi_booking_selector,
                "readonly",
                additional_applicant_tabs,
            ),
        )

        # CAMPOS
        # Dirección
        user_address_label = Label(self.frame, text="Dirección")
        user_address_entry = Entry(self.frame, textvariable=user_info.address)

        # Hijos
        user_children_label = Label(self.frame, text="Hijos menores")
        user_children_entry = Combobox(
            self.frame,
            values=[True, False],
            textvariable=user_info.children,
        )

        # Cantidad de hijos
        user_children_quantity_label = Label(
            self.frame, text="Cantidad de hijos menores"
        )
        user_children_quantity_entry = Spinbox(
            self.frame,
            from_=0,
            to=20,
            textvariable=user_info.children_quantity,
        )

        # Estado civil
        user_civil_status_label = Label(self.frame, text="Estado civil")
        user_civil_status_entry = Combobox(
            self.frame,
            values=[
                "Casado/a",
                "Divorciado/a",
                "Viudo/a",
                "Soltero/a",
                "Separado/a",
            ],
            textvariable=user_info.civil_status,
        )

        # Cónyuge
        user_name_spouse_label = Label(self.frame, text="Nombre y apellido del cónyuge")
        user_name_spouse_entry = Entry(
            self.frame, textvariable=user_info.complete_name_spouse
        )

        # Pasaporte del país
        user_country_passport_label = Label(self.frame, text="Posee pasaporte del país")
        user_country_passport_entry = Combobox(
            self.frame,
            values=[True, False],
            textvariable=user_info.country_passport,
        )

        # Número de pasaporte
        user_country_passport_number_label = Label(
            self.frame, text="Número de pasaporte"
        )
        user_country_passport_number_entry = Entry(
            self.frame, textvariable=user_info.country_passport_number
        )

        # Estatura
        user_height_label = Label(self.frame, text="Estatura en cm")
        user_height_entry = Entry(self.frame, textvariable=user_info.height)

        # Color de ojos
        user_eye_color_label = Label(self.frame, text="Color de ojos")
        user_eye_color_entry = Combobox(
            self.frame,
            values=["Celeste", "Marron", "Negro", "Verde"],
            textvariable=user_info.eye_color,
        )

        # DNI en pdf
        user_document_pdf_label = Label(self.frame, text="DNI en pdf")

        user_document_var = StringVar(value="No hay archivos cargados")
        user_document_pdf_title = Label(self.frame, text=user_document_var.get())

        user_document_pdf_entry = Button(
            self.frame,
            text="Seleccionar",
            command=lambda: select_pdf_file(
                user_info.document_pdf, user_document_var
            ),
        )

        # Pasaporte en pdf
        user_passport_pdf_label = Label(self.frame, text="Pasaporte en pdf")

        user_passport_var = StringVar(value="No hay archivos cargados")
        user_passport_pdf_title = Label(self.frame, text=user_passport_var.get())

        user_passport_pdf_entry = Button(
            self.frame,
            text="Seleccionar",
            command=lambda: select_pdf_file(
                user_info.passport_pdf, user_passport_var
            ),
        )

        # Posicionar los elementos
        self.frame.grid(row=0, column=0)

        login_frame.grid(row=0, column=0)

        multiple_booking_form_frame.grid(row=0, column=1, padx=5, pady=10)

        multi_booking_selector.grid(row=0, column=0, pady=10)
        multi_booking_selector.set(1)

        additional_applicant_tabs.grid(row=1, column=0, sticky="nsew")

        user_booking_type1_entry.grid(row=3, column=0)
        user_booking_type1_entry.invoke()

        user_booking_type2_entry.grid(row=3, column=1)

        user_address_label.grid(row=4, column=0)
        user_address_entry.grid(row=4, column=1)

        user_children_label.grid(row=5, column=0)
        user_children_entry.current(1)
        user_children_entry.grid(row=5, column=1)

        user_children_quantity_label.grid(row=6, column=0)
        user_children_quantity_entry.grid(row=6, column=1)

        user_civil_status_label.grid(row=7, column=0)
        user_civil_status_entry.current(0)
        user_civil_status_entry.grid(row=7, column=1)

        user_name_spouse_label.grid(row=8, column=0)
        user_name_spouse_entry.grid(row=8, column=1)

        user_country_passport_label.grid(row=9, column=0)
        user_country_passport_entry.current(1)
        user_country_passport_entry.grid(row=9, column=1)

        user_country_passport_number_label.grid(row=10, column=0)
        user_country_passport_number_entry.grid(row=10, column=1)

        user_height_label.grid(row=11, column=0)
        user_height_entry.grid(row=11, column=1)

        user_eye_color_label.grid(row=12, column=0)
        user_eye_color_entry.current(0)
        user_eye_color_entry.grid(row=12, column=1)

        user_document_pdf_label.grid(row=13, column=0)
        user_document_pdf_title.grid(row=13, column=1)
        user_document_pdf_entry.grid(row=13, column=2, padx=5, pady=10)

        user_passport_pdf_label.grid(row=15, column=0)
        user_passport_pdf_title.grid(row=15, column=1)
        user_passport_pdf_entry.grid(row=15, column=2, padx=5, pady=10)

        for widget in self.frame.winfo_children():
            # Excluir botones con el texto "Seleccionar"
            if isinstance(widget, Button) and widget["text"] == "Seleccionar":
                continue

            if isinstance(widget, Label) or isinstance(widget, Label):
                widget["width"] = 30
                widget["justify"] = "left"
                widget["anchor"] = "w"

            if isinstance(widget, Entry):
                widget["width"] = 40

            if isinstance(widget, Combobox) or isinstance(widget, Button):
                widget["width"] = 37

            if isinstance(widget, Spinbox):
                widget["width"] = 38

            widget.grid_configure(padx=10, pady=5)

    def set_state_form(self, new_state) -> None:
        for widget in self.frame.winfo_children():
            if isinstance(widget, (Entry, Button, Combobox, Spinbox, Radiobutton)):
                widget.configure(state=new_state)
