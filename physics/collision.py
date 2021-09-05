from pygame import Rect
from abc import ABC


class Collision(ABC):
    TOLERANCE = 10

    @staticmethod
    def in_tolerance(x, y):
        return abs(x - y) < Collision.TOLERANCE

    @staticmethod
    def detect_single(actor, collider, dir='any'):
        if dir == 'any':
            return True
        elif dir == 'left':
            return Collision.in_tolerance(actor.next_rect.left, collider.rect.right)
        elif dir == 'right':
            return Collision.in_tolerance(actor.next_rect.right, collider.rect.left)
        elif dir == 'bottom':
            return Collision.in_tolerance(actor.next_rect.bottom, collider.rect.top)
        elif dir == 'top':
            return Collision.in_tolerance(actor.next_rect.top, collider.rect.bottom)
        else:
            raise Exception(f'Unknown direction: {dir}')

    @staticmethod
    def detect(actor, colliders, dir='any'):
        for collider in colliders:
            if Rect.colliderect(actor.next_rect, collider.rect):
                return Collision.detect_single(actor, collider, dir)
