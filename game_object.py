from abc import ABC
from pygame.image import load
from pygame.sprite import Sprite


class GameObject(Sprite, ABC):
    def __init__(self, x, y, *images):
        super().__init__()
        self.images = [load(image) for image in images]
        self.image_idx = 0
        self.image = self.images[self.image_idx]
        self.rect = self.image.get_rect(bottomleft=(x, y))
