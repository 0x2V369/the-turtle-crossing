from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape('turtle')
        self.setheading(90)
        self.penup()
        self.reset_turtle()

    def move_forward(self):
        """
        Method to move the turtle forward with user input
        """
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)

    def reset_turtle(self):
        """
        Moves turtle to its starting position for game or new level start
        """
        self.goto(STARTING_POSITION)
