import math
import numpy as np
import pygame as pg
from pygame.math import Vector2
from game.actors.fusion import Marionette


class Ramio(Marionette):
    MAX_SPEED = 7

    def __init__(self, x, y):
        super().__init__(x, y, Vector2(0, 0), 'player.png')
        self.last_cursor_position = (0, 0)

    def update(self, actors):
        self.update_position(actors)
        self.move()

    def update_position(self, actors):
        self.update_x(actors)
        self.update_y(actors)

    def respond(self, keys):
        self.keyboard_input(keys)
        self.mouse_input()

    def keyboard_input(self, keys):
        if keys[pg.K_w]:
            self.velocity.y = -self.MAX_SPEED
        elif keys[pg.K_s]:
            self.velocity.y = self.MAX_SPEED
        else:
            self.velocity.y = 0

        if keys[pg.K_a]:
            self.velocity.x = -self.MAX_SPEED
        elif keys[pg.K_d]:
            self.velocity.x = self.MAX_SPEED
        else:
            self.velocity.x = 0

    def mouse_input(self):
        current_cursor_position = pg.mouse.get_pos()
        if current_cursor_position != self.last_cursor_position:
            self.last_cursor_position = current_cursor_position
            distance = np.subtract(current_cursor_position, self.position)
            angle = math.degrees(math.pi + math.atan2(*distance))
            self.rotate(angle)
