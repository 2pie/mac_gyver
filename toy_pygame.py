import pygame

pygame.init()

# window
win_width = 500
win_height = 500
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Toy")

# set up 
x = 50 # initial position of rectangle
y = 50
width = 40
height = 60
vel = 5 # velocity


# board: coordinates are from the top left, moving left = x -1, moving up: y+1. 0;0 is the top lef

# main loop
run = True # run variable, wether game is active or not
while run:
    pygame.time.delay(100) # clock of the game, in millisecond
    
    # manual quit condition
    for event in pygame.event.get():# list of all events that happened
        if event.type == pygame.QUIT:
            run = False

    # coordinates of an object is the top left point of this object
    # moving
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > vel: # vel and not zero because move by five units at a time
        x -= vel
    if keys[pygame.K_RIGHT] and x < win_width - vel - width:
        x += vel
    if keys[pygame.K_UP] and y > vel:
        y -= vel
    if keys[pygame.K_DOWN] and y < win_height - vel - width:
        y += vel

    # arguments: window, color(RBG), rectangle coord
    win.fill((0,0,0)) # erase past rectangle
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    # refresh display
    pygame.display.update()

pygame.quit()