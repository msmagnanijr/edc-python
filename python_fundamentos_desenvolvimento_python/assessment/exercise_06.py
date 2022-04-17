"""Usando a biblioteca ‘pygame’, escreva um programa que desenha na tela em posição aleatória um quadrado amarelo de tamanho 50 (cinquenta),
toda vez que a tecla espaço for pressionada ou o botão direito for clicado"""
import pygame
from random import randint
from time import sleep
import sys

def main():

    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Exercise 06')
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    x = randint(0, 800)
                    y = randint(0, 600)
                    pygame.draw.rect(screen, (255, 255, 0), (x, y, 50, 50))
                    pygame.display.flip()
                    sleep(0.1)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 3:
                    x = randint(0, 800)
                    y = randint(0, 600)
                    pygame.draw.rect(screen, (255, 255, 0), (x, y, 50, 50))
                    pygame.display.flip()
                    sleep(0.1)
        clock.tick(60)
    pygame.quit()

if __name__ == "__main__":
    sys.exit(main())