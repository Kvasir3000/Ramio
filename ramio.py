import sys
import pygame as pg
from pygame import image, display
from player import Player
from game_object import GameObject

GAME_IS_RUNNING = True
SCREEN_WIDTH, SCREEN_HEIGHT = 1920, 1080
MAIN_WINDOW = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
BACKGROUND = image.load('Background.png')
move_flag = 0   # 0 => player is not moving, 1 => go to the right, -1 => go to the left

pg.init()
CLOCK = pg.time.Clock()     # Used for frame rate management
FPS = 60    # Constant value to keep FPS at the same rate

PLAYER = Player(700, 750)
WALL_R = GameObject(1700, 750, 'brickwall.png')
WALL_L = GameObject(50, 750, 'brickwall.png')

objects = pg.sprite.Group()     # Group of sprites on the game scene
objects.add(WALL_R)
objects.add(WALL_L)


def draw():
    MAIN_WINDOW.blit(BACKGROUND, (0, 0))
    MAIN_WINDOW.blit(PLAYER.image, PLAYER.rect)
    objects.draw(MAIN_WINDOW)


def update():
    PLAYER.update(move_flag)


def handle_quit_event(user_event):  # TODO: try to use match-case statement
    if user_event.type == pg.QUIT:
        pg.quit()
        sys.exit()


def collision_detection(velocity):
    temp_rect = PLAYER.rect.move(velocity, 0)
    for obj in objects:
        if pg.Rect.colliderect(temp_rect, obj.rect):
            return True


def handle_player_movement():
    keys = pg.key.get_pressed()
    global move_flag
    if keys[pg.K_a] and not collision_detection(-PLAYER.velocity):
        move_flag = -1
    elif keys[pg.K_d] and not collision_detection(PLAYER.velocity):
        move_flag = 1
    else:
        move_flag = 0


def process_input():
    for event in pg.event.get():
        handle_quit_event(event)
    handle_player_movement()

while GAME_IS_RUNNING:
    draw()
    process_input()
    update()

    display.update()
    CLOCK.tick(FPS)
