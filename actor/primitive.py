from pygame.image import load
from pygame.sprite import Sprite
from physics import constants
from pygame.math import Vector2
from abc import ABC, abstractmethod
from physics.collision import Collision


class Actor(Sprite, ABC):
    def __init__(self, x, y, image):
        super().__init__()
        self.original_image = load(image)
        self.image = self.original_image
        self.rect = self.image.get_rect(bottomleft=(x, y))

    @property
    def x(self):
        return self.rect.x

    @property
    def y(self):
        return self.rect.y

    @property
    def next_rect(self):
        return self.rect

    def move_image(self, offset):
        self.rect.move_ip(offset)

    # TODO: remove first condition when ground is added
    def is_falling(self, objects):
        return self.y < 600 and not Collision.detect(self, objects, dir='bottom')

    def normalize(self, y):
        return y * -1


class MovingActor(Actor, ABC):
    def __init__(self, x, y, velocity, image):
        Actor.__init__(self, x, y, image)
        self.velocity = velocity

    @property
    @abstractmethod
    def base_velocity(self) -> Vector2:
        pass

    @property
    @abstractmethod
    def jump_height(self) -> int:
        pass

    @property
    def next_rect(self):
        return self.rect.move(self.velocity)

    def move(self, offset):
        super().move_image(offset)

    def jump(self):
        self.velocity.y += constants.GRAVITATIONAL_ACCELERATION / 60


class AnimatedActor(Actor, ABC):
    def __init__(self, x, y, *images):
        super().__init__(x, y, images[0])
        self.image_idx = 0
        self.images = [load(image) for image in images]
        self.image = self.images[self.image_idx]

    @property
    @abstractmethod
    def animation_speed(self) -> int:
        pass

    def animate(self, step):
        self.image_idx = (self.image_idx + step) % len(self.images)
        self.image = self.images[int(self.image_idx)]


class ManipulatedActor(Actor, ABC):
    def __init__(self, x, y, image):
        super().__init__(x, y, image)

    @abstractmethod
    def handle(self, keys):
        pass
