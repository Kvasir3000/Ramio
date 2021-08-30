from abc import ABC, abstractmethod


class GameObject(ABC):
    def __init__(self, x, y, *sprites):  # TODO: check is sprites are empty
        self.x = x
        self.y = y
        self.sprites = list(sprites)
        self.height = sprites[0].get_height()
        self.width = sprites[0].get_width()

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def generate_output(self):
        pass

    @staticmethod
    def __x_collision(obj1, obj2):
        return obj1.x < obj2.x + obj2.width and obj1.x + obj1.width > obj2.x

    @staticmethod
    def __y_collision(obj1, obj2):
        return obj1.y < obj2.y + obj2.y and obj1.y + obj1.height > obj2.y

    @staticmethod
    def collision(obj1, obj2):
        return GameObject.__x_collision(obj1, obj2) and GameObject.__y_collision(obj1, obj2)
