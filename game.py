import pygame
import csv
import random

pygame.init()

# Set up the game
from setup import *

# Define classes
from classes import *


# Create instances

all_list = pygame.sprite.Group()
wall_list = pygame.sprite.Group()
guard_list = pygame.sprite.Group()
item_list = pygame.sprite.Group()


# Walls
for row in wall_data:
    block = Block(int(row[0]), int(row[1]), SPRITE_WIDTH, SPRITE_HEIGHT, pic = wall_pic)
    wall_list.add(block)
    all_list.add(block)

# Borders of the screen
border_l = Block(0, 0, 0, 600, pic = None, border = True)
border_u = Block(0, 0, 600, 0, pic = None, border = True)
border_d = Block(0, 600, 600, 0, pic = None, border = True)
border_r = Block(600, 0, 0, 600, pic = None, border = True)
for border in (border_l, border_u, border_d, border_r):
    all_list.add(border)
    wall_list.add(border)


# Guardian
x_guard = 280
y_guard = 0
guard = Block(x_guard, y_guard, SPRITE_WIDTH, SPRITE_HEIGHT, pic = guard_pic)
all_list.add(guard)
guard_list.add(guard) # need to have a list for spritecollide

# Items
n = 1
occupied_space = [wall_data, (x_guard, y_guard, SPRITE_WIDTH, SPRITE_HEIGHT)]
item_pics = [needle_pic, ether_pic, tube_pic]
while n <= N_ITEM:
    item = Item(wall_data, pic = item_pics[n-1])
    all_list.add(item)
    item_list.add(item)
    occupied_space.append((item.rect.x, item.rect.y, SPRITE_WIDTH, SPRITE_HEIGHT))
    n += 1

# Player
mg = Player(280, 560, SPRITE_WIDTH, SPRITE_HEIGHT, pic = mg_pic)
mg.walls = wall_list
mg.guard = guard_list
mg.item = item_list
all_list.add(mg)


# Main loop 

run = True 
victory = False
defeat = False
while run:
    pygame.time.delay(CLOCK)
    
    # Get events
    for event in pygame.event.get():# list of all events that happened
        if event.type == pygame.QUIT:
            run = False
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                mg.move(-mg.vel, 0)
            elif event.key == pygame.K_RIGHT:
                mg.move(mg.vel, 0)
            elif event.key == pygame.K_UP:
                mg.move(0, -mg.vel)
            elif event.key == pygame.K_DOWN:
                mg.move(0, mg.vel)
 
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                mg.move(mg.vel, 0)
            elif event.key == pygame.K_RIGHT:
                mg.move(-mg.vel, 0)
            elif event.key == pygame.K_UP:
                mg.move(0, mg.vel)
            elif event.key == pygame.K_DOWN:
                mg.move(0, -mg.vel)


    # Draw
    all_list.update()
    win.fill((0,0,0))
    all_list.draw(win)
    font = pygame.font.Font(pygame.font.get_default_font(), 24)
    text = font.render("Score = " + str(mg.score), True, (255, 255, 255))
    win.blit(text, dest = (0,0))
    pygame.display.update()

    if victory:
        font = pygame.font.Font(pygame.font.get_default_font(), 36)
        text = font.render("You win !", True, (255, 255, 255))
        win.blit(text, dest=(220,220))
        pygame.display.update()
        pygame.time.delay(1000)
        run = False
    
    if defeat:
        font = pygame.font.Font(pygame.font.get_default_font(), 36)
        text = font.render("You lose !", True, (255, 255, 255))
        win.blit(text, dest=(220,220))
        pygame.display.update()
        pygame.time.delay(1000)
        run = False

pygame.quit()