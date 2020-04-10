import pygame
import setup as su
import classes as cl

pygame.init()

# CREATE INSTANCES

all_list = pygame.sprite.Group()
wall_list = pygame.sprite.Group()
guard_list = pygame.sprite.Group()
item_list = pygame.sprite.Group()


# Walls
for row in su.wall_data:
    block = cl.Block(
        int(row[0]), int(row[1]), su.SPR_WIDTH, su.SPR_HEIGHT, pic=su.wall_pic
        )
    wall_list.add(block)
    all_list.add(block)

# Borders of the screen
border_l = cl.Block(0, 0, 0, 600, pic=None, border=True)
border_u = cl.Block(0, 0, 600, 0, pic=None, border=True)
border_d = cl.Block(0, 600, 600, 0, pic=None, border=True)
border_r = cl.Block(600, 0, 0, 600, pic=None, border=True)
for border in (border_l, border_u, border_d, border_r):
    all_list.add(border)
    wall_list.add(border)


# Guardian
guard = cl.Block(
    su.X_GUARD, su.Y_GUARD, su.SPR_WIDTH, su.SPR_HEIGHT, pic=su.guard_pic
    )
all_list.add(guard)
guard_list.add(guard)       # need to have a list for spritecollide

# Items
n = 1
occupied_space = [su.wall_data]
occupied_space.append((su.X_GUARD, su.Y_GUARD, su.SPR_WIDTH, su.SPR_HEIGHT))
item_pics = [su.needle_pic, su.ether_pic, su.tube_pic]
while n <= su.N_ITEM:
    item = cl.Item(su.wall_data, pic=item_pics[n-1])
    all_list.add(item)
    item_list.add(item)
    occupied_space.append(
        (item.rect.x, item.rect.y, su.SPR_WIDTH, su.SPR_HEIGHT)
        )
    n += 1

# Player
mg = cl.Player(
    su.X_PLAYER, su.Y_PLAYER, su.SPR_WIDTH, su.SPR_HEIGHT, pic=su.mg_pic
    )
mg.walls = wall_list
mg.guard = guard_list
mg.item = item_list
mg.victory = False
mg.defeat = False
all_list.add(mg)


### MAIN LOOP

run = True
while run:
    pygame.time.delay(su.CLOCK)
    
    # Get events
    for event in pygame.event.get():    # list of all events that happened
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

    for i in range(0, su.N_SPRITES*2):  # because tile is only 20 px
        i = i*su.SPR_WIDTH/2
        for j in range(0, su.N_SPRITES*2):
            j = j*su.SPR_HEIGHT/2
            su.win.blit(su.floor_pic, dest=(i, j))

    all_list.draw(su.win)
    font = pygame.font.Font(pygame.font.get_default_font(), 24)
    text = font.render("Score = " + str(mg.score), True, (255, 255, 255))
    su.win.blit(text, dest=(0, 0))
    pygame.display.update()

    if mg.victory:
        font = pygame.font.Font(pygame.font.get_default_font(), 36)
        text = font.render("You win !", True, (255, 255, 255))
        su.win.blit(text, dest=(220, 220))
        pygame.display.update()
        pygame.time.delay(1000)
        run = False
    
    if mg.defeat:
        font = pygame.font.Font(pygame.font.get_default_font(), 36)
        text = font.render("You lose !", True, (255, 255, 255))
        su.win.blit(text, dest=(220, 220))
        pygame.display.update()
        pygame.time.delay(1000)
        run = False

pygame.quit()
