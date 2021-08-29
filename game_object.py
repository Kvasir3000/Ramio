import abc


class GameObject:

    def __init__(self, x, y, sprite):
        self.x = x
        self.y = y
        self.sprite = sprite
        self.height = sprite.get_height()
        self.width = sprite.get_width()

    @abc.abstractmethod
    def update(self):
        pass

    @abc.abstractmethod
    def generate_output(self):
        pass

    @staticmethod
    def collision(obj_1, obj_2):
        if obj_1.x < obj_2.x + obj_2.width and obj_1.x + obj_1.width > obj_2.x \
                 and obj_1.y < obj_2.y + obj_2.y and obj_1.y + obj_1.height > obj_2.y:
                    return True
