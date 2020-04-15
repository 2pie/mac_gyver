import pygame


class Block(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height, pic, border=False):

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