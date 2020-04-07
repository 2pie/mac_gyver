import pygame
import csv
import random

pygame.init()

########################## Set up the game
 
win_width = 600
win_height = 600
n_item = 3
n_sprites = 15
sprite_height = win_height/n_sprites
sprite_width = win_width/n_sprites

win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Help MacGyver Escape!")
clock = 100 # clock of the game, in millisecond

# import walls data
wall_data = csv.reader(open('blocks.csv'), delimiter = ',')
wall_data = list(wall_data)

# import pictures
wall_pic = pygame.image.load('ressource/wall_tile.png')
guard_pic = pygame.image.load('ressource/Gardien.png')
mg_pic = pygame.image.load('ressource/MacGyver.png')


########################## Define classes

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y, width = sprite_width, height = sprite_height, pic = mg_pic):
        
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

    def __init__(self, x, y, width = sprite_width, height = sprite_height, pic = wall_pic, border = False):

        # Call the parent class
        pygame.sprite.Sprite.__init__(self)
        self.image = pic
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        if border == True:
            self.image = pygame.Surface([width, height])
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

class Item(pygame.sprite.Sprite):
    
    def __init__(self, other_blocks, color = (0, 255, 0)):
        pygame.sprite.Sprite.__init__(self)

        xy_wall = [(int(row[0]), int(row[1])) for row in wall_data]

        # generate item position
        while True:
            x_item = random.randint(0, n_sprites - 1)
            x_item = x_item * sprite_width
            y_item = random.randint(0, n_sprites - 1)
            y_item = y_item * sprite_height
            xy_item = (x_item, y_item)

            # check if not in a wall
            match = False
            for wall in xy_wall:
                if xy_item == wall:
                    match = True
            if match == False:
                break

        self.image = pygame.Surface([sprite_width, sprite_height])
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
for row in wall_data:
    block = Block(int(row[0]), int(row[1]), sprite_width, sprite_height, pic = wall_pic)
    wall_list.add(block)
    all_list.add(block)

# Borders of the screen
border_l = Block(0, 0, 0, 600, border = True)
border_u = Block(0, 0, 600, 0, border = True)
border_d = Block(0, 600, 600, 0, border = True)
border_r = Block(600, 0, 0, 600, border = True)
for border in (border_l, border_u, border_d, border_r):
    all_list.add(border)
    wall_list.add(border)


# Guardian
x_guard = 280
y_guard = 0
guard = Block(x_guard, y_guard, pic = guard_pic)
all_list.add(guard)
guard_list.add(guard) # need to have a list for spritecollide

# Items
n = 1
occupied_space = [wall_data, (x_guard, y_guard, sprite_width, sprite_height)]
while n <= n_item:
    item = Item(wall_data, color = (0, 255, 255))
    all_list.add(item)
    item_list.add(item)
    occupied_space.append((item.rect.x, item.rect.y, sprite_width, sprite_height))
    n += 1

# Player
mg = Player(280, 560, pic = mg_pic)
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