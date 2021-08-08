from pygame.image import load
from pygame.sprite import Sprite
from pygame.transform import scale

from luck.commons.constants import BLOCK_SIZE


class MetalBlock(Sprite):
    def __init__(self, x: int = 0, y: int = 0) -> None:
        super().__init__()

        self.image = scale(
            load("luck/structure/metal_tile_flat.png"),
            (BLOCK_SIZE, BLOCK_SIZE),
        )

        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

    def update(self) -> None:
        ...
