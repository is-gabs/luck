import pygame
from pygame import display
from pygame import event
from pygame import locals
from pygame.image import load
from pygame.sprite import Group
from pygame.sprite import GroupSingle
from pygame.time import Clock
from pygame.transform import scale

from luck.commons.constants import BLOCK_SIZE
from luck.commons.constants import HEIGHT
from luck.commons.constants import SCREEN_SIZE
from luck.commons.constants import TICK
from luck.commons.constants import WIDTH
from luck.player.hero import Hero
from luck.structure.ground import MetalBlock

pygame.init()
clock = Clock()
screen = display.set_mode(SCREEN_SIZE)
background = scale(load("luck/commons/backgrounds/space.jpg"), SCREEN_SIZE)


metal_block = MetalBlock(y=HEIGHT - BLOCK_SIZE)
hero = Hero()

ground_group = Group()
hero_group = GroupSingle(hero)


def build_ground():
    n_blocks = int(WIDTH / BLOCK_SIZE)

    for i in range(n_blocks):
        ground_group.add(MetalBlock(x=i * BLOCK_SIZE, y=HEIGHT - BLOCK_SIZE))


build_ground()


while True:
    clock.tick(TICK)

    screen.blit(background, (0, 0))

    ground_group.draw(screen)
    hero_group.draw(screen)

    ground_group.update()
    hero_group.update()

    display.update()

    for e in event.get():
        if e.type == locals.QUIT:
            pygame.quit()
