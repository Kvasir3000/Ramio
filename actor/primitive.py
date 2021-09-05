from pygame.image import load
from pygame.sprite import Sprite
from physics.constants import Constants
from abc import ABC, abstractmethod


class Actor(Sprite, ABC):
    def __init__(self, position, image):
        super().__init__()
        self.image = load(image)
        self.rect = self.image.get_rect(bottomleft=position)

    @property
    def x(self):
        return self.rect.x

    @x.setter
    def x(self, val):
        self.rect.x = val

    @property
    def y(self):
        return self.rect.y

    @y.setter
    def y(self, val):
        self.rect.y = val

    def move_image(self, offset):
        self.rect.move_ip(offset)


class MovingActor(Actor, ABC):
    def __init__(self, position, velocity, image):
        Actor.__init__(self, position, image)
        self.velocity = velocity

    @property
    @abstractmethod
    def base_velocity(self):
        pass

    @property
    @abstractmethod
    def jump_height(self):
        pass

    def move(self, offset):
        super().move_image(offset)

    # TODO: sdelay
    def jump(self):
        self.y_velocity += Constants.ACCELERATION / 60

    @property
    def x_velocity(self):
        return self.velocity[0]

    @x_velocity.setter
    def x_velocity(self, val):
        self.velocity[0] = val

    @property
    def y_velocity(self, ):
        return self.velocity[1]

    @y_velocity.setter
    def y_velocity(self, val):
        self.velocity[1] = val


class AnimatedActor(Actor, ABC):
    def __init__(self, position, *images):
        super().__init__(position, images[0])
        self.image_idx = 0
        self.images = [load(image) for image in images]
        self.image = self.images[self.image_idx]

    @property
    @abstractmethod
    def animation_speed(self):
        pass

    def animate(self, step):
        self.image_idx = (self.image_idx + step) % len(self.images)
        self.image = self.images[int(self.image_idx)]


class ManipulatedActor(Actor, ABC):
    def __init__(self, position, image):
        super().__init__(position, image)

    @abstractmethod
    def handle(self, keys):
        pass

