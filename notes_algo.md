---

I followed the tutorials to get started with pygame, seting up the screen, moving objects, placing boundaries.

I wrote a toy program to follow the video.
Since the tutorial was not very far from the type of game I had to design, I then progressively modify this program to create my game.

I followed the following steps

# Movement and boundaries
Create an empty screen, and a rectange that moves in this screen. Prevent rectangle from leaving the screen.


From the start, I used an Object oriented programming approach. I defined the object player.

Then I added a class Wall stopping player in case of collision.

Once I had the basic structure of the code (i.e. my player class and my wall class), I designed the shape of the labyrinth with blocks.

# Design of the board
The board must be 15 sprites long. I make it also 15 sprites wide to have a square. The basic sprite is based on the size of Macgyver's picture, slightly cropped to make it 40 pixel long. 
40*15 = 600 So the screen should be 600*600 pixels, composed of a 15*15 grid of sprites of size 40*40 pixels.

# Reference

## Starting with pygame
https://www.youtube.com/watch?v=i6xMBig-pP4
https://www.youtube.com/watch?v=2-DNswzCkqk

## Walls
https://www.youtube.com/watch?v=1aGuhUFwvXA
https://www.youtube.com/watch?v=8IRyt7ft7zg
http://programarcadegames.com/python_examples/show_file.php?file=move_with_walls_example.py


## Using OOP 
https://www.youtube.com/watch?v=xfnRywBv5VM


# Extensions
Simplifier le keydown/keyup? juste bouger si keydown ?
Image pour layrinthe
sons etc.
Clean code (border block, etc.)
python3: parenthesis apres print ?
changer le type des méthode et propriété