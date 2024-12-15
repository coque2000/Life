import pygame
import sys
import time
import random

class Life_UI():
    def __init__(self, matriz=None, escala: int = 2, retraso: float = 0):
        self._matriz =  matriz if matriz else []
        self._escala = escala
        self._retraso = retraso
        # Filas y columnas
        self._filas = len(self._matriz)  # Numero de filas
        self._columnas = len(self._matriz[0]) if self._filas > 0 else 0  # Numero de columnas
        # Tamanio ventana
        self._height = self._filas * self._escala
        self._width = self._columnas * self._escala
        # print(f"height: {self._height}")
        # print(f"width: {self._width}")
        # Colores
        self._color_fondo = (0, 0, 0)  # Color de fondo de la ventana (negro)
        self._color_celda_iluminada = (100, 200, 255)  # Celda "encendida" (azul)
        self._color_celda_apagada = (0, 0, 0)  # Celda "apagada" (gris)

        # Incializar interfaz
        pygame.init()
        self._pantalla = pygame.display.set_mode((self._width, self._height))
        pygame.display.set_caption(f"Life")
        self._generacion = 0

        # self.crear_interfaz()

    @property
    def matriz(self):
        return self._matriz

    @matriz.setter
    def matriz(self, matriz: list):
        self._matriz = matriz
        self._filas = len(matriz)
        self._columnas = len(matriz[0]) if self._filas > 0 else 0
        self._height = self._filas * self._escala
        self._width = self._columnas * self._escala

    @property
    def escala(self):
        return self._escala

    @escala.setter
    def escala(self, escala: int):
        self._escala = escala

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        self._width = width

    @property
    def color_fondo(self):
        return self._color_fondo

    @color_fondo.setter
    def color_fondo(self, color_fondo):
        self._color_fondo = color_fondo

    @property
    def color_celda_iluminada(self):
        return self._color_celda_iluminada

    @color_celda_iluminada.setter
    def color_celda_iluminada(self, color_celda_iluminada):
        self._color_celda_iluminada = color_celda_iluminada

    @property
    def color_celda_apagada(self):
        return self._color_celda_apagada

    @color_celda_apagada.setter
    def color_celda_apagada(self, color_celda_apagada):
        self._color_celda_apagada = color_celda_apagada

    def crear_interfaz(self):
        corriendo = True
        while corriendo:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    corriendo = False

            # Actualiza la matriz y redibuja la interfaz
            self._actualizar_estado()
            self._dibujar_interfaz()
            time.sleep(self._retraso)  # Pausa para controlar la velocidad de actualización

        pygame.quit()
        sys.exit()

    def _dibujar_interfaz(self):
        """Dibuja la interfaz gráfica según el estado actual de la matriz."""
        # Dibujar el fondo
        self._pantalla.fill(self._color_fondo)
        # Dibujar la cuadricula
        for fila in range(self._filas):
            for columna in range(self._columnas):
                x = columna * self._escala
                y = fila * self._escala
                color_celda = self._color_celda_iluminada if self._matriz[fila][columna] else self._color_celda_apagada
                pygame.draw.rect(self._pantalla, color_celda, (x, y, self._escala, self._escala))
        # Actualizar la pantalla
        pygame.display.flip()

    def actualizar_pixel(self, fila: int, columna: int, valor: int):
        """
        Actualiza un pixel de in matriz, cambia la interfaz debido a que se encuentra en ejecucion
        :param x:
        :param y:
        :param valor: 0 o 1
        :return: None
        """
        if 0 <= fila < self._filas and 0 <= columna < self._columnas:
            self._matriz[fila][columna] = valor
        else:
            print(f"Coordenadas fuera de rango: ({fila}, {columna})")

    def _actualizar_estado(self):

        nueva_matriz = [[0 for _ in range(self._columnas)] for _ in range(self._filas)]

        for fila in range(self._filas):
            for columna in range(self._columnas):


                # Implementar reglas aquí
                # nueva_matriz[fila][columna] = self._matriz[fila][columna]  # Ejemplo

                nueva_matriz[fila][columna] = random.randint(0, 1)

        self._generacion += 1
        self._matriz = nueva_matriz

if __name__ == "__main__":
    # Matriz de ejemplo (0 = apagado, 1 = iluminado)
    matriz = [
        [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    ]


    life = Life_UI(matriz=matriz, escala=80, retraso=0.1)
    life.crear_interfaz()





