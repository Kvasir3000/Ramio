import pygame as pg
import pygame.image
from player import Player


SCREEN_WIDTH, SCREEN_HEIGHT = 1920, 1080
MAIN_WINDOW = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
BACKGROUND = pygame.image.load('farm.png')
PLAYER_SPRITE = pygame.image.load('ghost.png')
PLAYER = Player(100, 1000, PLAYER_SPRITE)


def handle_event(user_event):   # TODO: try to use match-case statement
    if user_event.type == pg.QUIT:
        pg.quit()


pg.init()


def draw():
    MAIN_WINDOW.blit(BACKGROUND, (0, 0))
    MAIN_WINDOW.blit(PLAYER.sprites, (PLAYER.x, PLAYER.y))


def update():
    PLAYER.update()

while pg.get_init():
    MAIN_WINDOW.blit(BACKGROUND, (0, 0))
    pygame.display.update()
    for event in pg.event.get():
        handle_event(event)
