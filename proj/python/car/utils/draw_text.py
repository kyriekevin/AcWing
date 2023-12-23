import pygame


def draw_text(screen, text, size, x, y):
    font = pygame.font.SysFont(pygame.font.get_default_font(), size)
    image = font.render(text, True, "white")
    rect = image.get_rect()
    rect.center = (x, y)
    screen.blit(image, rect)
