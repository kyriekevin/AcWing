import os.path

import pygame
from player import Player
from wall import Wall
from star import Star
from target import Target
from utils.collided import collided_rect, collided_circle


class GameManager:
    def __init__(self, screen, level=1):
        self.screen = screen
        self.level = level

        self.player = None
        self.walls = pygame.sprite.Group()
        self.stars = pygame.sprite.Group()
        self.stars_cnt = 0
        self.targets = pygame.sprite.Group()

        self.eat_stars_sound = pygame.mixer.Sound("static/sounds/eat_stars.wav")
        self.eat_stars_sound.set_volume(0.3)

        self.success_sound = pygame.mixer.Sound("static/sounds/success.wav")
        self.success_sound.set_volume(0.3)

        self.load()

    def load_walls(self, walls):
        self.walls.empty()
        for x, y, width, height in walls:
            wall = Wall(x, y, width, height)
            wall.add(self.walls)

    def load_starts(self, stars):
        self.stars.empty()
        for x, y in stars:
            start = Star(x, y)
            start.add(self.stars)

    def load_targets(self, targets):
        self.targets.empty()
        for x, y in targets:
            target = Target(x, y)
            target.add(self.targets)

    def load_player(self, x, y, angle):
        if self.player:
            self.player.kill()
        self.player = Player(x, y, angle)

    def load(self):
        with open("static/maps/level_%d.txt" % self.level) as f:
            walls_cnt = int(f.readline())
            walls = []
            for i in range(walls_cnt):
                walls.append(map(int, f.readline().split()))
            self.load_walls(walls)

            self.stars_cnt = int(f.readline())
            stars = []
            for i in range(self.stars_cnt):
                stars.append(map(int, f.readline().split()))
            self.load_starts(stars)

            targets_cnt = int(f.readline())
            targets = []
            for i in range(targets_cnt):
                targets.append(map(int, f.readline().split()))
            self.load_targets(targets)

            x, y, angle = map(int, f.readline().split())
            self.load_player(x, y, angle)

    def next_level(self):
        self.level += 1
        if not os.path.isfile("static/maps/level_%d.txt" % self.level):
            return False

        self.load()

        return True

    def check_collide(self):
        if pygame.sprite.spritecollide(self.player, self.walls, False, collided_rect):
            self.player.crash()

        if pygame.sprite.spritecollide(self.player, self.stars, True, collided_circle):
            self.eat_stars_sound.play()
            self.stars_cnt -= 1

        if self.stars_cnt == 0:
            if pygame.sprite.spritecollide(self.player, self.targets, True, collided_circle):
                self.success_sound.play()
                return True

        return False

    def update(self):
        self.stars.update()
        self.stars.draw(self.screen)

        self.targets.update()
        self.targets.draw(self.screen)

        self.player.update()
        success = self.check_collide()
        self.screen.blit(self.player.image, self.player.rect)

        self.walls.update()
        self.walls.draw(self.screen)

        return success
