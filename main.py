import pygame

pygame.init()

window = pygame.display.set_mode((1920, 1080))
gameLoop = True
while gameLoop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameLoop = False
