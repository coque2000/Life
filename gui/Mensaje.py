import tkinter as tk

from tkinter import messagebox

class Mensaje:

    @staticmethod
    def mensaje_error(titulo=None, mensaje=None):
        messagebox.showerror(titulo, mensaje)

if __name__ == "__main__":
    Mensaje.mensaje_error("Ejemplo", "Mensaje ejemplo")