import pygame
import config
import math


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, angle):
        super().__init__()
        self.width = config.CAR_WIDTH
        self.height = config.CAR_HEIGHT
        self.forward_angle = angle
        self.image_source = pygame.image.load("static/img/car.png").convert()
        self.image = pygame.transform.scale(self.image_source, (self.width, self.height))
        self.image = pygame.transform.rotate(self.image, -self.forward_angle)
        self.image.set_colorkey("black")
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.last_time = pygame.time.get_ticks()
        self.delta_time = 0

        self.move_velocity_limit = 300
        self.move_velocity = 0
        self.move_acceleration = 500
        self.move_friction = 0.9

        self.rotate_velocity_limit = 100
        self.rotate_velocity = 0

        self.crash_sound = pygame.mixer.Sound("static/sounds/crash.mp3")
        self.crash_sound.set_volume(0.1)

        self.move_sound = pygame.mixer.Sound("static/sounds/move.mp3")
        # self.move_sound.set_volume(0.2)
        self.move_voice_channel = pygame.mixer.Channel(7)

    def update_delta_time(self):
        current_time = pygame.time.get_ticks()
        self.delta_time = (current_time - self.last_time) / 1000
        self.last_time = current_time

    def input(self):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_w]:
            self.move_velocity += self.move_acceleration * self.delta_time
            self.move_velocity = min(self.move_velocity, self.move_velocity_limit)
            if not self.move_voice_channel.get_busy():
                self.move_voice_channel.play(self.move_sound)
        elif key_pressed[pygame.K_s]:
            self.move_velocity -= self.move_acceleration * self.delta_time
            self.move_velocity = max(self.move_velocity, -self.move_velocity_limit)
            if not self.move_voice_channel.get_busy():
                self.move_voice_channel.play(self.move_sound)
        else:
            self.move_velocity = int(self.move_friction * self.move_velocity)
            if self.move_voice_channel.get_busy():
                self.move_voice_channel.stop()

        sign = 1 if self.move_velocity > 0 else -1

        if key_pressed[pygame.K_d]:
            self.rotate_velocity = self.rotate_velocity_limit * sign
        elif key_pressed[pygame.K_a]:
            self.rotate_velocity = -self.rotate_velocity_limit * sign
        else:
            self.rotate_velocity = 0

    def rotate(self, direction=1):
        self.forward_angle += self.rotate_velocity * self.delta_time * direction
        self.image = pygame.transform.scale(self.image_source, (self.width, self.height))
        self.image = pygame.transform.rotate(self.image, -self.forward_angle)
        self.image.set_colorkey("black")
        self.rect = self.image.get_rect(center=self.rect.center)

    def move(self, direction=1):
        if direction == 1 and abs(self.move_velocity) > 50:
            self.rotate(direction)

        vx = self.move_velocity * math.cos(math.pi * self.forward_angle / 180) * direction
        vy = self.move_velocity * math.sin(math.pi * self.forward_angle / 180) * direction
        self.rect.x += vx * self.delta_time
        self.rect.y += vy * self.delta_time

        if direction == -1 and abs(self.move_velocity) > 50:
            self.rotate(direction)

    def update(self):
        self.update_delta_time()
        self.input()
        self.move()

    def crash(self):
        self.crash_sound.play()
        self.move(-1)
        if self.move_velocity >= 0:
            self.move_velocity = min(-self.move_velocity, -50)
        else:
            self.move_velocity = max(-self.move_velocity, 50)
        self.rotate_velocity *= -1
