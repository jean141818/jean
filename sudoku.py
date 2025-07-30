import pygame
import random
import sys
import time

# Inicializar pygame
pygame.init()

# Constantes
WIDTH, HEIGHT = 540, 600
GRID_SIZE = 540
CELL_SIZE = GRID_SIZE // 9
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
LIGHT_BLUE = (173, 216, 230)
DARK_BLUE = (50, 50, 150)  # Color para números fijos
RED = (220, 0, 0)         # Color para números del usuario
GREEN = (0, 150, 0)       # Color para mensajes
HINT_COLOR = (0, 200, 0)  # Color para pistas

# Configuración de la ventana
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku")
font = pygame.font.SysFont('Arial', 40)
small_font = pygame.font.SysFont('Arial', 20)

class Sudoku:
    def __init__(self, difficulty=40):
        self.board = [[0 for _ in range(9)] for _ in range(9)]
        self.solution = [[0 for _ in range(9)] for _ in range(9)]
        self.fixed = [[False for _ in range(9)] for _ in range(9)]
        self.selected = None
        self.difficulty = difficulty
        self.generate_puzzle()
        self.start_time = time.time()
        self.end_time = None
        self.errors = 0
        self.completed = False
        
    def is_valid(self, row, col, num):
        # Verificar fila
        if num in self.board[row]:
            return False
        
        # Verificar columna
        for i in range(9):
            if self.board[i][col] == num:
                return False
        
        # Verificar cuadrante 3x3
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if self.board[i][j] == num:
                    return False
        
        return True
    
    def solve(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == 0:
                    for num in random.sample(range(1, 10), 9):  # Prueba números en orden aleatorio
                        if self.is_valid(row, col, num):
                            self.board[row][col] = num
                            if self.solve():
                                return True
                            self.board[row][col] = 0
                    return False
        return True
    
    def generate_puzzle(self):
        # Generar solución completa
        self.solve()
        self.solution = [row[:] for row in self.board]
        
        # Crear copia para el tablero de juego
        self.board = [row[:] for row in self.solution]
        
        # Eliminar celdas para crear el puzzle
        cells_to_remove = self.difficulty
        while cells_to_remove > 0:
            row, col = random.randint(0, 8), random.randint(0, 8)
            if self.board[row][col] != 0:  # Solo eliminar celdas que tengan números
                self.board[row][col] = 0
                self.fixed[row][col] = False  # Celda modificable
                cells_to_remove -= 1
        
        # Marcar las celdas restantes (con números) como fijas
        for row in range(9):
            for col in range(9):
                if self.board[row][col] != 0:
                    self.fixed[row][col] = True
    
    def draw(self):
        # Dibujar el tablero
        screen.fill(WHITE)
        
        # Dibujar las celdas
        for row in range(9):
            for col in range(9):
                rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(screen, WHITE, rect)
                pygame.draw.rect(screen, GRAY, rect, 1)
                
                # Dibujar números
                if self.board[row][col] != 0:
                    num_color = DARK_BLUE if self.fixed[row][col] else RED
                    num_text = font.render(str(self.board[row][col]), True, num_color)
                    screen.blit(num_text, (col * CELL_SIZE + CELL_SIZE // 3, 
                                    row * CELL_SIZE + CELL_SIZE // 6))
        
        # Dibujar líneas gruesas para los cuadrantes
        for i in range(0, 10, 3):
            pygame.draw.line(screen, BLACK, (0, i * CELL_SIZE), (GRID_SIZE, i * CELL_SIZE), 3)
            pygame.draw.line(screen, BLACK, (i * CELL_SIZE, 0), (i * CELL_SIZE, GRID_SIZE), 3)
        
        # Resaltar celda seleccionada
        if self.selected and not self.completed:  # No resaltar si el juego está completado
            row, col = self.selected
            if not self.fixed[row][col]:  # Solo resaltar si no es fija
                pygame.draw.rect(screen, LIGHT_BLUE, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE), 3)
        
        # Calcular tiempo transcurrido
        if self.completed:
            elapsed_time = self.end_time - self.start_time
        else:
            elapsed_time = time.time() - self.start_time
        
        # Dibujar información del juego
        time_text = small_font.render(f"Tiempo: {int(elapsed_time) // 60}:{int(elapsed_time) % 60:02d}", True, BLACK)
        errors_text = small_font.render(f"Errores: {self.errors}", True, BLACK)
        screen.blit(time_text, (10, GRID_SIZE + 10))
        screen.blit(errors_text, (10, GRID_SIZE + 40))
        
        # Dibujar instrucciones
        instructions = small_font.render("1-9: Insertar número | 0: Borrar | R: Reiniciar | N: Nuevo juego", True, BLACK)
        screen.blit(instructions, (10, GRID_SIZE + 70))
        
        # Mostrar mensaje de victoria
        if self.completed:
            message = f"¡Ganaste! Tiempo: {int(elapsed_time) // 60}:{int(elapsed_time) % 60:02d} | Errores: {self.errors}"
            text = font.render(message, True, GREEN)
            screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT - 50))
    
    def select(self, row, col):
        # No permitir seleccionar si el juego está completado
        if self.completed:
            return False
            
        # Permitir seleccionar cualquier celda vacía o no fija
        if not self.fixed[row][col]:
            self.selected = (row, col)
            return True
        return False
    
    def place_number(self, num):
        if self.completed:
            return
            
        if self.selected and not self.fixed[self.selected[0]][self.selected[1]]:
            row, col = self.selected
            
            # Verificar si el número es correcto
            if num != 0 and self.solution[row][col] != num:
                self.errors += 1
            
            self.board[row][col] = num
            
            # Verificar si el juego está completado
            if self.is_complete():
                self.completed = True
                self.end_time = time.time()
    
    def is_complete(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == 0 or (not self.fixed[row][col] and self.board[row][col] != self.solution[row][col]):
                    return False
        return True
    
    def reset(self):
        # Restablecer solo las celdas no fijas
        for row in range(9):
            for col in range(9):
                if not self.fixed[row][col]:
                    self.board[row][col] = 0
        self.errors = 0
        self.start_time = time.time()
        self.end_time = None
        self.selected = None
        self.completed = False

def main():
    game = Sudoku()
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_r:
                    game.reset()
                elif event.key == pygame.K_n:
                    game = Sudoku()
                elif game.selected and not game.completed:
                    if pygame.K_0 <= event.key <= pygame.K_9:
                        num = event.key - pygame.K_0
                        game.place_number(num)
                    elif pygame.K_KP0 <= event.key <= pygame.K_KP9:
                        num = event.key - pygame.K_KP0
                        game.place_number(num)
            
            if event.type == pygame.MOUSEBUTTONDOWN and not game.completed:
                pos = pygame.mouse.get_pos()
                if pos[0] < GRID_SIZE and pos[1] < GRID_SIZE:
                    row, col = pos[1] // CELL_SIZE, pos[0] // CELL_SIZE
                    game.select(row, col)
        
        game.draw()
        pygame.display.flip()
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()