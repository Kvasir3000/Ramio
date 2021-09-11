from game.actors.primitive import MovingActor, AnimatedActor, ManipulatedActor
from abc import ABC


class Puppet(MovingActor, AnimatedActor, ABC):
    def __init__(self, x, y, velocity, *images):
        MovingActor.__init__(self, x, y, velocity, images[0])
        AnimatedActor.__init__(self, x, y, *images)


class Marionette(Puppet, ManipulatedActor, ABC):
    def __init__(self, x, y, velocity, *images):
        Puppet.__init__(self, x, y, velocity, *images)
