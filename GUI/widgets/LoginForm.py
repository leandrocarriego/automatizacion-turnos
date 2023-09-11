from tkinter import LabelFrame
from tkinter.ttk import Label, Entry

from schemas.schemas import UserInfo


class LoginForm:
    def __init__(self, parent_frame: LabelFrame, user_info: UserInfo) -> None:
        self.frame = LabelFrame(parent_frame, border=1, text="Login")

        user_username_label = Label(self.frame, width=10, text="Usuario")
        user_username_entry = Entry(self.frame, width=30, textvariable=user_info.user)

        user_password_label = Label(self.frame, width=10, text="Contraseña")
        user_password_entry = Entry(self.frame, width=20, textvariable=user_info.password)

        user_username_label.grid(row=0, column=0, padx=10, pady=15)
        user_username_entry.grid(row=0, column=1, padx=0, pady=15)

        user_password_label.grid(row=0, column=2, padx=10, pady=15)
        user_password_entry.grid(row=0, column=3, padx=10, pady=15)

    def get_frame(self) -> LabelFrame:
        return self.frame
