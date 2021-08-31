from game_object import GameObject
from glob import glob


class Player(GameObject):
    __DEFAULT_VELOCITY = 1
    # TODO: make x and y as pair

    def __init__(self, x, y):
        super().__init__(x, y, self.__DEFAULT_VELOCITY, "Character01.png")

    def update(self, *args):
        if args[0] == 1:
            self.image_idx = (self.image_idx + 0.09) % len(self.images)
            self.image = self.images[int(self.image_idx)]
            self.rect.move_ip(self.velocity, 0)
        elif args[0] == -1:
            self.rect.move_ip(-self.velocity, 0)
        else:
            current_sprite = 0
            self.image = self.images[current_sprite]
