import numpy as np

class Matriz():

    @staticmethod
    def llenar_matriz(densidad: float, filas: int, columnas: int):
        matriz = []
        for fila in range(filas):
            fila_valores = []
            for columna in range(columnas):
                num_aleatorio = np.random.rand(1)
                if num_aleatorio[0] < densidad:
                    fila_valores.append(1)
                else:
                    fila_valores.append(0)
            matriz.append(fila_valores)
        return matriz

    @staticmethod
    def imprimir_matriz(matriz):
        for fila in matriz:
            print(fila)

if __name__ == "__main__":
    matriz = Matriz.llenar_matriz(.50, 10, 10)
    Matriz.imprimir_matriz(matriz)
