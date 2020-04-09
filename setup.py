import pygame
import csv

WIN_WIDTH = 600
WIN_HEIGHT = 600
N_ITEM = 3
N_SPRITES = 15
SPR_HEIGHT = WIN_HEIGHT/N_SPRITES
SPR_WIDTH = WIN_WIDTH/N_SPRITES
CLOCK = 100      # clock of the game, in millisecond


win = pygame.display.set_mode((WIN_HEIGHT, WIN_HEIGHT))
pygame.display.set_caption("Help MacGyver Escape!")

# import walls data
wall_data = csv.reader(open('blocks.csv'), delimiter=',')
wall_data = list(wall_data)

# import pictures
wall_pic = pygame.image.load('ressource/wall_tile.png')
guard_pic = pygame.image.load('ressource/Gardien.png')
mg_pic = pygame.image.load('ressource/MacGyver.png')
needle_pic = pygame.image.load('ressource/aiguille2.png')
ether_pic = pygame.image.load('ressource/ether.png')
tube_pic = pygame.image.load('ressource/tube_plastique.png')

# Position player and guardian
X_GUARD = 280
Y_GUARD = 0
X_PLAYER = 280
Y_PLAYER = 560
