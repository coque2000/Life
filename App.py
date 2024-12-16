from gui.Entrada_Datos_UI import Entrada_Datos_UI
from gui.Life_UI import Life_UI
#from algoritmos.life.gui.Mensaje import Mensaje
from gui.Mensaje import Mensaje
from util.Generar_Matriz import Matriz
from model.Life import Life

if __name__ == "__main__":
    datos = Entrada_Datos_UI()
    datos.mostrar()
    densidad = datos.densidad
    generaciones = datos.generaciones

    if densidad == 0 or generaciones == 0 or densidad == None or generaciones == None:
        print("Sin comenzar")
    elif not (densidad > 0 or generaciones > 0):
        Mensaje.mensaje_error("Datos no validos", "Los datos proporcionados no son validos")
    else:
        matriz: list = Matriz.llenar_matriz(densidad=densidad, filas=60, columnas=100)
        life_game = Life(matriz=matriz, generaciones=generaciones)
        life_ui = Life_UI(matriz=matriz, escala=10, retraso=0.1, life_game=life_game)
        life_ui.crear_interfaz()


