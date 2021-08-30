import sys
import pygame as pg
from pygame import image, display
from player import Player

SCREEN_WIDTH, SCREEN_HEIGHT = 1920, 1080
MAIN_WINDOW = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
BACKGROUND = image.load('farm.png')
PLAYER = Player(0, 0)


def handle_event(user_event):  # TODO: try to use match-case statement
    if user_event.type == pg.QUIT:
        pg.quit()
        sys.exit()
    if event.type == pg.KEYDOWN:
        if event.key == pg.K_LEFT:
            PLAYER.move_left()
        if event.key == pg.K_RIGHT:
            PLAYER.move_right()


pg.init()


def draw():
    MAIN_WINDOW.blit(BACKGROUND, (0, 0))
    MAIN_WINDOW.blit(PLAYER.sprites[0], PLAYER.rect.topleft)


def update():
    PLAYER.update()


while True:
    for event in pg.event.get():
        handle_event(event)

    draw()
    display.update()
