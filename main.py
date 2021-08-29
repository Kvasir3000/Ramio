import pygame as pg
import pygame.image

SCREEN_WIDTH, SCREEN_HEIGHT = 1920, 1080
MAIN_WINDOW = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
BACKGROUND = pygame.image.load('farm.png')

def handle_event(user_event):   # TODO: try to use match-case statement
    if user_event.type == pg.QUIT:
        pg.quit()


pg.init()

while pg.get_init():
    for event in pg.event.get():
        handle_event(event)

    MAIN_WINDOW.blit(BACKGROUND, (0, 0))
    pygame.display.update()