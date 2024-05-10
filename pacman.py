import pygame
from pygame.locals import *
import heapq

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
CELL_SIZE = 40
FPS = 100

# Tamanho do labirinto (largura x altura)
LABYRINTH_WIDTH = 20
LABYRINTH_HEIGHT = 15

clock = pygame.time.Clock()

pygame.init()

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Pac-Man")

def carregar_labirinto(nivel):
    if nivel == 1:
        labirinto = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 1],
            [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1],
            [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1],
            [1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1],
            [1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
            [1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1],
            [1, 2, 1, 0, 1, 1, 1, 1, 2, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
            [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1],
            [1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
            [1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 2, 0, 0, 1],
            [1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
            [1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        ]
    elif nivel == 2:
        labirinto = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1],
            [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
            [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 2, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        ]
    elif nivel == 3:
        labirinto = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
            [1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 2, 0, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
            [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1],
            [1, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
            [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 2, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1],
            [1, 0, 0, 0, 1, 2, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1],
            [1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 2, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]
    return labirinto

LABYRINTH = carregar_labirinto(1)

class PacMan:
    def __init__(self):

        self.x = 40
        self.y = 40
        self.velocidade = 2
        self.direcao = 0
        self.image = pygame.image.load('pacman.png')
        self.image = pygame.transform.scale(self.image, (CELL_SIZE, CELL_SIZE))
        self.rect = pygame.Rect(self.x, self.y, CELL_SIZE, CELL_SIZE)

    def mover(self, keys):
        # Movimento do Pac-Man
        if keys[K_LEFT]:
            self.direcao = 1
        elif keys[K_RIGHT]:
            self.direcao = 2
        elif keys[K_UP]:
            self.direcao = 3
        elif keys[K_DOWN]:
            self.direcao = 4

        if self.direcao == 1:
            novo_x = self.x - self.velocidade
            if not colisao_parede(novo_x, self.y):
                self.x = novo_x
        elif self.direcao == 2:
            novo_x = self.x + self.velocidade
            if not colisao_parede(novo_x + CELL_SIZE - 1, self.y):
                self.x = novo_x
        elif self.direcao == 3:
            novo_y = self.y - self.velocidade
            if not colisao_parede(self.x, novo_y):
                self.y = novo_y
        elif self.direcao == 4:
            novo_y = self.y + self.velocidade
            if not colisao_parede(self.x, novo_y + CELL_SIZE - 1):
                self.y = novo_y

        self.rect.x = self.x
        self.rect.y = self.y

    def desenhar(self):
        screen.blit(self.image, (self.x, self.y))

def manhattan(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

# Função para encontrar o caminho usando o algoritmo A*
def a_estrela(labirinto, inicial, final):
    rows, cols = len(labirinto), len(labirinto[0])
    open_list = []
    heapq.heappush(open_list, (0, inicial))
    came_from = {}
    g_score = {tuple(inicial): 0}
    
    while open_list:
        current_cost, current_node = heapq.heappop(open_list)
        current_node = tuple(current_node)
        
        if current_node == final:
            path = []
            while current_node in came_from:
                path.append(current_node)
                current_node = came_from[current_node]
            path.append(tuple(inicial))
            path.reverse()
            return path
        
        for dx, dy in [(40, 0), (-40, 0), (0, 40), (0, -40)]:
            vizinho = (current_node[0] + dx, current_node[1] + dy)
            
            if (0 <= vizinho[0] < rows) and (0 <= vizinho[1] < cols) and labirinto[vizinho[0]][vizinho[1]] == 0:
                tentative_g_score = g_score[current_node] + 1
                if vizinho not in g_score or tentative_g_score < g_score[vizinho]:
                    came_from[vizinho] = current_node
                    g_score[vizinho] = tentative_g_score
                    f_score = tentative_g_score + manhattan(vizinho, final)
                    heapq.heappush(open_list, (f_score, vizinho))
    
    return None

class Fantasma:
    def __init__(self, nome, x, y):
        self.x = x
        self.y = y
        self.x_inicial = x
        self.y_inicial = y
        self.assustado = False
        self.velocidade = 1
        if(nome == "blinky"):
            self.velocidade = 1.5
        self.direcao = 0
        self.nome = nome
        self.image = pygame.image.load(nome + '.png')
        self.image = pygame.transform.scale(self.image, (CELL_SIZE, CELL_SIZE))
        self.rect = pygame.Rect(self.x, self.y, CELL_SIZE, CELL_SIZE)

    # Movimento do fantasma
    def mover(self, pacman_x, pacman_y):

        # Busca gulosa e distancia Euclidiana
        if(self.nome == "blinky" or self.nome == "clyde"):
            if self.assustado:
                self.voltar_inicio()
            else:
                if self.x < pacman_x:
                    novo_x = self.x + self.velocidade
                    if not colisao_parede(novo_x + CELL_SIZE - 1, self.y):
                        self.x = novo_x
                elif self.x > pacman_x:
                    novo_x = self.x - self.velocidade
                    if not colisao_parede(novo_x, self.y):
                        self.x = novo_x

                if self.y < pacman_y:
                    novo_y = self.y + self.velocidade
                    if not colisao_parede(self.x, novo_y + CELL_SIZE - 1):
                        self.y = novo_y
                elif self.y > pacman_y:
                    novo_y = self.y - self.velocidade
                    if not colisao_parede(self.x, novo_y):
                        self.y = novo_y
                
                if(self.nome == "clyde" ):
                    if(
                        self.x == pacman_x + 10
                        or self.x == pacman_x - 10
                        or self.y == pacman_y + 10
                        or self.y == pacman_y - 10
                    ):
                        self.assustado = True
            
        # A* e busca de Manhattan
        elif(self.nome == "pinky" or self.nome == "inky"):
            novo_x = self.x
            novo_y = self.y
            inicial = [self.x, self.y]
            final = [pacman_x + CELL_SIZE, pacman_y]
            caminho = a_estrela(LABYRINTH, inicial, final)
            if caminho:
                novo_x = caminho[1][0]
                novo_y = caminho [1][1]
            
            else:
                if self.x < pacman_x:
                    novo_x = self.x + self.velocidade
                elif self.x > pacman_x:
                    novo_x = self.x - self.velocidade
                if self.y < pacman_y:
                    novo_y = self.y + self.velocidade
                elif self.y > pacman_y:
                    novo_y = self.y - self.velocidade

            if novo_x == self.x:
                if novo_y > self.y:
                    novo_y = self.y + self.velocidade
                    if not colisao_parede(self.x, novo_y + CELL_SIZE - 1):
                        self.y = novo_y
                else:
                    novo_y = self.y - self.velocidade
                    if not colisao_parede(self.x, novo_y):
                        self.y = novo_y
            else:
                if novo_x < self.x:
                    novo_x = self.x - self.velocidade
                    if not colisao_parede(novo_x, self.y):
                        self.x = novo_x
                else:
                    novo_x = self.x + self.velocidade
                    if not colisao_parede(novo_x + CELL_SIZE - 1, self.y):
                        self.x = novo_x

    def voltar_inicio(self):
        if (self.x == self.x_inicial
            and self.y == self.y_inicial):
            self.assustado = False
        if self.x < self.x_inicial:
            novo_x = self.x + self.velocidade
            if not colisao_parede(novo_x + CELL_SIZE - 1, self.y):
                self.x = novo_x
        elif self.x > self.x_inicial:
            novo_x = self.x - self.velocidade
            if not colisao_parede(novo_x, self.y):
                self.x = novo_x

        if self.y < self.y_inicial:
            novo_y = self.y + self.velocidade
            if not colisao_parede(self.x, novo_y + CELL_SIZE - 1):
                self.y = novo_y
            elif self.y > self.y_inicial:
                novo_y = self.y - self.velocidade
                if not colisao_parede(self.x, novo_y):
                    self.y = novo_y

    def desenhar(self):
        screen.blit(self.image, (self.x, self.y))

def proximonivel():
    global nivel
    global LABYRINTH
    global pacman
    global fantasmas
    global pontuacao
    global tempo_invisivel
    global fantasmas_visiveis
    global total_de_frutinhas
    global dot_matrix

    pygame.init()
    pygame.display.set_caption("Pac-Man")

    pacman = PacMan()
    fantasmas = [Fantasma("blinky", 200, 200), Fantasma("clyde", 440, 200), Fantasma("inky", 480, 200), Fantasma("pinky", 240, 200)]
    tempo_invisivel = 0
    fantasmas_visiveis = True

    if nivel == 1:
        LABYRINTH = carregar_labirinto(1)

    elif nivel == 2:
        LABYRINTH = carregar_labirinto(2)

    elif nivel == 3:
        LABYRINTH = carregar_labirinto(3) 

    else:
        nivel = 1
        LABYRINTH = carregar_labirinto(1)  # Reinicia o jogo se não houver mais níveis
    
    total_de_frutinhas = sum(row.count(0) for row in LABYRINTH)
    total_de_frutinhas += LABYRINTH.count(2)
    3

    dot_matrix = [[0 for _ in range(20)] for _ in range(15)]
    for row in range(len(LABYRINTH)):
        for col in range(len(LABYRINTH[row])):
            if LABYRINTH[row][col] == 0:
                dot_matrix[row][col] = 1
    
    loopprincipal(True)

def tela_vitoria():
    font = pygame.font.Font(None, 36)
    game_win_text = font.render("Você venceu!", True, (255, 255, 255))
    score_text = font.render("Pontuação: " + str(pontuacao), True, (255, 255, 255))
    next_text = font.render("Pressione 'C' para continuar", True, (255, 255, 255))
    quit_text = font.render("Pressione 'S' para sair", True, (255, 255, 255))

    game_win_rect = game_win_text.get_rect()
    score_rect = score_text.get_rect()
    next_rect = next_text.get_rect()
    quit_rect = quit_text.get_rect()

    game_win_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 50)
    score_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
    next_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 50)
    quit_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 100)

    screen.fill((0, 0, 255))
    screen.blit(game_win_text, game_win_rect)
    screen.blit(score_text, score_rect)
    screen.blit(next_text, next_rect)
    screen.blit(quit_text, quit_rect)

    pygame.display.flip()

def tela_gameover(pontuacao):
    font = pygame.font.Font(None, 36)

    game_over_text = font.render("Game Over", True, (255, 255, 255))
    score_text = font.render("Pontuação: " + str(pontuacao), True, (255, 255, 255))
    restart_text = font.render("Pressione 'R' para reiniciar", True, (255, 255, 255))
    quit_text = font.render("Pressione 'S' para sair", True, (255, 255, 255))

    game_over_rect = game_over_text.get_rect()
    score_rect = score_text.get_rect()
    restart_rect = restart_text.get_rect()
    quit_rect = quit_text.get_rect()

    game_over_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 50)
    score_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
    restart_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 50)
    quit_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 100)

    screen.fill((0, 0, 0))

    screen.blit(game_over_text, game_over_rect)
    screen.blit(score_text, score_rect)
    screen.blit(restart_text, restart_rect)
    screen.blit(quit_text, quit_rect)

def desenhar_frutas():
    global pontuacao
    global tempo_invisivel
    global fantasmas_visiveis
    global total_de_frutinhas

    dot_radius = 3

    for row in range(len(dot_matrix)):
        for col in range(len(dot_matrix[row])):
            if dot_matrix[row][col] == 1:
                dot_x = col * CELL_SIZE + CELL_SIZE // 2
                dot_y = row * CELL_SIZE + CELL_SIZE // 2

                pygame.draw.circle(screen, (255, 255, 255), (dot_x, dot_y), dot_radius)

                # Verifica colisão com o Pac-Man e remove a bolinha se houver
                pacman.rect = pygame.Rect(pacman.x, pacman.y, CELL_SIZE, CELL_SIZE)
                dot_rect = pygame.Rect(dot_x - dot_radius, dot_y - dot_radius, 2 * dot_radius, 2 * dot_radius)
                
                if pacman.rect.colliderect(dot_rect):
                    dot_matrix[row][col] = 0  # Remove a bolinha
                    pontuacao += 10
                    total_de_frutinhas -= 1

    for row in range(len(LABYRINTH)):
        for col in range(len(LABYRINTH[row])):
            if LABYRINTH[row][col] == 2:
                fruit_x = col * CELL_SIZE + CELL_SIZE // 2
                fruit_y = row * CELL_SIZE + CELL_SIZE // 2
                pygame.draw.circle(screen, (255, 0, 0), (fruit_x, fruit_y), 6)  # Desenha frutinhas bônus

                if (
                    pacman.x < fruit_x + 6
                    and pacman.x + CELL_SIZE > fruit_x - 6
                    and pacman.y < fruit_y + 6
                    and pacman.y + CELL_SIZE > fruit_y - 6
                ):
                    LABYRINTH[row][col] = 0  # Remove a frutinha bônus
                    fantasmas_visiveis = False
                    tempo_invisivel = 10 * FPS
                    total_de_frutinhas -= 1

def desenhar_labirinto():
    for y, row in enumerate(LABYRINTH):
        for x, cell in enumerate(row):
            if cell == 1:
                pygame.draw.rect(screen, (0, 0, 255), (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def colisao_parede(x, y):
    cell_x = int(x / CELL_SIZE)  
    cell_y = int(y / CELL_SIZE) 

    if cell_x < 0 or cell_x >= LABYRINTH_WIDTH or cell_y < 0 or cell_y >= LABYRINTH_HEIGHT:
        return True

    return LABYRINTH[cell_y][cell_x] == 1

def loopprincipal(running):
    global game_over
    global fantasmas_visiveis
    global tempo_invisivel
    global nivel
    global total_de_frutinhas
    global pontuacao

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        keys = pygame.key.get_pressed()
        pacman.mover(keys)

        # Verifica colisão com os fantasmas
        for i in range(len(fantasmas)):
            if (
                pacman.x < fantasmas[i].x + CELL_SIZE
                and pacman.x + CELL_SIZE > fantasmas[i].x
                and pacman.y < fantasmas[i].y + CELL_SIZE
                and pacman.y + CELL_SIZE > fantasmas[i].y
                and fantasmas_visiveis
            ):
                game_over = True

        for i in range(len(fantasmas)):
            if fantasmas_visiveis:
                fantasmas[i].mover(pacman.x, pacman.y)

        if total_de_frutinhas == -5:
            game_over = True

        # Verifica se o jogo terminou
        if game_over:
            if total_de_frutinhas == -5:
                tela_vitoria()
                if keys[pygame.K_c]:
                    game_over = False
                    nivel += 1
                    proximonivel()
                elif keys[pygame.K_s]:
                    pygame.quit()
            else:
                tela_gameover(pontuacao)
                if keys[pygame.K_r]:
                    game_over = False
                    nivel = 1
                    pontuacao = 0
                    proximonivel()
                elif keys[pygame.K_s]:
                    pygame.quit()
            pygame.display.flip()
        
        else:
            screen.fill((0, 0, 0))
            desenhar_frutas()
            desenhar_labirinto()
            pacman.desenhar()
            texto_pontuacao = font.render(f'Pontuação: {pontuacao}', True, (255, 255, 255))
            screen.blit(texto_pontuacao, (10, 10))

            if not fantasmas_visiveis:
                tempo_invisivel -= 1

            if tempo_invisivel <= 0:
                fantasmas_visiveis = True

            if fantasmas_visiveis:
                for i in range(len(fantasmas)):
                    fantasmas[i].desenhar()

            pygame.display.flip()

        clock.tick(FPS)

game_over = False

total_de_frutinhas = sum(row.count(0) for row in LABYRINTH)  # Conta os espaços vazios (bolinhas brancas)
total_de_frutinhas += LABYRINTH.count(2)  # Conta as frutinhas bônus

pygame.font.init()
font = pygame.font.Font(None, 36)

pacman = PacMan()
fantasmas = [Fantasma("blinky", 200, 200), Fantasma("clyde", 440, 200), Fantasma("inky", 480, 200), Fantasma("pinky", 240, 200)]
pontuacao = 0
tempo_invisivel = 0
fantasmas_visiveis = True
nivel = 1
carregar_labirinto(1)
dot_matrix = [[0 for _ in range(20)] for _ in range(15)]
# Preencha a matriz das bolinhas brancas com 1 nos espaços vazios do labirinto
for row in range(len(LABYRINTH)):
    for col in range(len(LABYRINTH[row])):
        if LABYRINTH[row][col] == 0:
            dot_matrix[row][col] = 1
loopprincipal(True)

pygame.quit()