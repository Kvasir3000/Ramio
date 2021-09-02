import sys
import pygame as pg
from pygame import image, display
from player import Player
from game_object import GameObject

# GAME_IS_RUNNING = True
# SCREEN_WIDTH, SCREEN_HEIGHT = 1920, 1080
# MAIN_WINDOW = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# BACKGROUND = image.load('Background.png')
# move_flag = 0   # 0 => player is not moving, 1 => go to the right, -1 => go to the left
#
# pg.init()
# CLOCK = pg.time.Clock()     # Used for frame rate management
# FPS = 60    # Constant value to keep FPS at the same rate
#
# PLAYER = Player(700, 750)
# WALL_R = GameObject(1700, 750, 'brickwall.png')
# WALL_L = GameObject(50, 750, 'brickwall.png')
#
# objects = pg.sprite.Group()     # Group of sprites on the game scene
# objects.add(WALL_R)
# objects.add(WALL_L)
#
#
# def draw():
#     MAIN_WINDOW.blit(BACKGROUND, (0, 0))
#     MAIN_WINDOW.blit(PLAYER.image, PLAYER.rect)
#     objects.draw(MAIN_WINDOW)
#
#
# def update():
#     PLAYER.update(move_flag)
#
#
# def handle_quit_event(user_event):  # TODO: try to use match-case statement
#     if user_event.type == pg.QUIT:
#         pg.quit()
#         sys.exit()
#
#
# def collision_detection(velocity):
#     temp_rect = PLAYER.rect.move(velocity, 0)
#     for obj in objects:
#         if pg.Rect.colliderect(temp_rect, obj.rect):
#             return True
#
#
# def handle_player_movement():
#     keys = pg.key.get_pressed()
#     global move_flag
#     if keys[pg.K_a] and not collision_detection(-PLAYER.velocity):
#         move_flag = -1
#     elif keys[pg.K_d] and not collision_detection(PLAYER.velocity):
#         move_flag = 1
#     else:
#         move_flag = 0
#
#
# def process_input():
#     for event in pg.event.get():
#         handle_quit_event(event)
#     handle_player_movement()
#
# while GAME_IS_RUNNING:
#     draw()
#     process_input()
#     update()
#
#     display.update()
#     CLOCK.tick(FPS)


class Game:
    def __init__(self):
        self.__game_is_running = True
        self.__screen_width, self.__screen_height = 1920, 1080
        self.__main_window = display.set_mode((self.__screen_width, self.__screen_height))
        self.__background = None
        self.__move_flag = 0
        pg.init()
        self.__clock = pg.time.Clock()
        self.__fps = 60
        self.__player = pg.sprite.GroupSingle()
        self.__objects = pg.sprite.Group()

    def __load(self):
        self.__background = image.load('Background.png')
        player = Player((700, 750))
        self.__player.add(player)

    def __draw(self):
        self.__main_window.blit(self.__background, (0, 0))
        self.__player.draw(self.__main_window)

    def __update(self):
        self.__player.update(self.__move_flag)

    def __handle_quit_event(self, user_event):
        if user_event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    def __collision_detection(self, velocity):
        temp_rect = self.__player.sprite.rect.move(velocity, 0)
        for obj in self.__objects:
            if pg.Rect.colliderect(temp_rect, obj.rect):
                return True

    def __handle_player_movement(self):
        keys = pg.key.get_pressed()
        velocity = self.__player.sprite.velocity[0]
        if keys[pg.K_a] and not self.__collision_detection(-velocity):
            self.__player.sprite.direction = -1
        elif keys[pg.K_d] and not self.__collision_detection(velocity):
            self.__player.sprite.direction = 1
        else:
            self.__player.sprite.direction = 0

    def __process_input(self):
        for event in pg.event.get():
            self.__handle_quit_event(event)
        self.__handle_player_movement()

    def start(self):
        self.__load()
        while self.__game_is_running:
            self.__process_input()
            self.__update()
            self.__draw()

            display.update()
            self.__clock.tick(self.__fps)

game = Game()
game.start()
