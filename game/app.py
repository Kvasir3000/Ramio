import pygame
import pygame as pg
from game.actors.ramio import Ramio
from game.actors.block import Brick
from pygame.sprite import Group, GroupSingle


class Game:
    def __init__(self, width=1920, height=1080, fps=60):
        pg.init()
        self.is_running = True
        self.fps = fps
        self.clock = pg.time.Clock()
        self.actors = Group(Brick(300, 500))
        self.player = GroupSingle(Ramio(400, 100))
        self.window = pg.display.set_mode((width, height), pygame.FULLSCREEN)
        pygame.mouse.set_visible(True)

    @property
    def events(self):
        return pg.event.get()

    @property
    def pressed_keys(self):
        return pg.key.get_pressed()

    def start(self):

        pygame.mouse.set_pos(1000, 1000)
        while self.is_running:
            self.display()
            self.update()
            self.process_input()

    def process_input(self):
        if self.received_quit_event() or self.pressed_keys[pygame.K_ESCAPE]:
            self.close()
        else:
            self.player.sprite.respond(self.pressed_keys)

    def received_quit_event(self):
        return any([event.type == pg.QUIT for event in self.events])

    def display(self):
        self.window.fill((0, 0, 0))
        self.player.draw(self.window)
        self.actors.draw(self.window)

    def update(self):
        self.clock.tick(self.fps)
        pg.display.update()
        self.player.update(self.actors.sprites())

    def close(self):
        pg.quit()
        self.is_running = False
