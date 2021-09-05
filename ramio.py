import pygame
from actor.player import Player
from actor.block import Brick
from pygame import image, display, time
from pygame.sprite import Group


class Game:
    def __init__(self, width=1920, height=1080, fps=60):
        self.is_running = True
        self.fps = fps
        self.clock = time.Clock()
        self.actors = Group(Player((400, 100)))
        self.objects = Group(Brick((1000, 750)))
        self.objects.add(Brick((100, 750)))
        self.objects.add(Brick((800, 500)))
        self.background = image.load('Background.png')
        self.window = display.set_mode((width, height), pygame.FULLSCREEN)

    @property
    def player(self):
        return self.actors.sprites()[0]

    @property
    def events(self):
        return pygame.event.get()

    @property
    def pressed_keys(self):
        return pygame.key.get_pressed()

    def start(self):
        while self.is_running:
            self.display()
            self.update()
            self.process_input()

    def process_input(self):
        if self.received_quit_event():
            self.close()
        else:
            self.player.handle(self.pressed_keys)

    def received_quit_event(self):
        return any([event.type == pygame.QUIT for event in self.events])

    def display(self):
        self.window.blit(self.background, (0, 0))
        self.actors.draw(self.window)
        self.objects.draw(self.window)

    def update(self):
        self.clock.tick(self.fps)
        display.update()
        self.actors.update(*self.objects.sprites())

    def close(self):
        self.is_running = False


if __name__ == "__main__":
    pygame.init()
    Game().start()
    pygame.quit()

