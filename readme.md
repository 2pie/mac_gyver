---
This is a small game written in python with the pygame module. Help MacGyver escape !

# My process

1. I did the first three video courses on Python: "Démarrez votre projet avec python", "Découvrez la programmation orientée objet" et "Découvrez le fonctionnement des algorithmes". I wanted to have more practice before doing the last cours "Perfectionnez vous en Python".  I also did small projects: a "guess the number" game and a random password generator (not in github). This gave me some basics skills in python. 

2. I followed some tutorials to get discover pygame. I learned how to create a window, add a rectangle that can be moved with keyboard arrows, and I also learned to add walls that stops the movement of the rectangle. 
This last part was not easy, after some research, I found a method in a tutorial that worked. The idea of the method is, after a vertical (resp. horizontal) coordinate change, test if there is a collision with a wall. If there is a collision, set the moving vertical (resp horizontal) coordinates equal to the coordinates of the vertical (resp. horizontal edge of the wall.
It needed to use parent classes.
REVENIR LA DESSUS

From there I structured my code in an object oriented framework. The code was composed of three parts:
- Building the classes
- Creating the instances
- Main loop of the game

3. Once I had an idea of how pygame works, I designed the labyrinth. I used an spreadsheet software to draw the labyrinth in a grid, with wall blocks represented by ones. I then wrote a small R script to generate a csv file from this table that gives the x,y coordinates, width and height of each block (not in github,  because not necessary to run the program). I imported this file in my program to create the labyrinth. I added walls at the edge of the screen with the same class. 

4. I created the Guardian using the same class as for the walls. These object are not moving and in my program they don't "do" anything, they are just generated but have no methods in their classes. It is the player that does all the action, and therefore has several method in its class. This way of doing thing has the draw back that the code is concentrated in the player class, and therefore harder to read. However, I find it more intuitive to put all the interactions with other elements of the game in one function "update", than to split it in all classes. Intuitively, the player has the active part, he stops in front of a wall, he kills the guardian he picks up objects, while the other element have a passive role (they are picked, they are killed). It seemed therefore more logical to give the method ruling the interactions to the player.


# Classes

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