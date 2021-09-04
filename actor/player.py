import pygame
from actor.fusion import Marionette


class Player(Marionette):
    def __init__(self, position):
        super().__init__(position, self.base_velocity, 'Character01.png')
        self.direction = 0

    @property
    def base_velocity(self):
        return 1, 0

    @property
    def jump_height(self):
        return 0

    @property
    def animation_speed(self):
        return 1

    def update(self, *args):
        if self.direction == 1:
            self.velocity = (1, 0)
            self.move(self.velocity)
        elif self.direction == -1:
            self.velocity = (-1, 0)
            self.move(self.velocity)

    def handle(self, keys):
        if keys[pygame.K_a]:
            self.direction = -1
        elif keys[pygame.K_d]:
            self.direction = 1
        else:
            self.direction = 0
