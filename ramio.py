import pygame
from actor.player import Player
from actor.block import Brick
from pygame import image, display, time
from pygame.sprite import Group, GroupSingle


class Game:
    def __init__(self, width=1920, height=500, fps=60):
        self.is_running = True
        self.fps = fps
        self.clock = time.Clock()
        self.player = GroupSingle(Player(400, 900))
        self.actors = Group(Brick(300, 500))
        self.window = display.set_mode((width, height), pygame.FULLSCREEN)

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
            self.player.sprite.handle(self.pressed_keys)

    def received_quit_event(self):
        return any([event.type == pygame.QUIT for event in self.events])

    def display(self):
        self.window.fill((0, 0, 0))
        self.player.draw(self.window)
        self.actors.draw(self.window)

    def update(self):
        self.clock.tick(self.fps)
        display.update()
        self.player.update(self.actors.sprites())

    def close(self):
        self.is_running = False


if __name__ == "__main__":
    pygame.init()
    Game().start()
    pygame.quit()

