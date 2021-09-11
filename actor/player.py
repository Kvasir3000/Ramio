import pygame
from actor.fusion import Marionette
from physics.collision import Collision
from pygame.math import Vector2
import pygame.mouse as mouse
import math


class Player(Marionette):
    def __init__(self, x, y):
        super().__init__(x, y, self.base_velocity, 'player.png')
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
        if self.velocity.x > 0 and Collision.detect(self, actors, 'right'):
            self.velocity.x = 0
        elif self.velocity.x < 0 and Collision.detect(self, actors, 'left'):
            self.velocity.x = 0

    def update_y(self, actors):
        if self.velocity.y > 0 and Collision.detect(self, actors, 'bottom'):
            self.velocity.y = 0
        elif self.velocity.y < 0 and Collision.detect(self, actors, 'top'):
            self.velocity.y = 0

    def handle(self, keys):
        self.keyboard_input(keys)
        self.mouse_input()

    def keyboard_input(self, keys):
        if keys[pygame.K_w]:
            self.velocity.y = -7
        elif keys[pygame.K_s]:
            self.velocity.y = 7
        else:
            self.velocity.y = 0

        if keys[pygame.K_a]:
            self.velocity.x = -7
        elif keys[pygame.K_d]:
            self.velocity.x = 7
        else:
            self.velocity.x = 0

    def mouse_input(self):
        mouse_x, mouse_y = mouse.get_pos()
        if mouse_x <= 0:
            mouse_x = 1
        if mouse_y <= 0:
            mouse_y = 1
        x_distance = mouse_x - self.rect.topleft[0]
        y_distance = mouse_y - self.rect.topleft[1]
        if x_distance == 0:
            x_distance = 1
        elif y_distance == 0:
            y_distance = 1

        angle = (180 / math.pi) * -math.atan2(y_distance, x_distance)
        self.image = pygame.transform.rotate(self.original_image, angle)
        orig_center = self.rect.center
        self.rect = self.image.get_rect(center=orig_center)
