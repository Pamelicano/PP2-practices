import pygame
import sys
from clock import Clock

pygame.init()

WIDTH, HEIGHT = 1100, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")

clock = pygame.time.Clock()

mickey_clock = Clock(screen)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False
        if event.type == pygame.QUIT:
            running = False

    mickey_clock.draw()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()