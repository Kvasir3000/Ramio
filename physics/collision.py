import pygame as pg
from abc import ABC


class Collision(ABC):

    @staticmethod
    def detect(direction, player, actors):
        player_rect = player.rect.move(player.velocity[0], player.velocity[1])
        for actor in actors:
            if pg.Rect.colliderect(player_rect, actor):
                if direction == 'left':
                    return abs(player_rect.left - actor.rect.right) < 10
                elif direction == 'right':
                    return abs(player_rect.right - actor.rect.left) < 10
                elif direction == 'bottom':
                    return abs(player.rect.bottom - actor.rect.top) < 10
                elif direction == 'top':
                    return abs(player_rect.top - actor.rect.bottom) < 10
