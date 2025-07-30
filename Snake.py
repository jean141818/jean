import pygame
import time
import random

# Inicializar pygame
pygame.init()

# Definir colores
blanco = (255, 255, 255)
amarillo = (255, 255, 102)
negro = (0, 0, 0)
rojo = (213, 50, 80)
verde = (0, 255, 0)
azul = (50, 153, 213)

# Dimensiones de la pantalla
ancho_pantalla = 800
alto_pantalla = 600

# Inicializar pantalla
pantalla = pygame.display.set_mode((ancho_pantalla, alto_pantalla))
pygame.display.set_caption('Juego de la Serpiente')

# Reloj para controlar la velocidad del juego
reloj = pygame.time.Clock()

# Tamaño de los bloques de la serpiente y velocidad
tamano_bloque = 20
velocidad_serpiente = 15

# Fuentes
fuente_estilo = pygame.font.SysFont("bahnschrift", 25)
fuente_puntos = pygame.font.SysFont("comicsansms", 35)

# Función para mostrar los puntos
def mostrar_puntos(puntos):
    valor = fuente_puntos.render("Tus Puntos: " + str(puntos), True, amarillo)
    pantalla.blit(valor, [0, 0])

# Función para dibujar la serpiente
def dibujar_serpiente(tamano_bloque, lista_serpiente):
    for bloque in lista_serpiente:
        pygame.draw.rect(pantalla, verde, [bloque[0], bloque[1], tamano_bloque, tamano_bloque])

# Función para mostrar mensajes
def mensaje(msg, color):
    mesg = fuente_estilo.render(msg, True, color)
    pantalla.blit(mesg, [ancho_pantalla / 6, alto_pantalla / 3])

# Función principal del juego
def juego():
    game_over = False
    game_close = False

    # Posición inicial de la serpiente
    x1 = ancho_pantalla / 2
    y1 = alto_pantalla / 2

    # Cambio de posición
    x1_cambio = 0
    y1_cambio = 0

    # Cuerpo de la serpiente
    lista_serpiente = []
    largo_serpiente = 1

    # Posición de la comida
    comida_x = round(random.randrange(0, ancho_pantalla - tamano_bloque) / 20.0) * 20.0
    comida_y = round(random.randrange(0, alto_pantalla - tamano_bloque) / 20.0) * 20.0

    while not game_over:

        while game_close == True:
            pantalla.fill(azul)
            mensaje("¡Perdiste! Presiona Q-Salir o C-Jugar de nuevo", rojo)
            mostrar_puntos(largo_serpiente - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        juego()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_cambio = -tamano_bloque
                    y1_cambio = 0
                elif event.key == pygame.K_RIGHT:
                    x1_cambio = tamano_bloque
                    y1_cambio = 0
                elif event.key == pygame.K_UP:
                    y1_cambio = -tamano_bloque
                    x1_cambio = 0
                elif event.key == pygame.K_DOWN:
                    y1_cambio = tamano_bloque
                    x1_cambio = 0

        # Si choca con los bordes
        if x1 >= ancho_pantalla or x1 < 0 or y1 >= alto_pantalla or y1 < 0:
            game_close = True

        x1 += x1_cambio
        y1 += y1_cambio
        pantalla.fill(negro)
        
        # Dibujar comida
        pygame.draw.rect(pantalla, rojo, [comida_x, comida_y, tamano_bloque, tamano_bloque])
        
        # Actualizar posición de la serpiente
        cabeza_serpiente = []
        cabeza_serpiente.append(x1)
        cabeza_serpiente.append(y1)
        lista_serpiente.append(cabeza_serpiente)
        
        # Eliminar bloques extras si no ha comido
        if len(lista_serpiente) > largo_serpiente:
            del lista_serpiente[0]

        # Si choca consigo misma
        for bloque in lista_serpiente[:-1]:
            if bloque == cabeza_serpiente:
                game_close = True

        dibujar_serpiente(tamano_bloque, lista_serpiente)
        mostrar_puntos(largo_serpiente - 1)

        pygame.display.update()

        # Si come la comida
        if x1 == comida_x and y1 == comida_y:
            comida_x = round(random.randrange(0, ancho_pantalla - tamano_bloque) / 20.0) * 20.0
            comida_y = round(random.randrange(0, alto_pantalla - tamano_bloque) / 20.0) * 20.0
            largo_serpiente += 1

        reloj.tick(velocidad_serpiente)

    pygame.quit()
    quit()

# Iniciar el juego
juego()


