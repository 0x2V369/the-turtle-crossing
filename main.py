import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Initialize and set up the main game screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Initialize the player, scoreboard and car_manager objects
player = Player()
score_board = Scoreboard()
car_manager = CarManager()

# Receive user input
screen.listen()
screen.onkey(player.move_forward, " Up")

game_is_on = True

# Main loop for the game
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.move_cars()
    car_manager.clear_old_cars()
    car_manager.create_car()

    # Detect if turtle is hit by a car
    for car in car_manager.cars_on_screen:
        if car.distance(player) < 20:
            game_is_on = False
            score_board.game_over()

    # Detect if a level is passed
    if player.ycor() > 250:
        score_board.new_level()
        player.reset_turtle()
        car_manager.increase_car_speed()

# Close the screen once clicked on it
screen.exitonclick()
