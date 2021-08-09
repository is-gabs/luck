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
from luck.commons.constants import SCREEN_HEIGHT
from luck.commons.constants import SCREEN_SIZE
from luck.commons.constants import SCREEN_WIDTH
from luck.commons.constants import TICK
from luck.player.hero import Hero
from luck.structure.ground import MetalBlock

RUNNING = True


pygame.init()
clock = Clock()
screen = display.set_mode(SCREEN_SIZE)
background = scale(load("luck/commons/backgrounds/space.jpg"), SCREEN_SIZE)


metal_block = MetalBlock(y=SCREEN_HEIGHT - BLOCK_SIZE)

ground_group = Group()

hero = Hero(floor=ground_group, y=SCREEN_HEIGHT / 2)

hero_group = GroupSingle(hero)


def build_ground():
    n_blocks = int(SCREEN_WIDTH / BLOCK_SIZE)

    for i in range(n_blocks):
        ground_group.add(
            MetalBlock(x=i * BLOCK_SIZE, y=SCREEN_HEIGHT - BLOCK_SIZE)
        )


build_ground()


while RUNNING:
    clock.tick(TICK)

    screen.blit(background, (0, 0))

    ground_group.draw(screen)
    hero_group.draw(screen)

    ground_group.update()
    hero_group.update()

    display.flip()

    for e in event.get():
        if e.type == locals.QUIT:
            pygame.quit()
            RUNNING = False
