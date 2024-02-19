"""
Turtle Graphics
"""

import turtle
import random


def draw_square(x, y):
    """Draws a square with each side a length of 20 units."""
    global pen
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color(random.choice(colors))
    for _ in range(4):
        pen.forward(20)
        pen.left(90)


def draw_circle(x, y):
    """Draws a circle with radius 20 units."""
    global pen
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color(random.choice(colors))
    pen.circle(20)


def draw_triangle(x, y):
    """Draws an equilateral triangle with side length 20 units."""
    global pen
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color(random.choice(colors))
    for _ in range(3):
        pen.forward(20)
        pen.left(120)


def main():
    """Main function to create Turtle Graphics and draw a square."""
    # Setup
    screen = turtle.Screen()
    screen.setup(width=400, height=400)
    screen.title("Turtle Graphics")

    # Create a turtle instance
    global pen
    pen = turtle.Turtle()

    # Define available colours
    global colors
    colors = ["red", "green", "blue", "orange", "purple", "yellow", "cyan", "magenta"]

    # Draw shapes at random locations
    for _ in range(10000):
        shape = random.choice([draw_square, draw_circle, draw_triangle])
        x = random.randint(-180, 180)
        y = random.randint(-180, 180)
        shape(x, y)

    # Keep the window open until closed by the user
    screen.mainloop()


if __name__ == '__main__':
    main()
