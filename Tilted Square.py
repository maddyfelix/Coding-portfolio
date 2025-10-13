import turtle

colors = ["SlateGray1"]


loop = 0

while loop < 18:
    for each_color in colors:
        turtle.color(each_color, each_color)
        turtle.left(20)
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
        loop = loop + 1
