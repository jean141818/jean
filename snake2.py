import random
import time
import os
import msvcrt  # Solo para Windows (para lectura de teclas sin "Enter")

# Configuración del juego
ANCHO = 20
ALTO = 10
VELOCIDAD = 0.2

def limpiar_pantalla():
    """Limpia la pantalla de la consola."""
    os.system('cls' if os.name == 'nt' else 'clear')

def dibujar_mundo(serpiente, comida):
    """Dibuja el mundo del Snake en ASCII."""
    for y in range(ALTO):
        for x in range(ANCHO):
            if (x, y) == comida:
                print("🍎", end="")
            elif (x, y) in serpiente:
                print("🟢" if (x, y) == serpiente[0] else "🟩", end="")
            else:
                print("  ", end="")
        print()

def mover_serpiente(serpiente, direccion):
    """Mueve la serpiente en la dirección dada."""
    cabeza_x, cabeza_y = serpiente[0]
    if direccion == "ARRIBA":
        nueva_cabeza = (cabeza_x, cabeza_y - 1)
    elif direccion == "ABAJO":
        nueva_cabeza = (cabeza_x, cabeza_y + 1)
    elif direccion == "IZQUIERDA":
        nueva_cabeza = (cabeza_x - 1, cabeza_y)
    elif direccion == "DERECHA":
        nueva_cabeza = (cabeza_x + 1, cabeza_y)
    
    # Verificar colisión con bordes
    if (nueva_cabeza[0] < 0 or nueva_cabeza[0] >= ANCHO or 
        nueva_cabeza[1] < 0 or nueva_cabeza[1] >= ALTO):
        return None  # Game Over
    
    # Verificar colisión consigo misma
    if nueva_cabeza in serpiente:
        return None
    
    serpiente.insert(0, nueva_cabeza)
    return serpiente

def generar_comida(serpiente):
    """Genera comida en una posición aleatoria no ocupada por la serpiente."""
    while True:
        comida = (random.randint(0, ANCHO - 1), random.randint(0, ALTO - 1))
        if comida not in serpiente:
            return comida

def leer_tecla():
    """Lee una tecla sin necesidad de presionar Enter (solo Windows)."""
    if os.name == 'nt':
        try:
            tecla = msvcrt.getch().decode()
            if tecla == 'w':
                return "ARRIBA"
            elif tecla == 's':
                return "ABAJO"
            elif tecla == 'a':
                return "IZQUIERDA"
            elif tecla == 'd':
                return "DERECHA"
            elif tecla == 'q':
                return "SALIR"
        except:
            pass
    return None

def juego_snake_consola():
    """Función principal del juego Snake en consola."""
    serpiente = [(ANCHO // 2, ALTO // 2)]
    direccion = "DERECHA"
    comida = generar_comida(serpiente)
    puntuacion = 0
    
    print("¡Snake en Consola!")
    print("Controles: W (Arriba), S (Abajo), A (Izquierda), D (Derecha), Q (Salir)")
    time.sleep(2)
    
    while True:
        limpiar_pantalla()
        dibujar_mundo(serpiente, comida)
        print(f"Puntuación: {puntuacion}")
        
        # Leer tecla
        nueva_direccion = leer_tecla()
        if nueva_direccion == "SALIR":
            break
        if nueva_direccion:
            # Evitar movimiento inverso (ej: de derecha a izquierda)
            if not ((direccion == "ARRIBA" and nueva_direccion == "ABAJO") or
                   (direccion == "ABAJO" and nueva_direccion == "ARRIBA") or
                   (direccion == "IZQUIERDA" and nueva_direccion == "DERECHA") or
                   (direccion == "DERECHA" and nueva_direccion == "IZQUIERDA")):
                direccion = nueva_direccion
        
        # Mover serpiente
        nueva_serpiente = mover_serpiente(serpiente.copy(), direccion)
        if not nueva_serpiente:
            print("¡Game Over!")
            break
        serpiente = nueva_serpiente
        
        # Verificar si comió
        if serpiente[0] == comida:
            comida = generar_comida(serpiente)
            puntuacion += 1
        else:
            serpiente.pop()  # Quitar cola si no comió
        
        time.sleep(VELOCIDAD)

if __name__ == "__main__":
    juego_snake_consola()