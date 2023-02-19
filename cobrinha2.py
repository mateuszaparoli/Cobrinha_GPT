import pygame
import time
import random

LARGURA_CANVAS = 600
ALTURA_CANVAS = 600

pygame.init()

# Definições do display
largura_tela = 1100
altura_tela = 600
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('Jogo da Cobrinha')

# Definições das cores
branco = (255, 255, 255)
preto = (0, 0, 0)
vermelho = (213, 50, 80)
verde = (0, 255, 0)

# Definições do relógio
clock = pygame.time.Clock()

# Definições da fonte
fonte_jogo = pygame.font.SysFont("bahnschrift", 25)
fonte_fim = pygame.font.SysFont("comicsansms", 45)

# Função para desenhar o texto
def texto(msg, cor):
    texto_tela = fonte_jogo.render(msg, True, cor)
    tela.blit(texto_tela, [largura_tela / 6, altura_tela / 3])

# Função do jogo
def jogo():
    # Definições iniciais da cobra
    cobra_pos = [100, 50]
    cobra_corpo = [[100, 50], [90, 50], [80, 50]]
    
    # Definições iniciais da comida
    comida_pos = [random.randrange(1, (largura_tela // 10)) * 10, 
                  random.randrange(1, (altura_tela // 10)) * 10]
    comida_spawn = True
    
    # Definições iniciais do movimento da cobra
    direcao = 'RIGHT'
    mudar_direcao = direcao
    
    # Loop do jogo
    jogo_rodando = True
    while jogo_rodando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    mudar_direcao = 'LEFT'
                elif event.key == pygame.K_RIGHT:
                    mudar_direcao = 'RIGHT'
                elif event.key == pygame.K_UP:
                    mudar_direcao = 'UP'
                elif event.key == pygame.K_DOWN:
                    mudar_direcao = 'DOWN'
        
        # Mudança da direção da cobra
        if mudar_direcao == 'LEFT' and direcao != 'RIGHT':
            direcao = 'LEFT'
        elif mudar_direcao == 'RIGHT' and direcao != 'LEFT':
            direcao = 'RIGHT'
        elif mudar_direcao == 'UP' and direcao != 'DOWN':
            direcao = 'UP'
        elif mudar_direcao == 'DOWN' and direcao != 'UP':
            direcao = 'DOWN'
        
        # Movimento da cobra
        if direcao == 'LEFT':
            cobra_pos[0] -= 10
        elif direcao == 'RIGHT':
            cobra_pos[0] += 10
        elif direcao == 'UP':
            cobra_pos[1] -= 10
        elif direcao == 'DOWN':
            cobra_pos[1] += 10

        # Adição de segmento da cobra
        cobra_corpo.insert(0, list(cobra_pos))
        if cobra_pos == comida_pos:
            comida_spawn = False
        else:
            cobra_corpo.pop()

        # Respawn da comida
        if not comida_spawn:
            comida_pos = [random.randrange(1, (largura_tela // 10)) * 10, 
                          random.randrange(1, (altura_tela // 10)) * 10]
        comida_spawn = True
        
        # Preenchimento do background
        tela.fill(preto)
        
        # Desenho da cobra
        for pos in cobra_corpo:
            pygame.draw.rect(tela, verde, pygame.Rect(
                pos[0], pos[1], 10, 10))
        
        
        # Desenho da comida
        pygame.draw.rect(tela, vermelho, pygame.Rect(
            comida_pos[0], comida_pos[1], 10, 10))

        pygame.display.update()
        clock.tick(20)
        
        if cobra_pos[0] < 0 or cobra_pos[0] > largura_tela-10:
            fim_de_jogo()
        if cobra_pos[1] < 0 or cobra_pos[1] > altura_tela-10:
            fim_de_jogo()

        for bloco in cobra_corpo[1:]:
            if cobra_pos == bloco:
                fim_de_jogo()


def fim_de_jogo():
    # Loop do fim de jogo
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_r:
                    jogo()

        pygame.display.update()
        clock.tick(10)  # adicionado para evitar uso excessivo da CPU

        # Preenchimento do background
        tela.fill(preto)

        # Desenho da mensagem de fim de jogo
        texto("Fim de jogo! Pressione R para jogar novamente ou Q para sair",  vermelho)

jogo()