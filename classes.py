import pygame
import random

from setup import *


class Player(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height, pic):
        
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
 
        self.image = pic
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel = 10 # velocity should not exceed 10, otherwise not enough precision

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
 
        # Do player hit a wall?
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
            # If we are moving right, set our right side to the left side of the wall we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                self.rect.left = block.rect.right
 
        # Move up/down
        self.rect.y += self.change_y
 
        # Do player hit a wall?
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom
        
        # Guardian interaction
        guard_hit = pygame.sprite.spritecollide(self, self.guard, False)
        if guard_hit:
            if self.score == N_ITEM:
                global victory
                victory = True
            
            if self.score < N_ITEM:
                global defeat
                defeat = True

            if self.change_x > 0:
                self.rect.right = guard.rect.left
            else:
                self.rect.left = guard.rect.right
        
        # Item interaction
        item_hit = pygame.sprite.spritecollide(self, self.item, True)
        if item_hit:
            self.score += 1
            
class Block(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height, pic, border = False):

        # Call the parent class
        pygame.sprite.Sprite.__init__(self)

        if border == False:
            self.image = pic
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

        elif border == True:
            self.image = pygame.Surface([width, height])
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

class Item(pygame.sprite.Sprite):
    
    def __init__(self, other_blocks, pic):
        pygame.sprite.Sprite.__init__(self)

        xy_wall = [(int(row[0]), int(row[1])) for row in other_blocks]

        # generate item position
        while True:
            x_item = random.randint(0, N_SPRITES - 1)
            x_item = x_item * SPRITE_WIDTH
            y_item = random.randint(0, N_SPRITES - 1)
            y_item = y_item * SPRITE_HEIGHT
            xy_item = (x_item, y_item)

            # check if not in a wall
            match = False
            for wall in xy_wall:
                if xy_item == wall:
                    match = True
            if match == False:
                break

        self.image = pic
        self.rect = self.image.get_rect()
        self.rect.x = x_item
        self.rect.y = y_item

