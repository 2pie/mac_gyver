import pygame


class Block(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height, pic, border=False):
        '''Initialize the Block instance

        Parameters:
        x,y : position of the block
        width, height: size of the block
        pic: picture for the block
        border: Is the block used as border of the screen ? (default = No)
        '''

        # Call the parent class
        pygame.sprite.Sprite.__init__(self)

        if border is False:
            self.image = pic
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

        elif border is True:
            self.image = pygame.Surface([width, height])
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
