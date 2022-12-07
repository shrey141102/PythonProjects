import colorgram
import turtle
import random
turtle.colormode(255)
new_colors = []
colors = colorgram.extract("Unknown.jpeg", 100)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    if r >= 210:
        continue
    tup = (r, g, b)
    new_colors.append(tup)

# color_list = [(197, 165, 117), (142, 80, 56), (59, 94, 119),
# (164, 152, 53), (136, 162, 181), (131, 34, 22), (69, 39, 32),
# (53, 117, 86), (192, 95, 78), (146, 177, 149), (19, 91, 68),
# (165, 143, 157), (31, 59, 76), (111, 75, 81), (128, 29, 33),
# (179, 204, 177), (71, 34, 36), (25, 82, 89), (89, 146, 127),
# (18, 69, 57), (41, 66, 90), (175, 94, 98), (179, 192, 205),
# (104, 129, 152), (67, 64, 59), (112, 135, 140), (175, 196, 206)]

turtle.penup()
turtle.hideturtle()
turtle.setheading(225)
turtle.fd(300)
turtle.setheading(0)
turtle.speed("fastest")

for i in range(1, 101):
    turtle.dot(20, random.choice(new_colors))
    turtle.fd(50)

    if i % 10 == 0:
        turtle.setheading(90)
        turtle.fd(50)
        turtle.setheading(180)
        turtle.fd(500)
        turtle.setheading(0)

screen = turtle.Screen()
screen.exitonclick()