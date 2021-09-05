import pygame
from actor.fusion import Marionette
from physics.collision import Collision
from pygame.math import Vector2
from physics import constants


class Player(Marionette):
    def __init__(self, x, y):
        super().__init__(x, y, self.base_velocity, 'Character01.png')
        self.is_jumping = False

    @property
    def base_velocity(self):
        return Vector2(0, 0)

    @property
    def jump_height(self):
        return 0

    @property
    def animation_speed(self):
        return 1

    def update(self, actors):
        self.update_position(actors)
        self.move(self.velocity)

    def update_position(self, actors):
        self.update_x(actors)
        self.update_y(actors)

    def update_x(self, actors):
        if self.velocity.x < 0 and Collision.detect(self, actors, dir='left'):
            self.velocity.x = 0
        elif self.velocity.x > 0 and Collision.detect(self, actors, dir='right'):
            self.velocity.x = 0

    def update_y(self, actors):
        if self.is_falling(actors):
            self.jump()
            if Collision.detect(self, actors, dir='top'):
                self.velocity.y *= -1
        elif self.velocity.y >= 0:
            self.velocity.y = 0
            self.is_jumping = False
        elif self.velocity.y < 0:
            self.jump()

    def handle(self, keys):
        self.handle_movement(keys)
        self.handle_jump(keys)

    def handle_movement(self, keys):
        if keys[pygame.K_a]:
            self.velocity.x = -2
        elif keys[pygame.K_d]:
            self.velocity.x = 2
        else:
            self.velocity.x = 0

    def handle_jump(self, keys):
        if keys[pygame.K_SPACE] and not self.is_jumping:
            self.is_jumping = True
            self.velocity.y = -10
