import pygame
import random
import setup as su


class Item(pygame.sprite.Sprite):
    
    def __init__(self, other_blocks, pic):
        pygame.sprite.Sprite.__init__(self)

        xy_wall = [(int(row[0]), int(row[1])) for row in other_blocks]

        # generate item position
        while True:
            x_item = random.randint(0, su.N_SPRITES - 1)
            x_item = x_item * su.SPR_WIDTH
            y_item = random.randint(0, su.N_SPRITES - 1)
            y_item = y_item * su.SPR_HEIGHT
            xy_item = (x_item, y_item)

            # check if not in a wall
            match = False
            for wall in xy_wall:
                if xy_item == wall:
                    match = True
            if match is False:
                break

        self.image = pic
        self.rect = self.image.get_rect()
        self.rect.x = x_item
        self.rect.y = y_item
