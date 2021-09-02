from game_object import GameObject


class MovingObject(GameObject):
    def __init__(self, position, velocity, *images):
        super().__init__(position, *images)
        self.velocity = velocity
        self.direction = 0

    @property
    def direction(self):
        return self.velocity.direction

    @direction.setter
    def direction(self, value):
        self.velocity.direction = value


