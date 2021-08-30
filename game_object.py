from abc import ABC, abstractmethod


class GameObject(ABC):
    def __init__(self, pos_x, pos_y, *sprites):  # TODO: check is sprites are empty
        self.sprite_idx = 0
        self.sprites = list(sprites)
        self.image = self.sprites[self.sprite_idx]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def draw(self):
        pass

    @staticmethod
    def collision(obj1, obj2):
        return obj1.rect.colliderect(obj2)
