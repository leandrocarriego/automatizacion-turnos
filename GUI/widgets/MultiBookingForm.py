import tkinter as tk
from tkinter.ttk import LabelFrame, Label, Entry, Button, Checkbutton, Combobox
from tkinter import filedialog, StringVar

from schemas.schemas import UserInfo
from utils.select_pdf_file import select_pdf_file

"""
Esta clase crea el formulario de pasaporte con booking multiple y actualiza con los datos ingresados 
el diccionario con los datos del usuario
user_info -> el diccionario con los datos del usuario
user_frame -> el frame del usuario dentro del cual estara el form dentro de la UI

class AdditionalApplicantInfo:
    def __init__(self):
        self.last_name = StringVar()
        self.first_name = StringVar()
        self.date_of_birth = StringVar()
        self.family_relationship = BooleanVar()
        self.address = StringVar()
        self.has_minor_children = BooleanVar()
        self.number_of_minor_children = IntVar()
        self.marital_status = BooleanVar()
        self.spouse_name = StringVar()
        self.has_country_passport = BooleanVar()
        self.passport_number = IntVar()
        self.height = IntVar()
        self.eye_color = StringVar()
        self.identification_document = ''
        self.passport_document = ''
"""





class MultiBookingForm:
    def __init__(
        self, parent_frame: LabelFrame, user_info: UserInfo, applicant_number: str
    ) -> None:
        applicant = f"applicant{applicant_number}"
        self.applicant_info = getattr(user_info.additional_applicants_info, applicant)

        self.frame = LabelFrame(parent_frame, text="Solicitante adicional")

        # Crear los elementos del formulario
        last_name_label = Label(self.frame, text="Apellido")
        last_name_entry = Entry(self.frame, textvariable=self.applicant_info.last_name)

        name_label = Label(self.frame, text="Nombre")
        name_entry = Entry(self.frame, textvariable=self.applicant_info.first_name)

        date_label = Label(self.frame, text="Fecha de Nacimiento (dd/mm/aaaa)")
        date_entry = Entry(self.frame, textvariable=self.applicant_info.date_of_birth)

        relationship_label = Label(self.frame, text="Relación Familiar")

        relationship_checkbox = Checkbutton(
            self.frame, variable=self.applicant_info.family_relationship
        )

        address_label = Label(self.frame, text="Dirección")
        address_entry = Entry(self.frame, textvariable=self.applicant_info.address)

        children_label = Label(self.frame, text="Hijos Menores")
        children_checkbox = Checkbutton(
            self.frame, variable=self.applicant_info.has_minor_children
        )

        number_of_children_label = Label(self.frame, text="Número de Hijos Menores")
        number_of_children_entry = Entry(
            self.frame, textvariable=self.applicant_info.number_of_minor_children
        )

        marital_status_label = Label(self.frame, text="Estado Civil")
        marital_status_checkbox = Checkbutton(
            self.frame, variable=self.applicant_info.marital_status
        )

        spouse_label = Label(
            self.frame,
            text="Nombre y Apellidos del Cónyuge/Unida Civilmente",
        )
        spouse_entry = Entry(self.frame, textvariable=self.applicant_info.spouse_name)

        passport_label = Label(
            self.frame,
            text="En posesión de un pasaporte italiano vencido o por vencer",
        )
        passport_checkbox = Checkbutton(
            self.frame, variable=self.applicant_info.has_italian_passport
        )

        passport_number_label = Label(self.frame, text="Número de Pasaporte")
        passport_number_entry = Entry(
            self.frame, textvariable=self.applicant_info.passport_number
        )

        height_label = Label(self.frame, text="Altura (cm)")
        height_entry = Entry(self.frame, textvariable=self.applicant_info.height)

        eye_color_label = Label(self.frame, text="Color de Ojos")
        eye_color_combobox = Combobox(
            self.frame,
            values=["Azul", "Verde", "Marrón", "Gris", "Negro"],
            textvariable=self.applicant_info.eye_color,
        )

        document_file_label = Label(self.frame, text="Documento de Identidad (PDF)")
        document_title_var = StringVar(value="No hay archivos cargados")
        document_file_title = Label(self.frame, text=document_title_var.get())

        document_file_select_button = Button(
            self.frame,
            text="Seleccionar",
            command=lambda: select_pdf_file(
                self.applicant_info.identification_document, document_title_var
            ),
        )

        passport_file_label = Label(self.frame, text="Pasaporte (PDF)")
        passport_title_var = StringVar(value="No hay archivos cargados")
        passport_file_title = Label(self.frame, text=passport_title_var.get())

        passport_file_select_button = Button(
            self.frame,
            text="Seleccionar",
            command=lambda: select_pdf_file(
                self.applicant_info.passport_document, passport_title_var
            ),
        )

        # Posicionar los elementos
        self.frame.grid(row=1, column=0, padx=0, pady=10)
        self.frame.state(["disabled"])

        last_name_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        last_name_entry.grid(row=0, column=1, padx=5, pady=5)

        name_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        name_entry.grid(row=1, column=1, padx=5, pady=5)

        date_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        date_entry.grid(row=2, column=1, padx=5, pady=5)

        relationship_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
        relationship_checkbox.grid(row=3, column=1, padx=5, pady=5)

        address_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")
        address_entry.grid(row=4, column=1, padx=5, pady=5)

        children_label.grid(row=5, column=0, padx=5, pady=5, sticky="w")
        children_checkbox.grid(row=5, column=1, padx=5, pady=5)

        number_of_children_label.grid(row=6, column=0, padx=5, pady=5, sticky="w")
        number_of_children_entry.grid(row=6, column=1, padx=5, pady=5)

        marital_status_label.grid(row=7, column=0, padx=5, pady=5, sticky="w")
        marital_status_checkbox.grid(row=7, column=1, padx=5, pady=5)

        spouse_label.grid(row=8, column=0, padx=5, pady=5, sticky="w")
        spouse_entry.grid(row=8, column=1, padx=5, pady=5)

        passport_label.grid(row=9, column=0, padx=5, pady=5, sticky="w")
        passport_checkbox.grid(row=9, column=1, padx=5, pady=5)

        passport_number_label.grid(row=10, column=0, padx=5, pady=5, sticky="w")
        passport_number_entry.grid(row=10, column=1, padx=5, pady=5)

        height_label.grid(row=11, column=0, padx=5, pady=5, sticky="w")
        height_entry.grid(row=11, column=1, padx=5, pady=5)

        eye_color_label.grid(row=12, column=0, padx=5, pady=5, sticky="w")
        eye_color_combobox.grid(row=12, column=1, padx=5, pady=5)

        document_file_label.grid(row=13, column=0, padx=5, pady=5, sticky="w")
        document_file_title.grid(row=13, column=1, padx=5, pady=5)
        document_file_select_button.grid(row=13, column=2, padx=5, pady=5)

        passport_file_label.grid(row=14, column=0, padx=5, pady=5, sticky="w")
        passport_file_title.grid(row=14, column=1, padx=5, pady=5)
        passport_file_select_button.grid(row=14, column=2, padx=5, pady=5)

        for widget in self.frame.winfo_children():
            # Excluir botones con el texto "Seleccionar"
            if isinstance(widget, Button) and widget["text"] == "Seleccionar":
                continue

            if isinstance(widget, tk.Label) or isinstance(widget, Label):
                widget["width"] = 30
                widget["justify"] = "left"
                widget["anchor"] = "w"

            if isinstance(widget, Entry):
                widget["width"] = 36

            if isinstance(widget, Combobox):
                widget["width"] = 37

            widget.grid_configure(padx=10, pady=5)
            widget.configure(state="disabled")

    def get_frame(self) -> LabelFrame:
        return self.frame
