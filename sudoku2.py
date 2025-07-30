def mostrar_tablero(tablero):
    """Muestra el tablero de Sudoku en la consola."""
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - -")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("| ", end="")
            print(tablero[i][j] if tablero[i][j] != 0 else ".", end=" ")
        print()

def encontrar_vacio(tablero):
    """Encuentra la próxima casilla vacía (representada por 0)."""
    for i in range(9):
        for j in range(9):
            if tablero[i][j] == 0:
                return (i, j)  # Devuelve (fila, columna)
    return None  # Si no hay casillas vacías

def es_valido(tablero, num, pos):
    """Verifica si un número es válido en una posición dada."""
    # Verificar fila
    if num in tablero[pos[0]]:
        return False
    
    # Verificar columna
    for i in range(9):
        if tablero[i][pos[1]] == num:
            return False
    
    # Verificar subcuadrícula 3x3
    sub_x = pos[1] // 3
    sub_y = pos[0] // 3
    for i in range(sub_y * 3, sub_y * 3 + 3):
        for j in range(sub_x * 3, sub_x * 3 + 3):
            if tablero[i][j] == num and (i, j) != pos:
                return False
    return True

def resolver(tablero):
    """Resuelve el Sudoku usando backtracking."""
    vacio = encontrar_vacio(tablero)
    if not vacio:
        return True  # ¡Tablero resuelto!
    fila, col = vacio
    
    for num in range(1, 10):
        if es_valido(tablero, num, (fila, col)):
            tablero[fila][col] = num
            if resolver(tablero):
                return True
            tablero[fila][col] = 0  # Retroceder si no lleva a una solución
    return False

def jugar():
    """Función principal para jugar al Sudoku."""
    # Tablero inicial (0 = casilla vacía)
    tablero = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    
    print("¡Bienvenido al Sudoku!")
    while True:
        mostrar_tablero(tablero)
        vacio = encontrar_vacio(tablero)
        if not vacio:
            print("¡Felicidades! ¡Has resuelto el Sudoku!")
            break
        
        try:
            fila = int(input("Ingresa la fila (1-9): ")) - 1
            col = int(input("Ingresa la columna (1-9): ")) - 1
            num = int(input("Ingresa el número (1-9): "))
            
            if fila not in range(9) or col not in range(9) or num not in range(1, 10):
                print("Entrada inválida. Usa números del 1 al 9.")
                continue
            
            if tablero[fila][col] != 0:
                print("¡Esa casilla ya está ocupada!")
                continue
            
            if es_valido(tablero, num, (fila, col)):
                tablero[fila][col] = num
            else:
                print("¡Movimiento inválido! Violación de las reglas del Sudoku.")
        except ValueError:
            print("Entrada inválida. Ingresa solo números.")

if __name__ == "__main__":
    jugar()