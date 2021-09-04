from actor.primitive import MovingActor, AnimatedActor, ManipulatedActor
from abc import ABC


class Puppet(MovingActor, AnimatedActor, ABC):
    def __init__(self, position, velocity, *images):
        MovingActor.__init__(self, position, velocity, images[0])
        AnimatedActor.__init__(self, position, *images)


class Marionette(Puppet, ManipulatedActor, ABC):
    def __init__(self, position, velocity,* images):
        Puppet.__init__(self, position, velocity, *images)
