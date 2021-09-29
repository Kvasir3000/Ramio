import pygame.sprite
from pygame import Rect
from abc import ABC


TOLERANCE_RANGE = 300


class Collision(ABC):

    @staticmethod
    def in_tolerance(x, y):
        return abs(x - y) < TOLERANCE_RANGE

    @staticmethod
    def detect_single_x(actor, collider):
        if actor.velocity[0] < 0 and actor.rect.center[0] > collider.rect.center[0]:
            return True

        elif actor.velocity[0] > 0 and actor.rect.center[0] < collider.rect.center[0]:
            return True
        else:
            return False

    @staticmethod
    def detect_single_y(actor, collider):
        if actor.velocity[1] < 0 and actor.rect.center[1] > collider.rect.center[1]:
            return True
        elif actor.velocity[1] > 0 and actor.rect.center[1] < collider.rect.center[1]:
            return True
        else:
            return False

    @staticmethod
    def detect_single(actor, collider):
        if not pygame.sprite.collide_mask(actor, collider):
            return False, False
        else:
            x = Collision.detect_single_x(actor, collider)
            y = Collision.detect_single_y(actor, collider)
            return x, y

    @staticmethod
    def detect(actor, colliders):
        x, y = False, False
        for collider in colliders:
            if pygame.sprite.collide_mask(actor, collider):
                x = Collision.detect_single_x(actor, collider)
                y = Collision.detect_single_y(actor, collider)
        return x, y

    @staticmethod
    def detect_rotation(actor, colliders):
        for collider in colliders:
            if pygame.sprite.collide_mask(actor, collider):
                return True
