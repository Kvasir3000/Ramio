from game_object import GameObject
from pygame import image


# class Player(GameObject):
#     def __init__(self, pos_x, pos_y):
#         super().__init__(pos_x, pos_y, image.load('ghost.png'))
#
#     def update(self):
#         pass
#
#     def move_left(self):
#         self.rect.move_ip(-25, 0)
#
#     def move_right(self):
#         self.rect.move_ip(25, 0)
#
#     def draw(self):
#         pass


class Player(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y, 'Character01.png')
        self.velocity = 1
        self.current_sprite = 0
        self.sprites = []
        self.sprites.append(image.load('Character01.png'))
        self.sprites.append(image.load('Character02.png'))
        self.sprites.append(image.load('Character03.png'))
        self.sprites.append(image.load('Character04.png'))
        self.sprites.append(image.load('Character05.png'))
        self.sprites.append(image.load('Character06.png'))

    def update(self, *args):
        if args[0] == 1:
            self.current_sprite += 0.09
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
            self.image = self.sprites[int(self.current_sprite)]
            self.rect.move_ip(self.velocity, 0)
        elif args[0] == -1:
            self.rect.move_ip(-self.velocity, 0)
        else:
            current_sprite = 0
            self.image = self.sprites[current_sprite]
