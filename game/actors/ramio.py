import math
import numpy as np
import pygame as pg
from pygame.math import Vector2
from game.actors.fusion import Marionette
from game.physics.collision import Collision


class Ramio(Marionette):
    MAX_SPEED = 7

    def __init__(self, x, y):
        super().__init__(x, y, Vector2(0, 0), 'player.png')

    def update(self, actors):
        self.update_position(actors)
        self.move()

    def update_position(self, actors):
        self.update_x(actors)
        self.update_y(actors)

    def update_x(self, actors):
        if self.velocity.x > 0 and Collision.detect(self, actors, 'right'):
            self.velocity.x = 0
        elif self.velocity.x < 0 and Collision.detect(self, actors, 'left'):
            self.velocity.x = 0

    def update_y(self, actors):
        if self.velocity.y > 0 and Collision.detect(self, actors, 'bottom'):
            self.velocity.y = 0
        elif self.velocity.y < 0 and Collision.detect(self, actors, 'top'):
            self.velocity.y = 0

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
        distance = np.subtract(pg.mouse.get_pos(), self.position)
        angle = math.degrees(math.pi + math.atan2(*distance))
        self.rotate(angle)