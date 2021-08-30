from game_object import GameObject
import pygame

class Player(GameObject):

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    super.x -= 1
                if event.key == pygame.K_RIGHT:
                    super.x += 1

    def generate_output(self):
        pass