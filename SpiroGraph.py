import random
from turtle import Screen
import turtle as t

timmy = t.Turtle()
#Adjusting the range of color
t.colormode(255)

#Generating Random colors.
def Random_Colors():
    """This function generates random colors and return it as tuples."""
    r = random.randint(0 , 255)
    g = random.randint(0 , 255)
    b = random.randint(0 , 255)
    return (r, g, b)
    
#Adjusting the speed of turtle
timmy.speed("fastest")   
#Making a SpiroGraph   
def draw_spiral(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        timmy.color(Random_Colors())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)

draw_spiral(5)

screen = Screen()
screen.exitonclick()