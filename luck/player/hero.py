import pygame
from pygame import key
from pygame.image import load
from pygame.sprite import Group
from pygame.sprite import Sprite
from pygame.transform import flip
from pygame.transform import scale

from luck.commons.constants import Directions
from luck.commons.constants import FLOOR_Y
from luck.commons.constants import GRAVITY
from luck.commons.constants import PLAYER_HEIGHT
from luck.commons.constants import SCREEN_WIDTH


class Hero(Sprite):
    def __init__(self, floor: Group, x: int = 0, y: int = 0) -> None:
        super().__init__()

        self.image = scale(
            load("luck/player/hero.png"), (PLAYER_HEIGHT, PLAYER_HEIGHT)
        )
        self.rect = self.image.get_rect()
        self.floor = floor

        self.height = PLAYER_HEIGHT
        self.direction = Directions.RIGHT

        self.rect.x = x
        self.rect.y = y

        self.speed_x = 9
        self.speed_y = 0

        self.mass = 2

        self.is_jumping = True

    def update(self) -> None:
        keys = key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.increase_x(self.speed_x * -1)
            if self.direction == Directions.RIGHT:
                self.direction = Directions.LEFT
                self.image = flip(self.image, True, False)
        if keys[pygame.K_RIGHT]:
            self.increase_x(self.speed_x)
            if self.direction == Directions.LEFT:
                self.direction = Directions.RIGHT
                self.image = flip(self.image, True, False)
        if keys[pygame.K_UP]:
            self.jump()

        if self.is_jumping:
            force = GRAVITY * 2 * self.mass * (self.speed_y * self.speed_y)

            if self.speed_y < 0:
                force = force * -1

            if self.rect.y - force > FLOOR_Y:
                self.rect.y = FLOOR_Y + 1
            else:
                self.rect.y -= force

            self.speed_y -= 1

            if self.is_on_floor:
                self.speed_y = 6
                self.is_jumping = False

    def jump(self):
        if self.is_on_floor:
            self.is_jumping = True

    def increase_x(self, speed):
        self.rect.x += speed
        if self.rect.x > SCREEN_WIDTH - 20:
            self.rect.x = SCREEN_WIDTH - 20
        elif self.rect.x < -10:
            self.rect.x = -10

    @property
    def is_on_floor(self):
        return any(
            self.rect.colliderect(block) for block in self.floor.sprites()
        )
