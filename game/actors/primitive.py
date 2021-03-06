import pygame as pg
from pygame import Vector2
from pygame.sprite import Sprite
from abc import ABC, abstractmethod
from game.physics.collision import Collision


class Actor(Sprite, ABC):
    def __init__(self, x, y, image):
        super().__init__()
        self.original_image = pg.image.load(image).convert_alpha()
        self.image = self.original_image
        self.rect = self.image.get_rect(center=(x, y))

    @property
    def position(self):
        return self.rect.x, self.rect.y

    @property
    def next_rect(self):
        return self.rect

    def rotate(self, angle):
        self.image = pg.transform.rotate(self.original_image, angle)
        self.rect = self.image.get_rect(center=self.rect.center)

    def move_image(self, offset):
        self.rect.move_ip(offset)


class MovingActor(Actor, ABC):
    def __init__(self, x, y, velocity, image):
        Actor.__init__(self, x, y, image)
        self.velocity = velocity

    @property
    def next_rect(self):
        return self.rect.move(self.velocity)

    def move(self):
        super().move_image(self.velocity)

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


class AnimatedActor(Actor, ABC):
    def __init__(self, x, y, *images):
        super().__init__(x, y, images[0])
        self.image_idx = 0
        self.images = [pg.image.load(image) for image in images]
        self.image = self.images[self.image_idx]

    def animate(self, step=1):
        self.image_idx = (self.image_idx + step) % len(self.images)
        self.image = self.images[int(self.image_idx)]


class ManipulatedActor(Actor, ABC):
    def __init__(self, x, y, image):
        super().__init__(x, y, image)

    @abstractmethod
    def respond(self, keys):
        pass
