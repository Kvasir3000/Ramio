from abc import ABC
from pygame.image import load
from pygame.sprite import Sprite


class GameObject(Sprite, ABC):
    def __init__(self, position, *images):
        super().__init__()
        self.image_idx = 0
        self.images = [load(image) for image in images]
        self.image = self.images[self.image_idx]
        self.rect = self.image.get_rect(bottomleft=position)
