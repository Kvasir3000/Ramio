class Velocity:
    def __init__(self, components):
        self.components = components

    def __getitem__(self, item):
        return self.components[item]
