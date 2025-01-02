# Term_Project_game

### Introduction to the Project ###
Github link to see the project files: https://github.com/Chan661/TP_game

Project Name: Play this VolleyBall Game!!
-----------------------------------------------------
Description

This is a simple two-person competition game whose key supporting feature is the ball-arm collision and the modelled projectile motion of the ball that involves air resistance.

There are also simple user interfaces that includes a menu which allows the users to pause and resume the current game, exit the game, start a new ball, and provides a brief yet detailed rule and game guidance.

The ball-arm collision changes the direction of the velocity of the ball and preserves its speed through linear algebra computation.

User can use keys groups 'wasder' and './[arrow keys] ' to control the movement of the players' positions and their arms, and making the ball dropping on the opponent's court or make them serve the ball outside the canvas earns players their point. More than three touches, which is a key element in normal volleyball game, increments corresponding points.

The program uses cmu_graphic's app model to model the game. In the game, app.paused and app.playing manage the stage and mouse presses manages usage of UI.
-----------------------------------------------------
### How to run the Project ###

Environment:
VSCode
Python 3.10.x or 3.11.x  - Site to download: https://www.python.org/downloads/
cmu graphic packages: run pip install cmu-graphics in the terminal with the directory where this project will be compiled and runned

Unpack the zip file to the directory where cmu graphics locates. The required files are imported as the headers says. Make sure that they are in the same directory.

To test the use of UI, as description describes, app.paused and app.playing can be helpful to test if the buttons work correctly.
