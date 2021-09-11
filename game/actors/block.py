from game.actors.primitive import Actor


class Brick(Actor):
    def __init__(self, x, y):
        super().__init__(x, y, 'Brickwall_small.png')