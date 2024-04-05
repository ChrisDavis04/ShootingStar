Import all the necessary modules to draw assets from such as pyGame the SimpleGE as well as random for the randomness of the falling object.
Start off by creating a class called "Game" that runs via the simpleGE.scene that will actually run the game
  Initialize all the attributes of the class
    Set the background image for the game
    Create attributes for the time so that the player starts off with 10 seconds to play the game. Create another attribute that holds the score and have the score start at 0.
    Create attributes for each sprite and put them all in a list so that they actually appear in the game
    Have it so that there can be many falling objects at a time by create attributes that are an empty list that can be appended with the amount of falling objects specified.
  define the processes of the game itself
    whenever the player collides with certain objects add 1 to the score and have this information displayed on the ui. Have the object that collided with the player reset so that it moves back to the top of the screen. Also create special objects that when collided with they either add or subtract from the user's time.
    Have the time left in the game be rapidly updating and that when the time reaches 0 the game will stop.

Import the player sprite by creating another class using the simpleGE.sprite
  initialize all of its attributes such as it's size, position as well as how fast it will move. Set the movement speed as a variable so that it can easily be changed later on.
  Within the class for the player character make it move horizontally on the bottom of the screen. Set it so that whenever the left arrow key is pressed the character will move left and when the right arrow key is pressed the character will move right.
  The speed of this movement will be entirely decided by the value of the movement speed variable.

Have objects falling from the top of the screen that will drop at different speeds
Create new classes for each different type of falling object
  Initialize all of its attributes such as it's size, position and have it so when it reaches the bottom of the screen it will automotically go back to the top and fall once more
  define how these objects will reset
    set the objects to start falling at a random place on the width of the screen and so that the objects will fall at different speeds as well


When the game is running, have lables that show the amount of time left as well as the player's current score. Have these lables have a clear background so textbox sprites can be set behind them

Create an intro screen for the that gives basic instructions and has buttons that allows for the player to start or quit the game
Establish a class for the intro screen and initialize all of its attributes
  set the current status of the game to be "quit" and use this variable to determine whether the game is being played or not
  create an attribute that will display the player's previous score when playing the game

  create buttons for starting and quiting the game

  define the processes of the intro screen
    when the play button is clicked set the status of the game to be "start"
    when the quit button is clicked set the status of the game to be "quit"



define main
  establish a while loop so that if first starts off on the intro screen showing the instructions as well as the score
    if the status of the game is set to start
      start the game
    else
      stop the game and set the while loop to false
