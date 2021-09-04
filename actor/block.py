from actor.primitive import Actor


class Brick(Actor):
    def __init__(self, position):
        super().__init__(position, 'Brickwall.png')