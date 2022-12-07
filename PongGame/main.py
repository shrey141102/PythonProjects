from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard


def lines_in_screen():
    # Making lines in between screen
    y = 300
    a = Turtle()
    a.hideturtle()
    a.penup()
    a.goto(0, y)
    a.pensize(5)
    a.color("white")
    while y >= -300:
        a.pendown()
        a.setheading(270)
        a.fd(50)
        a.penup()
        a.fd(40)
        y -= 90


lines_in_screen()
score = Scoreboard()
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONGGGGG")
screen.tracer(0)

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

# Detect collision with wall
    if ball.ycor() < -280 or ball.ycor() >= 280:
        ball.bounce_y()
# Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

# Detect when miss
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_add()
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_add()

screen.exitonclick()
