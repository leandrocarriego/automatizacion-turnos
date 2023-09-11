from tkinter.ttk import Combobox, Notebook


def set_disable_applicants(applicants: Notebook) -> None:
    for i in range(5):
        applicants.tab(i, state="disable")


def set_enable_applicants(selected_quantity: int, applicants: Notebook) -> None:
    for i in range(selected_quantity):
        applicants.tab(i, state="normal")


def enable_tabs(selected_quantity: int, applicants: Notebook) -> None:
    set_disable_applicants(applicants)
    set_enable_applicants(selected_quantity, applicants)


def change_state_notebook_tabs(
    widget: Combobox,
    state: str,
    applicants: Notebook,
) -> None:
    widget.config(state=state)

    if state == "disable":
        set_disable_applicants(applicants)
    elif state == "normal":
        set_enable_applicants(1, applicants)