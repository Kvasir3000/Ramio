from game_object import GameObject
from pygame import image


class Player(GameObject):
    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y, image.load('ghost.png'))

    def update(self):
        pass

    def move_left(self):
        self.rect.move_ip(-25, 0)

    def move_right(self):
        self.rect.move_ip(25, 0)

    def draw(self):
        pass
