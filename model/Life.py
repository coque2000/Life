from util.Generar_Matriz import Matriz

class Life:
    def __init__(self, matriz:list, generaciones: int):
        self._generaciones = generaciones
        self._generacion = 0
        self._matriz_actual = matriz
        self._matriz_anterior = self._matriz_actual

    @property
    def generacion(self):
        return self._generacion

    @generacion.setter
    def generacion(self, generacion):
        self._generacion = generacion

    @property
    def generaciones(self):
        return self._generaciones

    @generaciones.setter
    def generaciones(self, generaciones):
        self._generaciones = generaciones

    @property
    def matriz_actual(self):
        return self._matriz_actual

    @matriz_actual.setter
    def matriz_actual(self, matriz):
        self._matriz_actual = matriz

    @property
    def matriz_anterior(self):
        return self._matriz_anterior

    @matriz_anterior.setter
    def matriz_anterior(self, matriz_anterior):
        self._matriz_anterior = matriz_anterior

    def calcular_vecinos_cercanos(self, matriz, fila, columna):
        filas = len(matriz)
        columnas = len(matriz[0])
        # Definir las 8 direcciones posibles de los vecinos (arriba, abajo, izquierda, derecha y las 4 diagonales)
        direcciones = [
            (-1, 0), (1, 0), (0, -1), (0, 1),  # arriba, abajo, izquierda, derecha
            (-1, -1), (-1, 1), (1, -1), (1, 1)  # diagonales
        ]
        vecinos = []
        for d_fila, d_col in direcciones:
            # Calculamos la nueva fila y columna considerando el mundo envolvente
            nueva_fila = (fila + d_fila) % filas
            nueva_col = (columna + d_col) % columnas
            vecinos.append(self._matriz_actual[nueva_fila][nueva_col])
            # Retorna la suma suponiendo que solo hay valores de 1 y 0
        # print(f"Vecinos de {fila}*{col}: {vecinos}")
        return sum(vecinos)

    def siguiente_generacion(self):
        filas = len(self._matriz_actual)
        columnas = len(self._matriz_actual[0])
        siguiente_generacion = [[0 for _ in range(columnas)] for _ in range(filas)]  # Inicializar con ceros

        for i in range(len(self._matriz_actual)):  # Recorre las filas
            for j in range(len(self._matriz_actual[i])):  # Recorre las columnas
                # Si el elemento es 1
                valor = self._matriz_actual[i][j]
                if valor == 1:
                    # Calcular vecinos cercanos
                    if 2 <= self.calcular_vecinos_cercanos(self._matriz_actual, i, j) <= 3:
                        siguiente_generacion[i][j] = 1
                    else:
                        # Si la celda es cero
                        siguiente_generacion[i][j] = 0
                # Suponiendo que solo hay 0 o 1
                else:
                    # print(f"{i}*{j}: {calcular_vecinos_cercanos(matriz, i, j)}")
                    if self.calcular_vecinos_cercanos(self._matriz_actual, i, j) == 3:
                        siguiente_generacion[i][j] = 1
                    else:
                        siguiente_generacion[i][j] = 0
        self._generacion += 1
        self._matriz_anterior = self._matriz_actual
        self._matriz_actual = siguiente_generacion
        return self._matriz_actual

    def jugar(self):
        Matriz.imprimir_matriz(self._matriz_actual)
        for i in range(self._generaciones):
            self.siguiente_generacion()
            print("\n")
            print(f"Generacion {i + 1}")
            Matriz.imprimir_matriz(self._matriz_actual)

if __name__ == "__main__":
    # matriz = Matriz.llenar_matriz(.5, 10, 10)
    matriz = [[0, 0, 1, 1, 1],
            [1, 1, 0, 1, 0],
            [0, 0, 1, 1, 0],
            [0, 1, 1, 0, 0],
            [1, 1, 0, 1, 0]]
    life = Life(matriz, 5)
    life.jugar()
    # Matriz.imprimir_matriz(life.matriz_anterior)
    # Matriz.imprimir_matriz(life.matriz_actual)
    # print("\n")
