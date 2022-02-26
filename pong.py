import turtle
import winsound

from numpy import True_

wi = turtle.Screen()
wi.title("Pong by Prince Vanani")
wi.bgcolor("black")
wi.setup(height=600, width=800)
wi.tracer(0)  # it will stop windows from updating and speed up our game

# Score
score_a = 0
score_b = 0

# Create object for game
# object A means paddleA
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)
# object B means paddleB
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)
# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx=0.1
ball.dy=-0.1
# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# move paddle A up 
def paddle_a_up():
    y=paddle_a.ycor()
    y+=20
    paddle_a.sety(y)
# move paddle B down
def paddle_a_down():
    y=paddle_a.ycor()
    y-=20
    paddle_a.sety(y)
# move paddle B up 
def paddle_b_up():
    y=paddle_b.ycor()
    y+=20
    paddle_b.sety(y)
# move paddle B down
def paddle_b_down():
    y=paddle_b.ycor()
    y-=20
    paddle_b.sety(y)

#keyboard 
wi.listen()
wi.onkeypress(paddle_a_up,"w")
wi.onkeypress(paddle_a_down,"s")
wi.onkeypress(paddle_b_up,"Up")
wi.onkeypress(paddle_b_down,"Down")
# Main game loop for our game
while True:
    wi.update()
    #move ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    #border hit
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy*=-1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy*=-1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
    if ball.xcor()>390:
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0,0)
        ball.dx*=-1
    if ball.xcor()<-390:
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0,0)
        ball.dx*=-1
    if ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
        ball.dx *= -1 
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
    
    elif ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
        ball.dx *= -1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)