from tkinter import filedialog, StringVar

def select_pdf_file(file_var: str, file_label: StringVar) -> None:
            file_var = filedialog.askopenfilename(
                initialdir="C:/",
                title="Seleccionar archivo",
                defaultextension=".pdf",
                filetypes=(("Archivos pdf", "*.pdf"),),
            )
            document_title = file_var.split("/")[
                len(file_var.split("/")) - 1
            ]
            file_label.set(document_title)