import pygame
from sys import exit 
from settings import COMPRIMENTO_TELA, ALTURA_TELA, FPS
from cores import *
from processo import Processo
from processador import Processador 

pygame.init()
# Configurações pygame 
tela = pygame.display.set_mode((COMPRIMENTO_TELA, ALTURA_TELA))
EVENTO = pygame.USEREVENT + 1
pygame.time.set_timer(EVENTO, 500)
clock = pygame.time.Clock()

# Variáveis globais
tempo_decorrido = 0
processos = [Processo('P0', 40, 1), Processo('P1', 15, 2)]
processador = Processador(processos)
tam_retangulo = 0
processo_atual: Processo | None = None

def escrever_cronometro():
    fonte = pygame.font.SysFont(None, 35)
    fonte_surf = fonte.render(f'Tempo passado: {tempo_decorrido} ms', True, PRETO)
    fonte_ret = fonte_surf.get_rect(center=(150, 50))
    tela.blit(fonte_surf, fonte_ret)


def escrever_filas():
    filas = processador.filas
    filaIO = processador.filaIO
    fonte = pygame.font.SysFont(None, 30)
    
    for y, fila in enumerate(filas.keys()):
        nome_fila_surf = fonte.render(f'{fila}: ', True, PRETO)
        nome_fila_ret = nome_fila_surf.get_rect(center=(50, 100 + 40 * y))
        tela.blit(nome_fila_surf, nome_fila_ret)
        
        for x, processo in enumerate(filas[fila]):
            nome_processo_surf = fonte.render(f'{processo.nomeProcesso}', True, PRETO)
            nome_processo_ret = nome_processo_surf.get_rect(center=(80 + 30 * x, 100 + 40 * y))
            tela.blit(nome_processo_surf, nome_processo_ret)
    
    y_io = 100 + 40 * len(filas)
    io_surf = fonte.render(f'IO: ', True, PRETO)
    io_ret = io_surf.get_rect(center=(50, y_io))
    tela.blit(io_surf, io_ret)
    
    for x, processo in enumerate(filaIO):
        nome_processo_surf = fonte.render(f'{processo.nomeProcesso}', True, PRETO)
        nome_processo_ret = nome_processo_surf.get_rect(center=(80 + 30 * x, y_io))
        tela.blit(nome_processo_surf, nome_processo_ret)


def desenhar_diagrama():
    global tam_retangulo, processo_atual 
    if processo_atual == processador.get_processando(): ...

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == EVENTO:
            print(f'tempo= {tempo_decorrido}')
            processando = processador.get_processando()
            if processando is None:
                print('Processos finalizados!')
                exit()
            print(processando)
            processador.update(tempo_decorrido)
            tempo_decorrido += 1


    # Verificar a tela
    tela.fill('white')
    escrever_cronometro()
    escrever_filas()
    pygame.display.update()
    
    # incrementar o tempo 
    
    
    clock.tick(FPS)
