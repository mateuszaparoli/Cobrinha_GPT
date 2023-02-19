import pygame
import random

# Define as cores disponíveis no jogo
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]

# Inicializa o Pygame
pygame.init()

# Define o tamanho da janela
WINDOW_SIZE = (400, 400)

# Define o nome da janela
pygame.display.set_caption("Jogo de Memória")

# Cria a janela
screen = pygame.display.set_mode(WINDOW_SIZE)

# Define a fonte do texto
font = pygame.font.Font(None, 36)

# Define a sequência de cores para o usuário memorizar
sequence = []
for i in range(10):
    sequence.append(random.choice(colors))

# Define a variável que armazena a posição do usuário na sequência
user_index = 0

# Define a variável que armazena o resultado do jogo
game_over = False

# Loop principal do jogo
while not game_over:

    # Verifica se o usuário quer sair do jogo
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # Limpa a tela
    screen.fill((255, 255, 255))

    # Desenha as cores da sequência
    for i in range(len(sequence)):
        rect = pygame.Rect(50 + i * 50, 150, 50, 50)
        pygame.draw.rect(screen, sequence[i], rect)

    # Desenha o texto na tela
    text = font.render("Lembre-se da sequência e clique nas cores na ordem correta", True, (0, 0, 0))
    text_rect = text.get_rect(center=(200, 50))
    screen.blit(text, text_rect)

    # Verifica se o usuário clicou em uma cor
    mouse_pos = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()
    if mouse_pressed[0]:
        for i in range(len(sequence)):
            rect = pygame.Rect(50 + i * 50, 150, 50, 50)
            if rect.collidepoint(mouse_pos):
                # Verifica se o usuário acertou a cor
                if sequence[user_index] == colors[i]:
                    user_index += 1
                    if user_index == len(sequence):
                        # O usuário acertou a sequência inteira
                        user_index = 0
                        sequence.append(random.choice(colors))
                else:
                    # O usuário errou a sequência
                    user_index = 0
                    sequence = [random.choice(colors) for i in range(10)]

    # Atualiza a janela
    pygame.display.update()

# Finaliza o Pygame
pygame.quit()
