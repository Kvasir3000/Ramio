from moving_object import MovingObject
from velocity import Velocity
from direction import Direction


class Player(MovingObject):
    DEFAULT_VELOCITY = Velocity((1, 0), Direction.NONE)

    def __init__(self, position):
        super().__init__(position, self.DEFAULT_VELOCITY, "Character01.png")

    def update(self, flag):
        if self.direction == Direction.RIGHT:
            self.image_idx = (self.image_idx + 0.09) % len(self.images)
            self.image = self.images[int(self.image_idx)]
            self.rect.move_ip(self.velocity)
        elif self.direction == Direction.LEFT:
            self.rect.move_ip((-self.velocity[0], self.velocity[1]))
        else:
            current_sprite = 0
            self.image = self.images[current_sprite]
