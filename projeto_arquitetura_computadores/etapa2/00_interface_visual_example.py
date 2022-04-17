# https://gist.github.com/TauanSantana/0e76e15794a3c4fe41c898c11677aad0
import psutil
import pygame
import cpuinfo
import sys

largura_tela = 800
altura_tela = 600

azul = (0,0,255)
vermelho = (255,0,0)
branco = (255,255,255)
preto = (0,0,0)
cinza = (190,190,190)

sur_infocpu = pygame.surface.Surface((largura_tela, altura_tela/4))
sur_memoria = pygame.surface.Surface((largura_tela, altura_tela/4))
sur_cpu = pygame.surface.Surface((largura_tela, altura_tela/4))
sur_disco = pygame.surface.Surface((largura_tela, altura_tela/4))

info_cpu = cpuinfo.get_cpu_info()
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Análise de Computador")
pygame.display.init()
pygame.font.init()

clock = pygame.time.Clock()
terminou = False
cont = 60
font = pygame.font.Font(None, 32)

def mostra_info_cpu(s):
  s.fill(preto)
  mostra_texto(s, "Nome:", "brand_raw", 10)
  mostra_texto(s, "Arquitetura:", "arch", 30)
  mostra_texto(s, "Palavra (bits):", "bits", 50)
  mostra_texto(s, "Frequência (MHz):", "freq", 70)
  mostra_texto(s, "Núcleos (físicos):", "nucleos", 90)
  mostra_texto(s, "Núcleos (lógicos):", "nucleos_logicos", 110)
  tela.blit(s, (0, 0))

def mostra_texto(sur, nome, chave, pos_y):
  text = font.render(nome, True, branco)
  sur.blit(text, (10, pos_y))
  if chave == "freq":
      s = str(round(psutil.cpu_freq().current, 2))
  elif chave == "nucleos":
      s = str(psutil.cpu_count())
      s = s + " (" + str(psutil.cpu_count(logical=False)) + ")"
  elif chave == "nucleos_logicos":
      s = str(psutil.cpu_count())
      s = s + " (" + str(psutil.cpu_count(logical=True)) + ")"
  else:
      s = str(info_cpu[chave])
  text = font.render(s, True, cinza)
  sur.blit(text, (210, pos_y))
  

def mostra_uso_cpu(s, l_cpu_percent):
    s.fill(preto)
    capacidade = psutil.cpu_percent(interval=0)
    num_cpu = len(l_cpu_percent)
    x = y = 10
    desl = 10
    alt = s.get_height() - 2*y
    larg = (s.get_width()-2*y - (num_cpu+1)*desl)/num_cpu
    d = x + desl
    for i in l_cpu_percent:
      pygame.draw.rect(s, vermelho, (d, y + 20, larg, alt))
      pygame.draw.rect(s, azul,     (d, y + 20, larg, (1-i/100)*alt))
      d = d + larg + desl
    
    text = font.render("Uso de CPU por núcleo total:" + str(capacidade) + "%", 1, branco)
    s.blit(text, (20,10))
    tela.blit(s, (0, altura_tela/4))    



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

def mostra_uso_disco():
    disco = psutil.disk_usage('.')
    larg = largura_tela - 2*20
    sur_disco.fill(preto)
    pygame.draw.rect(sur_disco, azul, (20, 30, larg, 70))
    larg = larg*disco.percent/100
    pygame.draw.rect(sur_disco, vermelho, (20, 30, larg, 70))
    total = round(disco.total/(1024*1024*1024), 2)
    texto_barra = "Uso de Disco: (Total: " + str(total) + "GB):"
    text = font.render(texto_barra, 1, branco)
    sur_disco.blit(text, (20, 10))
    tela.blit(sur_disco, (0, ((3*altura_tela) - 120)/4))

def mostra_info_rede():
   for nic, addrs in psutil.net_if_addrs().items():
       if nic == "eth0":
           texto_barra = "%s -" % (nic) + " IP:" + str(addrs[0].address)
           text = font.render(texto_barra, 1, branco)
           tela.blit(text, (largura_tela /2 - 100, altura_tela - 20))
           


while not terminou:
  for event in pygame.event.get():
       if event.type == pygame.QUIT:
          terminou = True

  if cont == 60:
      perc = psutil.cpu_percent(percpu=True)
      mostra_info_cpu(sur_infocpu)
      mostra_uso_memoria()
      mostra_uso_cpu(sur_cpu, perc)
      mostra_uso_disco()
      mostra_info_rede()
      cont = 0
      
  pygame.display.update()
  clock.tick(60)
  cont = cont +1


  if __name__ == "__main__":
    sys.exit(main())