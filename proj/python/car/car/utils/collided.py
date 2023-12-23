import pygame
import math


def collided_rect(a, b):
    p = []
    for i, j in [(1, -1), (1, 1), (-1, 1), (-1, -1)]:
        t = pygame.Vector2(i * a.width / 2 * 0.8, j * a.height / 2 * 0.8).rotate(a.forward_angle)
        p.append(t + a.rect.center)

    for i in range(4):
        x = p[i]
        y = p[(i + 1) % 4]
        if b.rect.clipline(x, y):
            return True

    p.clear()
    for i, j in [(1, -1), (1, 1), (-1, 1), (-1, -1)]:
        t = pygame.Vector2(i * a.width / 2, j * a.height / 2 * 0.2).rotate(a.forward_angle)
        p.append(t + a.rect.center)

    for i in range(4):
        x = p[i]
        y = p[(i + 1) % 4]
        if b.rect.clipline(x, y):
            return True

    return False


def collided_circle(a, b):
    x1, y1 = a.rect.center
    x2, y2 = b.rect.center
    dx, dy = x2 - x1, y2 - y1
    if math.sqrt(dx * dx + dy * dy) < 50:
        return True

    return False
