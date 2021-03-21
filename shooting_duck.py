# shooting range by #Subhasmita #Bhanja all rights reserved

import pygame
import sys
import random

pygame.init()

# creating a screen in pygame
screen = pygame.display.set_mode((640, 360))
clock = pygame.time.Clock()
# program not to show the cross hair inside the game
pygame.mouse.set_visible(False)

# importing background image
bg_img = pygame.image.load("assets/wood.jpg").convert()

# importing cloud images
cloud_img = pygame.image.load("assets/cloud1.png")
cloud_img = pygame.transform.scale(cloud_img, (100, 100))
cloud1_img = pygame.image.load("assets/cloud2.png")
cloud1_img = pygame.transform.scale(cloud1_img, (100, 100))

# importing ground images
ground_img = pygame.image.load("assets/ground.png").convert_alpha()
ground_img = pygame.transform.scale(ground_img, (700, 70))
ground_y_pos = 290
ground_speed = 1

# importing water images
water_img = pygame.image.load("assets/water_surface.png").convert_alpha()
water_img = pygame.transform.scale(water_img, (700, 80))
# water vars
water_y_pos = 330
water_speed = 1

# cross hair images
cross_surface = pygame.image.load("assets/cursor.png")
cross_surface = pygame.transform.scale(cross_surface, (25, 25))
cross_rect = cross_surface.get_rect(center=(0, 0))

# importing duck images
duck_surface = pygame.image.load("assets/duck1.png").convert_alpha()
duck_surface = pygame.transform.scale(duck_surface, (100, 100))

# creating a random list of ducks
duck_list = []
for duck in range(20):
    duck_x_pos = random.randrange(25, 600)
    duck_y_pos = random.randrange(60, 300)
    duck_rect = duck_surface.get_rect(center=(duck_x_pos, duck_y_pos))
    duck_list.append(duck_rect)

# text properties
game_font = pygame.font.Font(None, 30)
text_surface = game_font.render('You won!', True, (255, 255, 255))
text_surface_rect = text_surface.get_rect(center=(320, 180))

# loops and events
running = True
while running:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        # mouse motion of the cross hair image and target shooting
        if event.type == pygame.MOUSEMOTION:
            cross_rect = cross_surface.get_rect(center=event.pos)
        if event.type == pygame.MOUSEBUTTONDOWN:
            for index, duck_rect in enumerate(duck_list):
                if duck_rect.collidepoint(event.pos):  # cross hair_rect.collide rect(duck_rect):
                    del duck_list[index]

    # blit of background
    screen.blit(bg_img, (0, 0))

    # blit of cloud
    screen.blit(cloud_img, (25, 0))
    screen.blit(cloud1_img, (500, 0))
    screen.blit(cloud_img, (250, -20))

    # blit of duck and rectangle around it for collision
    for duck_rect in duck_list:
        screen.blit(duck_surface, duck_rect)

    # vanishing duck when it collides with the rectangle around the cross hair
    if len(duck_list) == 0:
        screen.blit(text_surface, text_surface_rect)

    # blit of ground image
    screen.blit(ground_img, (0, ground_y_pos))

    # adding animation to y pos of water
    water_y_pos -= water_speed
    if water_y_pos <= 310 or water_y_pos >= 390:
        water_speed *= -1
    screen.blit(water_img, (0, water_y_pos))

    # blit of cross hair and the rectangle around it
    screen.blit(cross_surface, cross_rect)

    pygame.display.update()
    # frame rates in pixels
    clock.tick(120)
