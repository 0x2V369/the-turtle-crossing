from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.cars_on_screen = []
        self.move_in_pixels = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = randint(1,6)
        if random_chance == 1:
            car = Turtle()
            car.shape("square")
            car.shapesize(1, 2)
            car.penup()
            car.color(choice(COLORS))
            x_cor_random = randint(300, 350)
            y_cor_random = randint(- 250, 250)
            car.setheading(180)
            car.goto(x_cor_random, y_cor_random)
            self.cars_on_screen.append(car)

    def move_cars(self):
        """Method to move all cars across the screen"""
        for car in self.cars_on_screen:
            car.forward(self.move_in_pixels)

    def clear_old_cars(self):
        """Clears old cars from the screen once they are out of screen bounds"""
        for car in self.cars_on_screen:
            if car.xcor() < - 300:
                car.ht()
                self.cars_on_screen.remove(car)

    def increase_car_speed(self):
        """With each new level car speed is increased"""
        self.move_in_pixels += MOVE_INCREMENT
