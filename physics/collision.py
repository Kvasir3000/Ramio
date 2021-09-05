from pygame import Rect
from abc import ABC


class Collision(ABC):
    RADIUS = 10

    @staticmethod
    def in_radius(x, y):
        return abs(x - y) < Collision.RADIUS

    @staticmethod
    def detect_single(actor, collider, direction='any'):
        if direction == 'any':
            return True
        elif direction == 'left':
            return Collision.in_radius(actor.next_rect.left, collider.rect.right)
        elif direction == 'right':
            return Collision.in_radius(actor.next_rect.right, collider.rect.left)
        elif direction == 'bottom':
            return Collision.in_radius(actor.next_rect.bottom, collider.rect.top)
        elif direction == 'top':
            return Collision.in_radius(actor.next_rect.top, collider.rect.bottom)
        else:
            raise Exception(f'Unknown direction: {direction}')

    @staticmethod
    def detect(actor, colliders, direction='any'):
        for collider in colliders:
            if Rect.colliderect(actor.next_rect, collider.rect):
                return Collision.detect_single(actor, collider, direction)
