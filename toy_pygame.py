import pygame
import csv
import random

pygame.init()

########################## Set up the game
 
win_width = 600
win_height = 600
n_item = 3
# A AJOUTER !!!!
# n_sprites = 15
# sprite_width = win_height/n_sprites
# sprite_width = win_width/n_sprites

win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Help MacGyver Escape!")
clock = 100 # clock of the game, in millisecond

########################## Define classes

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height):
        
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
 
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([width, height])
        self.image.fill((255, 0, 0))
 
        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel = 10

        # Set move vector
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
            if self.score == n_item:
                global victory
                victory = True
            
            if self.score < n_item:
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

    def __init__(self, x, y, width, height, color = (0, 255, 0)):

        # Call the parent class
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Item(pygame.sprite.Sprite):
    
    def __init__(self, color = (0, 255, 0)):
        pygame.sprite.Sprite.__init__(self)

        xy_wall = []
        csv_reader = csv.reader(open('blocks.csv'), delimiter = ',')
        for row in csv_reader:
            xy_wall.append((int(row[0]), int(row[1])))

        while True:
        # generate item position
            x_item = random.randint(0, 14)
            x_item = x_item * 40
            y_item = random.randint(0, 14)
            y_item = y_item * 40
            xy_item = (x_item, y_item)

            # check if not in a wall
            match = False
            for wall in xy_wall:
                if xy_item == wall:
                    match = True
            if match == False:
                break

        width = 40
        height = 40
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x_item
        self.rect.y = y_item



########################## Create instances

all_list = pygame.sprite.Group()
wall_list = pygame.sprite.Group()
guard_list = pygame.sprite.Group()
item_list = pygame.sprite.Group()


# Walls
with open('blocks.csv') as csv_file: # REMOVE
    csv_reader = csv.reader(csv_file, delimiter = ',')
    for row in csv_reader:
        block = Block(int(row[0]), int(row[1]), int(row[2]), int(row[3]))
        wall_list.add(block)
        all_list.add(block)

# Border of the labyrinth
block_l = Block(0, 0, 0, 600)
block_u = Block(0, 0, 600, 0)
block_d = Block(0, 600, 600, 0)
block_r = Block(600, 0, 0, 600)
all_list.add(block_l)
all_list.add(block_u)
all_list.add(block_d)
all_list.add(block_r)
wall_list.add(block_l)
wall_list.add(block_u)
wall_list.add(block_d)
wall_list.add(block_r)

# Guardian
guard = Block(280, 0, 40, 40, (0, 0, 255))
all_list.add(guard)
guard_list.add(guard) # need to have a list for spritecollide

# Items METTRE EN CLASSE ?
n = 1
while n <= n_item:
    item = Item((0, 255, 255))
    all_list.add(item)
    item_list.add(item)
    n += 1

# Player
mg = Player(280, 560, 40, 40)
mg.walls = wall_list
mg.guard = guard_list
mg.item = item_list
all_list.add(mg)


########################## Main loop 

run = True 
victory = False
defeat = False
while run:
    pygame.time.delay(clock)
    
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
        win.blit(text, dest=(200,200))
        pygame.display.update()
        pygame.time.delay(1000)
        run = False
    
    if defeat:
        font = pygame.font.Font(pygame.font.get_default_font(), 36)
        text = font.render("You lose !", True, (255, 255, 255))
        win.blit(text, dest=(200,200))
        pygame.display.update()
        pygame.time.delay(1000)
        run = False

pygame.quit()