__author__: "Tomas Sabol"

"----------------------------"

import turtle


# screen config
screen = turtle.Screen()
screen.title("Pong game")
screen.bgcolor("black")
screen.setup(width=1000, height=600)


# left pad
left_pad = turtle.Turtle()
left_pad.speed(0)
left_pad.color("white")
left_pad.shape("square")
left_pad.shapesize(stretch_wid=6, stretch_len=2)
left_pad.penup()
left_pad.goto(-400, 0)


# right pad
right_pad = turtle.Turtle()
right_pad.speed(0)
right_pad.color("white")
right_pad.shape("square")
right_pad.shapesize(stretch_wid=6, stretch_len=2)
right_pad.penup()
right_pad.goto(400, 0)


# ball
ball = turtle.Turtle()
ball.speed(30)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 5
ball.dy = -5


# score
left_player = 0
right_player = 0


# display score
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("Left_player : 0 Right_player: 0", align="center", font=("SF", 24, "normal"))


# move pads vertically

def move_leftpad_up():
    y = left_pad.ycor()
    y += 20
    left_pad.sety(y)


def move_leftpad_down():
    y = left_pad.ycor()
    y -= 20
    left_pad.sety(y)


def move_rightpad_up():
    y = right_pad.ycor()
    y += 20
    right_pad.sety(y)


def move_rightpad_down():
    y = right_pad.ycor()
    y -= 20
    right_pad.sety(y)


# key bind
screen.listen()

screen.onkeypress(move_leftpad_up, "w")
screen.onkeypress(move_leftpad_down, "s")
screen.onkeypress(move_rightpad_up, "Up")
screen.onkeypress(move_rightpad_down, "Down")


while True:
    screen.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Checking borders
    if ball.ycor() > 280:
        ball.sety(280)
        ball.dy *= -1

    if ball.ycor() < -280:
        ball.sety(-280)
        ball.dy *= -1

    if ball.xcor() > 500:
        ball.goto(0, 0)
        ball.dy *= -1
        left_player += 1
        score.clear()
        score.write("Left_player : {} Right_player: {}".format(
            left_player, right_player), align="center",
            font=("Courier", 24, "normal"))

    if ball.xcor() < -500:
        ball.goto(0, 0)
        ball.dy *= -1
        right_player += 1
        score.clear()
        score.write("Left_player : {} Right_player: {}".format(
            left_player, right_player), align="center",
            font=("Courier", 24, "normal"))

    # Paddle ball collision
    if (ball.xcor() > 360 and ball.xcor() < 370) \
            and (ball.ycor() < right_pad.ycor() + 40 
            and ball.ycor() > right_pad.ycor() - 40):
        ball.setx(360)
        ball.dx *= -1

    if (ball.xcor() < -360 and ball.xcor() > -370)\
            and (ball.ycor() < left_pad.ycor() + 40 
                 and ball.ycor() > left_pad.ycor() - 40):
        ball.setx(-360)
        ball.dx *= -1
