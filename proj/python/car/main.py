import pygame
import config
from game_manager import GameManager
from utils.draw_text import draw_text

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
clock = pygame.time.Clock()

pygame.display.set_caption("Car")

pygame.mixer.music.load("static/sounds/bgm.wav")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)

game_manager = GameManager(screen, 1)

running = True
success_finished = False
success_time = -1

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif success_finished and event.type == pygame.KEYDOWN:
            running = False

    screen.fill("black")

    if success_finished:
        draw_text(screen, "Win!", 200, config.SCREEN_WIDTH // 2, config.SCREEN_HEIGHT // 2)
    else:
        if success_time != -1:
            if pygame.time.get_ticks() - success_time > 2000:
                has_next = game_manager.next_level()
                if not has_next:
                    success_finished = True
                    continue
                success_time = -1

        if game_manager.update():
            success_time = pygame.time.get_ticks()

    pygame.display.flip()
    clock.tick(config.FPS)

pygame.quit()
