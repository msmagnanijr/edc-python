import psutil
import pygame

largura_tela = 800
altura_tela = 600

azul = (0,0,255)
vermelho = (255,0,0)
branco = (255,255,255)
preto = (0,0,0)
cinza = (190,190,190)

sur_memoria = pygame.surface.Surface((largura_tela, altura_tela/4))

tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Análise de Computador")
pygame.display.init()
pygame.font.init()

clock = pygame.time.Clock()
terminou = False
cont = 60
font = pygame.font.Font(None, 32)

def mostra_uso_memoria():
    mem = psutil.virtual_memory()
    larg = largura_tela - 2*20
    sur_memoria.fill(preto)
    pygame.draw.rect(sur_memoria, azul, (20, 30, larg, 70))
    larg = larg*mem.percent/100
    pygame.draw.rect(sur_memoria, vermelho, (20, 30, larg, 70))
    total = round(mem.total/(1024*1024*1024),2)
    texto_barra = "Uso de memória (Total: " + str(total) + "GB):"
    text = font.render(texto_barra, 1, branco)
    sur_memoria.blit(text, (20,10))
    tela.blit(sur_memoria, (0, 2*altura_tela/4))

while not terminou:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True

    if cont == 60:
        perc = psutil.cpu_percent(percpu=True)
        mostra_uso_memoria()
        cont = 0
        
        pygame.display.update()
        clock.tick(60)
        cont = cont +1