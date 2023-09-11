from tkinter import Tk, Frame
from tkinter.ttk import Notebook

from GUI.widgets.PassportForm import PassportForm
from schemas.schemas import UsersInfo

"""
Este es el frame de todo lo relacionado a los usuarios
Incluye el frame 'Passport'
Se instancia en 'Window'
"""


class Users:
    def __init__(self, parent_frame: Tk, users_info: UsersInfo) -> None:
        self.frame = Notebook(parent_frame)

        # User 1
        user1_tab = Frame(self.frame)

        self.user1_form = PassportForm(
            user1_tab,
            users_info.user1,
        )

        # # User 2
        user2_tab = Frame(self.frame)

        self.user2_form = PassportForm(
            user2_tab,
            users_info.user2,
        )

        # # User 3
        user3_tab = Frame(self.frame)

        self.user3_form = PassportForm(
            user3_tab,
            users_info.user3,
        )

        # User 4
        user4_tab = Frame(self.frame)

        self.user4_form = PassportForm(
            user4_tab,
            users_info.user4,
        )

        user1_tab.grid(row=0, column=0, padx=0, pady=10)
        user2_tab.grid(row=0, column=1, padx=0, pady=10)
        user3_tab.grid(row=0, column=2, padx=0, pady=10)
        user4_tab.grid(row=0, column=3, padx=0, pady=10)

        self.frame.add(user1_tab, text="Usuario 1")
        self.frame.add(user2_tab, text="Usuario 2")
        self.frame.add(user3_tab, text="Usuario 3")
        self.frame.add(user4_tab, text="Usuario 4")

    def get_frame(self) -> Notebook:
        return self.frame
