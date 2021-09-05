import pygame
from actor.fusion import Marionette
from physics.collision import Collision
from physics.constants import Constants


class Player(Marionette):
    def __init__(self, position):
        super().__init__(position, self.base_velocity, 'Character01.png')
        self.is_jumping = False

    @property
    def base_velocity(self):
        return [0, 0]

    @property
    def jump_height(self):
        return 0

    @property
    def animation_speed(self):
        return 1

    def update_x_coordinates(self, actors):
        if self.x_velocity < 0 and Collision.detect('left', self, actors):
            self.x_velocity = 0
        elif self.x_velocity > 0 and Collision.detect('right', self, actors):
            self.x_velocity = 0

    def update_y_coordinates(self, actors):
        if self.is_falling(actors):
            self.jump()
            if Collision.detect('top', self, actors):
                self.y_velocity = -self.y_velocity
        elif self.y_velocity >= 0:
            self.y_velocity = 0
            self.is_jumping = False
        elif self.y_velocity < 0:
            self.jump()

    def update(self, *actors):
        self.update_x_coordinates(actors)
        self.update_y_coordinates(actors)
        self.move(self.velocity)

    def handle(self, keys):
        if keys[pygame.K_a]:
            self.x_velocity = -2.
        elif keys[pygame.K_d]:
            self.x_velocity = 2
        else:
            self.x_velocity = 0

        if keys[pygame.K_SPACE] and not self.is_jumping:
            self.is_jumping = True
            self.y_velocity = -10

    def is_falling(self, objects):
        return self.y < Constants.GROUND and not Collision.detect('bottom', self, objects)
