import math
import numpy as np
import pygame as pg
import pygame.mask
from pygame.math import Vector2
from game.actors.fusion import Marionette
from game.physics.collision import Collision
import copy

class Ramio(Marionette):
    MAX_SPEED = 7

    def __init__(self, x, y):
        super().__init__(x, y, Vector2(0, 0), 'player.png')
        self.last_cursor_position = (0, 0)
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, actors):
        self.move()
        collision_flag = Collision.detect(self, actors)
        if collision_flag[0]:
            self.velocity[0] = -self.velocity[0]
        if collision_flag[1]:
            self.velocity[1] = -self.velocity[1]
        if collision_flag[0] or collision_flag[1]:
            self.move()
            self.velocity[0] = 0
            self.velocity[0] = 0

    def respond(self, keys, actors):
        self.keyboard_input(keys)
        self.mouse_input(actors)

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

    def mouse_input(self, actors):
        current_cursor_position = pg.mouse.get_pos()
        temp = copy.copy(self)
        if current_cursor_position != self.last_cursor_position:
            distance = np.subtract(current_cursor_position, self.position)
            angle = math.degrees(math.pi + math.atan2(*distance))
            temp.rotate(angle)
            if not Collision.detect_rotation(temp, actors):
                self.rotate(angle)
                print('Rotated')
            else:
                current_cursor_position = self.last_cursor_position
               # pygame.mouse.set_pos(self.last_cursor_position)
            self.last_cursor_position = current_cursor_position
            self.mask = pygame.mask.from_surface(self.image)

