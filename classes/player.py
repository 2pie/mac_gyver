import pygame
import setup as su


class Player(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height, pic):
      
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        self.image = pic
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel = 10           # velocity should not exceed 10

        # attributes variables
        self.change_x = 0
        self.change_y = 0
        self.walls = None
        self.guard = None
        self.item = None
        self.score = 0

    def move(self, change_x, change_y):
        self.change_x += change_x
        self.change_y += change_y

    def update(self):

        # Move left/right
        self.rect.x += self.change_x
        
        # check if hit wall
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)

        # If hit wall update position
        for block in block_hit_list:
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                self.rect.left = block.rect.right
 
        # Move up/down
        self.rect.y += self.change_y
 
        # check if hit wall
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)

        # If hit wall update position
        for block in block_hit_list:
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom
        
        # Guardian interaction
        guard_hit = pygame.sprite.spritecollide(self, self.guard, False)
        if guard_hit:   # check if list is not empty
            
            if self.score == su.N_ITEM:
                self.victory = True
            
            if self.score < su.N_ITEM:
                self.defeat = True
        
        # Item interaction
        item_hit = pygame.sprite.spritecollide(self, self.item, True)
        if item_hit:
            self.score += 1
            