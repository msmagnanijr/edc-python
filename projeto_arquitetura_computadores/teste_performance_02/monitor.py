import psutil
import pygame
import cpuinfo
import sys

# define pygame global variables
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Análise de Recursos Computacionais")
infnet = pygame.image.load("infnet-graduacoes-live.png")
x = 130; # x coordnate of image
y = 10; # y coordinate of image
info_cpu = cpuinfo.get_cpu_info()
pygame.display.init()
pygame.font.init()
clock = pygame.time.Clock()
finished = False
count = 60
font = pygame.font.Font(None, 32)
color_black = (0, 0, 0)
color_blue = (0, 0, 255)
color_red = (255, 0, 0)
color_white = (255, 255, 255)
color_green = (50,205,50)
color_grey = (79,79,79)
color_orange = (210,105,30)
color_lavender = (230,230,250)
surface_cpu = pygame.surface.Surface((screen_width, screen_height / 4))


def show_cpu_info(s):
    s.fill(color_lavender)
    set_cpu_info(s, "Nome:", "brand_raw", 10)
    set_cpu_info(s, "Arquitetura:", "arch", 30)
    set_cpu_info(s, "Palavra (bits):", "bits", 50)
    set_cpu_info(s, "Frequência (MHz):", "freq", 70)
    set_cpu_info(s, "Núcleos (físicos):", "nucleos", 90)
    set_cpu_info(s, "Núcleos (lógicos):", "nucleos_logicos", 110)
    screen.blit(s, (0, 0))

def set_cpu_info(sur, nome, chave, pos_y):
  text = font.render(nome, True, color_black)
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
  text = font.render(s, True, color_grey)
  sur.blit(text, (210, pos_y))

def get_ip_address():
    for nic, addrs in psutil.net_if_addrs().items():
        if nic == "wlp0s20f3":
            ip_address = "%s - " % (nic) + str(addrs[0].address)
            return ip_address

def get_memory_usage():
    surface_memory = pygame.surface.Surface((screen_width, screen_height / 4))
    memory = psutil.virtual_memory()
    memory_screen_width = screen_width - 2*20
    surface_memory.fill(color_lavender)
    pygame.draw.rect(surface_memory, color_green, (20, 30, memory_screen_width, 70))
    memory_screen_width = memory_screen_width * memory.percent / 100
    pygame.draw.rect(surface_memory, color_orange, (20, 30, memory_screen_width, 70))
    total = round(memory.total / (1024*1024*1024),2)
    total_used =  round(memory.used / (1024*1024*1024),2)
    text_screen = str(total_used) + " GB Utilizados de um Total de " + str(total) + " GB"
    text = font.render(text_screen, 1, color_grey)
    surface_memory.blit(text, (20,10))
    screen.blit(surface_memory, (0, 1*screen_height/4))

def get_cpu_usage(l_cpu_percent):
    surface_memory = pygame.surface.Surface((screen_width, screen_height / 4))
    cpu = psutil.cpu_percent(interval=1)
    #screen.blit(surface_cpu, (0, ((2*screen_height) - 120)/4))
    surface_cpu.fill(color_black)
    capacidade = psutil.cpu_percent(interval=0)
    num_cpu = len(l_cpu_percent)
    x = y = 10
    desl = 10
    alt = surface_cpu.get_height() - 2*y
    larg = (surface_cpu.get_width()-2*y - (num_cpu+1)*desl)/num_cpu
    d = x + desl
    for i in l_cpu_percent:
        pygame.draw.rect(surface_cpu, color_red, (d, y + 20, larg, alt))
        pygame.draw.rect(surface_cpu, color_blue,     (d, y + 20, larg, (1-i/100)*alt))
        d = d + larg + desl

    text = font.render("Uso de CPU por núcleo total:" + str(capacidade) + "%", 1, color_white)
    surface_cpu.blit(text, (20,10))
    screen.blit(surface_cpu, (0, screen_height/4))


def get_disk_usage():
    surface_disk = pygame.surface.Surface((screen_width, screen_height / 4))
    disk = psutil.disk_usage('/')
    disk_screen_width = screen_width - 2*20
    surface_disk.fill(color_lavender)
    pygame.draw.rect(surface_disk, color_green, (20, 30, disk_screen_width, 70))
    disk_screen_width = disk_screen_width * disk.percent / 100
    pygame.draw.rect(surface_disk, color_orange, (20, 30, disk_screen_width, 70))
    total = round(disk.total / (1024*1024*1024),2)
    total_used = round(disk.used / (1024*1024*1024),2)
    text_screen = str(total_used) + " GB Utilizados de um Total de " + str(total) + " GB"
    text = font.render(text_screen, 1, color_grey)
    surface_disk.blit(text, (20,10))
    screen.blit(surface_disk,  (0, ((3*screen_height) - 120)/4))


def get_network_info():
    surface_network = pygame.surface.Surface((screen_width, screen_height/4))
    surface_network.fill(color_lavender)
    text_screen = "IP da Interface " + str(get_ip_address())
    text = font.render(text_screen, 1, color_grey)
    surface_network.blit(text, (20,10))
    screen.blit(surface_network,  (0, ((3.8*screen_height) - 120)/4))


def main():
    global finished
    global count
    screen.fill(color_lavender)
    #screen.blit(infnet, ( x,y)) # paint to screen
    perc = psutil.cpu_percent(percpu=True)
    pygame.display.update()
    while not finished:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
        if count == 60:
            show_cpu_info(surface_cpu)
            get_memory_usage()
            get_disk_usage()
            get_network_info()
            get_cpu_usage(perc)
            count = 0

            pygame.display.update()
            clock.tick(60)
            count = count +1

if __name__ == "__main__":
    sys.exit(main())