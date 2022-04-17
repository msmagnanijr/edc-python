import psutil
import pygame
import cpuinfo
import sys

# screen resolution
screen_width = 800
screen_height = 600

# colors
gray = (47,79,79)
green = (124,252,0)
purple =  (186,85,211)
white = (255,255,255)

# set vars
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Monitorando Recursos do Computador")
pygame.display.init()
pygame.font.init()
cpu_info = cpuinfo.get_cpu_info()
clock = pygame.time.Clock()
finished = False
count = 60
font = pygame.font.Font(None, 30)

def show_cpu_info():
    surface = pygame.surface.Surface((screen_width, screen_height/4))
    surface.fill(gray)
    set_infos(surface, "Nome:", "brand_raw", 10)
    set_infos(surface, "Arquitetura:", "arch", 30)
    set_infos(surface, "Palavra (bits):", "bits", 50)
    set_infos(surface, "Frequência (MHz):", "freq", 70)
    set_infos(surface, "Núcleos (físicos):", "nucleos", 90)
    set_infos(surface, "Núcleos (lógicos):", "nucleos_logicos", 110)
    screen.blit(surface, (0, 0))

def set_infos(surface, name, key, y):
    text = font.render(name, True, white)
    surface.blit(text, (10, y))
    if key == "freq":
        sur = str(round(psutil.cpu_freq().current, 2))
    elif key == "nucleos":
        sur = str(psutil.cpu_count())
        sur = sur + " (" + str(psutil.cpu_count(logical=False)) + ")"
    elif key == "nucleos_logicos":
        sur = str(psutil.cpu_count())
        sur = sur + " (" + str(psutil.cpu_count(logical=True)) + ")"
    else:
        sur = str(cpu_info[key])
    text = font.render(sur, True, white)
    surface.blit(text, (210, y))

def get_cpu_usage(cpu_utilization):
    surface_cpu = pygame.surface.Surface((screen_width, screen_height/4))
    surface_cpu.fill(gray)
    capacity = psutil.cpu_percent(interval=0)
    cpus = len(cpu_utilization)
    x = y = 10
    off = 10
    height = surface_cpu.get_height() - 2*y
    width = (surface_cpu.get_width()-2*y - (cpus+1)*off)/cpus
    value = x + off
    for i in cpu_utilization:
        pygame.draw.rect(surface_cpu, green, (value, y + 20, width, height))
        pygame.draw.rect(surface_cpu, purple,     (value, y + 20, width, (1-i/100)*height))
        value = value + width + off

    text = font.render("Uso de CPU por núcleo na FIAP. Consumo Atual: " + str(capacity) + "%", 1, white)
    surface_cpu.blit(text, (20,10))
    screen.blit(surface_cpu, (0, screen_height/4))

def get_memory_usage():
    surface_memory = pygame.surface.Surface((screen_width, screen_height/4))
    memory = psutil.virtual_memory()
    memory_screen_width = screen_width - 2*20
    surface_memory.fill(gray)
    pygame.draw.rect(surface_memory, purple, (20, 30, memory_screen_width, 70))
    memory_screen_width = memory_screen_width*memory.percent/100
    pygame.draw.rect(surface_memory, green, (20, 30, memory_screen_width, 70))
    total = round(memory.total/(1024*1024*1024),2)
    total_used =  round(memory.used / (1024*1024*1024),2)
    text_screen = str(total_used) + " GB Utilizados de um Total de " + str(total) + " GB"
    text = font.render(text_screen, 1, white)
    surface_memory.blit(text, (20,10))
    screen.blit(surface_memory, (0, 2*screen_height/4))

def get_disk_usage():
    surface_disk = pygame.surface.Surface((screen_width, screen_height/4))
    disk = psutil.disk_usage('/')
    disk_screen_width = screen_width - 2*20
    surface_disk.fill(gray)
    pygame.draw.rect(surface_disk, purple, (20, 30, disk_screen_width, 70))
    disk_screen_width = disk_screen_width*disk.percent/100
    pygame.draw.rect(surface_disk, green, (20, 30, disk_screen_width, 70))
    total = round(disk.total/(1024*1024*1024), 2)
    total_used =  round(disk.used / (1024*1024*1024),2)
    text_screen =  str(total_used) + " GB Utilizados de um Total de " + str(total) + " GB"
    text = font.render(text_screen, 1, white)
    surface_disk.blit(text, (20, 10))
    screen.blit(surface_disk, (0, ((3*screen_height) - 120)/4))

def get_ip_address():
    for nic, addrs in psutil.net_if_addrs().items():
        if nic == "enx3ce1a1c10ad0":
            ip_address = "%s é " % (nic) + str(addrs[0].address)
            return ip_address

def get_network_info():
    surface_network = pygame.surface.Surface((screen_width, screen_height/4))
    surface_network.fill(gray)
    text_screen = "IP da Interface " + str(get_ip_address())
    text = font.render(text_screen, 1, white)
    surface_network.blit(text, (20,10))
    screen.blit(surface_network,  (0, ((3.8*screen_height) - 120)/4))

def main():
    global finished
    global count

    while not finished:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True

        if count == 60:
            cpu_utilization = psutil.cpu_percent(percpu=True)
            show_cpu_info()
            get_memory_usage()
            get_cpu_usage(cpu_utilization)
            get_disk_usage()
            get_network_info()
            count = 0

        pygame.display.update()
        clock.tick(60)
        count = count +1

if __name__ == "__main__":
    sys.exit(main())