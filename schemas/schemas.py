from dataclasses import dataclass
from tkinter import StringVar, BooleanVar, IntVar


@dataclass
class Controls:
    init: callable
    load_data: callable
    search_calendar: callable
    finish: callable


class AdditionalApplicantInfo:
    def __init__(self) -> None:
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
        self.identification_document = ""
        self.passport_document = ""


class AdditionalApplicants:
    def __init__(self) -> None:
        self.applicant1 = AdditionalApplicantInfo()
        self.applicant2 = AdditionalApplicantInfo()
        self.applicant3 = AdditionalApplicantInfo()
        self.applicant4 = AdditionalApplicantInfo()
        self.applicant5 = AdditionalApplicantInfo()


class UserInfo:
    def __init__(self) -> None:
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
        self.document_pdf = ""
        self.passport_pdf = ""
        self.additional_applicants_quantity = IntVar(value=1)
        self.additional_applicants_info = AdditionalApplicants()


class UsersInfo:
    def __init__(self) -> None:
        self.user1 = UserInfo()
        self.user2 = UserInfo()
        self.user3 = UserInfo()
        self.user4 = UserInfo()
