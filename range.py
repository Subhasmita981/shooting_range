import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((640, 360))
clock = pygame.time.Clock()

bg_surface = pygame.image.load("assets/wood.jpg")
bg_surface = pygame.transform.scale(bg_surface, (640, 360))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()

    screen.blit(bg_surface, (0, 0))
    pygame.display.update()
    clock.tick(120)