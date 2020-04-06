import pygame
import csv

pygame.init()

########################## Set up the game
 
win_width = 600
win_height = 600
# n_sprites = 15
# sprite_width = win_height/n_sprites
# sprite_width = win_width/n_sprites

win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Help MacGyver Escape!")
clock = 100 # clock of the game, in millisecond

########################## Create objects

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
        self.vel = 8

        # Set move vector
        self.change_x = 0
        self.change_y = 0
        self.walls = None
        self.guard = None
 
    def move(self, change_x, change_y):
        self.change_x += change_x
        self.change_y += change_y
        
    def update(self):
        " Update the player position."

        # Move left/right
        self.rect.x += self.change_x
 
        # Do player hit a wall?
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
            # If we are moving right, set our right side to the left side of
            # the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                self.rect.left = block.rect.right
 
        # Move up/down
        self.rect.y += self.change_y
 
        # Do player hit a wall?
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
 
            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom
        
        # Do player hit Guardien?
        guard_hit = pygame.sprite.spritecollide(self, self.guard, False)
        if guard_hit:
            global victory
            victory = True

            if self.change_x > 0:
                self.rect.right = guard.rect.left
            else:
                self.rect.left = guard.rect.right




            
class Wall(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height):

        # Call the parent class
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Guardian(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height):
 
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

########################## Create instances

all_list = pygame.sprite.Group()
block_list = pygame.sprite.Group()
guard_list = pygame.sprite.Group()


# Walls
with open('blocks.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    for row in csv_reader:
        block = Wall(int(row[0]), int(row[1]), int(row[2]), int(row[3]))
        block_list.add(block)
        all_list.add(block)

# Border of the labyrinth
block_l = Wall(0, 0, 0, 600)
block_u = Wall(0, 0, 600, 0)
block_d = Wall(0, 600, 600, 0)
block_r = Wall(600, 0, 600, 0)
all_list.add(block_l)
all_list.add(block_u)
all_list.add(block_d)
all_list.add(block_r)
block_list.add(block_l)
block_list.add(block_u)
block_list.add(block_d)
block_list.add(block_r)

# Guardian
guard = Guardian(280, 0, 40, 40)
all_list.add(guard)
guard_list.add(guard) # need to have a list for spritecollide

# Player
mg = Player(280, 560, 40, 40)
mg.walls = block_list
mg.guard = guard_list
all_list.add(mg)


########################## Main loop 

run = True 
victory = False
while run:
    pygame.time.delay(clock)
    
    # manual quit condition
    for event in pygame.event.get():# list of all events that happened
        if event.type == pygame.QUIT:
            run = False
        
        # moving
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


    
    all_list.update()

    # Draw
    win.fill((0,0,0))
    all_list.draw(win)
    pygame.display.update()

    if victory:
        font = pygame.font.Font(pygame.font.get_default_font(), 36)
        text = font.render("You win !", True, (255, 255, 255))
        win.blit(text, dest=(200,200))
        pygame.display.update()
        pygame.time.delay(1000)
        run = False
    


pygame.quit()