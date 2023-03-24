import colorgram
import turtle as t
import random

t.colormode(255)

rgb_colors = []
colors = colorgram.extract("painting.jpeg", 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

turtle = t.Turtle()
turtle.penup()
y = -200
for _ in range(10):
    turtle.setpos(-220, y)
    for _ in range(10):
        turtle.dot(20, random.choice(rgb_colors))
        turtle.forward(50)
    y += 50

screen = t.Screen()
screen.exitonclick()
