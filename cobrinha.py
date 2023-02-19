from tkinter import Canvas
import pygame
import time
import random
import tkinter as tk

LARGURA_CANVAS = 600
ALTURA_CANVAS = 600

pygame.init()

# Definições do display
largura_tela = 800
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
                jogo_rodando = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    jogo_rodando = False
                if event.key == pygame.K_LEFT:
                    mudar_direcao = 'LEFT'
                elif event.key == pygame.K_RIGHT:
                    mudar_direcao = 'RIGHT'
                elif event.key == pygame.K_UP:
                    mudar_direcao = 'UP'
                elif event.key == pygame.K_DOWN:
                    mudar_direcao = 'DOWN'
        
        # Verificação da mudança de direção da cobra
        if mudar_direcao == 'LEFT' and not direcao == 'RIGHT':
            direcao = 'LEFT'
        elif mudar_direcao == 'RIGHT' and not direcao == 'LEFT':
            direcao = 'RIGHT'
        elif mudar_direcao == 'UP' and not direcao == 'DOWN':
            direcao = 'UP'
        elif mudar_direcao == 'DOWN' and not direcao == 'UP':
            direcao = 'DOWN'
        
        # Movimentação da cobra
        if direcao == 'RIGHT':
            cobra_pos[0] += 10
        elif direcao == 'LEFT':
            cobra_pos[0] -= 10
        elif direcao == 'UP':
            cobra_pos[1] -= 10
        elif direcao == 'DOWN':
            cobra_pos[1] += 10

          # Adiciona o corpo da cobra
    cobra_corpo = []
    for i in range(3):
        cobra_celula = Canvas.create_rectangle(25+i*20, 25, 45+i*20, 45, fill="blue")
        cobra_corpo.append(cobra_celula)

    # Movimenta a cobra
    dx = 20
    dy = 0
    while True:
        # Atualiza a posição da cabeça da cobra
        x, y = Canvas.coords(cobra_corpo[-1])
        nova_posicao_cabeca = x+dx, y+dy
        
        # Verifica colisão com as bordas do canvas
        if nova_posicao_cabeca[0] < 0 or nova_posicao_cabeca[0] >= LARGURA_CANVAS:
            print("Fim de jogo! Sua cobra colidiu com a borda.")
            break
        if nova_posicao_cabeca[1] < 0 or nova_posicao_cabeca[1] >= ALTURA_CANVAS:
            print("Fim de jogo! Sua cobra colidiu com a borda.")
            break

        # Cria uma nova célula da cobra na nova posição da cabeça
        nova_celula = Canvas.create_rectangle(*nova_posicao_cabeca, nova_posicao_cabeca[0]+20, nova_posicao_cabeca[1]+20, fill="blue")
        cobra_corpo.append(nova_celula)

        # Remove a célula mais antiga da cobra
        Canvas.delete(cobra_corpo[0])
        cobra_corpo = cobra_corpo[1:]

        # Atualiza a tela
        tk.update()
        time.sleep(0.1)

    tk.mainloop()