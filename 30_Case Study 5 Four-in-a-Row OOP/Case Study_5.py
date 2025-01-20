from IPython.display import clear_output


class CuatroEnRaya:
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.tablero = self.crear_tablero()
        self.turno = None

    def crear_tablero(self):
        tablero = [None] * self.filas
        for f in range(self.filas):
            tablero[f] = ['.'] * self.columnas
        return tablero

    def mostrar_tablero(self):
        """
        Muestra el tablero por pantalla.
        """
        # Sacamos por pantalla la cabecera
        for num in range(self.columnas):
            print(num, end='  ')
        # Sacamos por pantalla el tablero
        for fila in self.tablero:
            print("")
            for casilla in fila:
                print(casilla, end="  ")

    def introducir_ficha(self, columna, color):
        # Introduce una ficha en el tablero indicado.
        if columna >= self.columnas or columna < 0:
            print("Error: número de columna fuera del rango.")
            return
        elif self.tablero[0][columna] != '.':
            print("Error: la columna está llena de fichas.")
            return
        else:
            for fila in range(self.filas - 1, -1, -1):
                if self.tablero[fila][columna] == '.':
                    self.tablero[fila][columna] = color
                    return

    def revisar_filas(self, color):
        # Recorremos las filas en busca de cuatro en raya.
        for r in range(self.filas):
            for c in range(self.columnas - 3):
                if self.tablero[r][c] == color and self.tablero[r][c + 1] == color and self.tablero[r][
                    c + 2] == color and self.tablero[r][c + 3] == color:
                    return True

    def revisar_columnas(self, color):
        # Recorremos las columnas en busca de cuatro en raya.
        for c in range(self.columnas):
            for r in range(self.filas - 3):
                if self.tablero[r][c] == color and self.tablero[r + 1][c] == color and self.tablero[r + 2][
                    c] == color and self.tablero[r + 3][c] == color:
                    return True

    def revisar_diagonal_derecha(self, color):
        # Recorremos las diagonales hacia la derecha en busca de cuatro en raya.
        for c in range(self.columnas - 3):
            for r in range(self.filas - 1, 2, -1):
                if self.tablero[r][c] == color and self.tablero[r - 1][c + 1] == color and self.tablero[r - 2][
                    c + 2] == color and self.tablero[r - 3][c + 3] == color:
                    return True

    def revisar_diagonal_izquierda(self, color):
        # Recorremos las diagonales hacia la izquierda en busca de cuatro en raya.
        for c in range(self.columnas - 1, 2, -1):
            for r in range(self.filas - 1, 2, -1):
                if self.tablero[r][c] == color and self.tablero[r - 1][c - 1] == color and self.tablero[r - 2][
                    c - 2] == color and self.tablero[r - 3][c - 3] == color:
                    return True

    def comprobar_ganador(self, color):
        # Comprueba si se ha producido un cuatro en raya.
        return self.revisar_filas(color) or self.revisar_columnas(color) or self.revisar_diagonal_derecha(
            color) or self.revisar_diagonal_izquierda(color)

    def jugar(self, player1='X', player2='O'):
        self.turno = player2
        while True:
            self.turno = player1 if self.turno == player2 else player2
            self.mostrar_tablero()
            columna = int(input("Turno del jugador {}:".format(self.turno)))
            self.introducir_ficha(columna, self.turno)
            clear_output(wait=False)
            if self.comprobar_ganador(self.turno):
                print("\n\n¡¡Ha ganado el jugador {}!!\n\n".format(self.turno))
                self.mostrar_tablero()
                break

Juego = CuatroEnRaya(6, 7)
Juego.jugar()