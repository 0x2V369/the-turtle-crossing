from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.ht()
        self.level = 1
        self.penup()
        self.color("black")
        self.goto(-270, 260)
        self.update_score_board()

    def update_score_board(self):
        """Print the correct level on the screen when game starts or new level is achieved"""
        self.clear()
        self.write(f"Level: {self.level}", font=FONT)

    def new_level(self):
        """Update level text on the screen"""
        self.level += 1
        self.update_score_board()

    def game_over(self):
        """Print the GAME OVER message in the middle of the screen"""
        self.teleport(0, 0)
        self.write("GAME OVER", align='center', font=FONT)
