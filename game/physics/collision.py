from pygame import Rect
from abc import ABC

TOLERANCE_RANGE = 10


class Collision(ABC):

    @staticmethod
    def in_tolerance(x, y):
        return abs(x - y) < TOLERANCE_RANGE

    @staticmethod
    def detect_single(actor, collider, direction='any'):
        if not Rect.colliderect(actor.next_rect, collider.rect):
            return False
        if direction == 'any':
            return True
        elif direction == 'left':
            return Collision.in_tolerance(actor.next_rect.left, collider.rect.right)
        elif direction == 'right':
            return Collision.in_tolerance(actor.next_rect.right, collider.rect.left)
        elif direction == 'bottom':
            return Collision.in_tolerance(actor.next_rect.bottom, collider.rect.top)
        elif direction == 'top':
            return Collision.in_tolerance(actor.next_rect.top, collider.rect.bottom)
        else:
            raise ValueError(f'Unknown direction: {direction}')

    @staticmethod
    def detect(actor, colliders, direction='any'):
        return any([Collision.detect_single(actor, collider, direction) for collider in colliders])
