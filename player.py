from moving_object import MovingObject
from velocity import Velocity
from direction import Direction


class Player(MovingObject):
    DEFAULT_VELOCITY = Velocity((1, 0))

    def __init__(self, position):
        super().__init__(position, self.DEFAULT_VELOCITY, "Character01.png")

    def update(self, flag):
        if self.direction == self.direction == 1:
            self.image_idx = (self.image_idx + 0.9) % len(self.images)  # TODO: ETO NE RABOTAET, PEREDELAY
            self.image = self.images[int(self.image_idx)]
            self.rect.move_ip(self.velocity[0], self.velocity[1])
        elif self.direction == self.direction == -1:
            self.rect.move_ip((-self.velocity[0], self.velocity[1]))
        else:
            current_sprite = 0
            self.image = self.images[current_sprite]
