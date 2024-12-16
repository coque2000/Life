import tkinter as tk
from gui.Mensaje import Mensaje

class Entrada_Datos_UI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Life")
        self.geometry("450x250")
        self._densidad: float = 0
        self._generaciones: int = 0
        self.body()

    def body(self):
        titulo_principal = tk.Label(self, text="Life", font=("Arial", 18, "bold"), justify=tk.CENTER)
        titulo_principal.pack(side=tk.TOP)
        titulo = tk.Label(self, text="Ingresa los siguientes datos", font=("Arial", 12), justify=tk.LEFT)
        titulo.pack(side=tk.TOP, fill=tk.BOTH)
        frame_general = tk.Frame(self, padx=20, pady=10)
        frame_general.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        frame_densidad = tk.Frame(frame_general, pady=0)
        frame_densidad.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self._txt_densidad = tk.Label(frame_densidad, text="Densidad", font=("Arial", 12), justify=tk.CENTER)
        self._txt_densidad.pack(side=tk.LEFT, fill=tk.X, expand=False)
        self.entry_densidad = tk.Entry(frame_densidad)
        self.entry_densidad.pack(side=tk.RIGHT, fill=tk.X, expand=True)

        frame_generaciones = tk.Frame(frame_general, pady=0)
        frame_generaciones.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self._txt_generaciones = tk.Label(frame_generaciones, text="Generaciones", font=("Arial", 12), justify=tk.CENTER)
        self._txt_generaciones.pack(side=tk.LEFT, fill=tk.X, expand=False)
        self.entry_generaciones = tk.Entry(frame_generaciones)
        self.entry_generaciones.pack(side=tk.RIGHT, fill=tk.X, expand=True)

        frame_botones = tk.Frame(frame_general, pady=0)
        frame_botones.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        frame_aceptar = tk.Frame(frame_general, padx=10, pady=5)
        frame_aceptar.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        frame_cancelar = tk.Frame(frame_general, padx=10, pady=5)
        frame_cancelar.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self._btn_aceptar = tk.Button(frame_aceptar, text="Aceptar", command=self.on_btn_aceptar, padx=10, pady=5)
        self._btn_aceptar.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self._btn_cancelar = tk.Button(frame_cancelar, text="Cancelar", command=self.on_btn_cancelar, padx=10, pady=5)
        self._btn_cancelar.pack(side=tk.LEFT, fill=tk.X, expand=True)

    def on_btn_aceptar(self):
        densidad: float = 0.0
        generaciones: int = 0
        error: str = ""
        try:
            densidad = float(self.entry_densidad.get())
            self._densidad = densidad
        except Exception as e:
            print(f"Error: {e}")
            error += f"\nDensidad invalida: {self.entry_densidad.get()}"
        try:
            generaciones = int(self.entry_generaciones.get())
            self._generaciones = generaciones
        except Exception as e:
            print(f"Error: {e}")
            error += f"\nGeneraciones invalida: {self.entry_generaciones.get()}"
        if not error:
            self.quit()
        else:
            Mensaje.mensaje_error("Error", f"Errores:{error}")

    def on_btn_cancelar(self):
        self.quit()

    def mostrar(self):
        self.mainloop()
        # self.grab_set()  # Bloquea la interacción con otras ventanas
        # self.wait_window()  # Espera hasta que la ventana se cierre

    @property
    def densidad(self):
        return self._densidad

    @densidad.setter
    def densidad(self, densidad: float):
        self._densidad = densidad

    @property
    def generaciones(self):
        return self._generaciones

    @generaciones.setter
    def generaciones(self, generaciones: int):
        self._generaciones = generaciones


if __name__ == "__main__":
    datos = Entrada_Datos_UI()
    datos.mostrar()

    print(f"densidad: {datos.densidad}")
    print(f"generaciones: {datos.generaciones}")





