import turtle
import time
from random import randrange

def Pong():
 COL1=['navy blue','dark green','pink','black']
 COL2=['yellow','orange','blue','white']
 i=randrange(0,4)
 col1=COL1[i]
 col2=COL2[i]

 wn = turtle.Screen()
 wn.title("PONG")
 wn.bgcolor(col1)
 wn.setup(width=1000, height=600)
 wn.tracer(0)

 scoreA = 0
 scoreB = 0

 #pad A
 padA = turtle.Turtle()
 padA.speed(0)
 padA.shape("square")
 padA.color(col2)
 padA.shapesize(stretch_wid=6, stretch_len=1)
 padA.penup()
 padA.goto(-450,0)

 #pad B
 padB = turtle.Turtle()
 padB.speed(0)
 padB.shape("square")
 padB.color(col2)
 padB.shapesize(stretch_wid=6, stretch_len=1)
 padB.penup()
 padB.goto(450,0) 

 #ball
 ball = turtle.Turtle()
 ball.speed(0)
 ball.shape("square")
 ball.color(col2)
 ball.penup()
 ball.goto(0,0)
 ball.dx = 0.4
 ball.dy = 0.4

 #pen
 pen = turtle.Turtle()
 pen.speed(0)
 pen.penup()
 pen.ht()
 pen.goto(0,20)
 pen.color("red")
 pen.write("WELCOME TO PONG",align="center", font=("Terminal",30,"normal"))
 pen.goto(0,-20)
 pen.write("- Control the paddles using W,D and Up,Down", align= "center", font = ("Terminal",12, "normal"))
 pen.goto(0,-60)
 pen.write("- The player who scores 3 points first wins", align= "center", font = ("Terminal", 12, "normal"))
 time.sleep(3)
 pen.clear()

 ben = turtle.Turtle()
 ben.speed(0)
 ben.color(col2)
 ben.penup()
 ben.goto(0,0)
 ben.ht()

 pen.color(col2)
 pen.goto(0,260)
 pen.write("Player A: 0                              Player B: 0", align="center", font=("Arial",24,"normal"))

 #MOVEMENT 
 #Up

 def padA_up():
    y = padA.ycor()
    y+= 20
    if y<=240:
       padA.sety(y)

 def padA_down():
    y = padA.ycor()
    y-=20
    if y>=-240:
       padA.sety(y)

 def padB_up():
    y = padB.ycor()
    y+= 20
    if y<=240:
       padB.sety(y)

 def padB_down():
    y = padB.ycor()
    y-=20
    if y>=-240:
       padB.sety(y)

 def Continue():
     pen.clear()
     Pong()

 def Exit():
     wn.bye()

 wn.listen()
 wn.onkeypress(padA_up,"w")
 wn.onkeypress(padA_down,"s")
 wn.onkeypress(padB_up,"Up")
 wn.onkeypress(padB_down,"Down")

 #game loop
 while True:
    wn.update()
    #ben.write("ycor:{}".format(padA.ycor()), align="center", font=("Arial",24,"normal"))
    #ben.clear()

    #move the ball
    ball.setx((ball.xcor()) + (ball.dx))
    ball.sety((ball.ycor()) + (ball.dy))

    #border
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -285:
        ball.sety(-285)
        ball.dy *= -1

    if ball.xcor() > 485:
        ball.goto(0,0)
        ball.dx*=-1
        
        scoreA +=1
        pen.clear()
        pen.write("Player A: {}                              Player B: {}".format(scoreA, scoreB), align="center", font=("Arial",24,"normal"))

        if scoreA == 3:
            w = "Player A"
            l = "Player B"
            break

    if ball.xcor() < -490:
        ball.goto(0,0)
        ball.dx*=-1
        
        scoreB +=1
        pen.clear()
        pen.write("Player A: {}                              Player B: {}".format(scoreA, scoreB), align="center", font=("Arial",24,"normal"))

        if scoreB == 3:
            w = "Player B"
            l = "Player A"
            break

    if (ball.xcor() > 440) and (ball.xcor() < 450) and (ball.ycor() < (padB.ycor() + 60)) and (ball.ycor() > (padB.ycor() - 60)):
        ball.dx*=-1
        ball.setx(440)

    if (ball.xcor() < -440) and (ball.xcor() > -450) and (ball.ycor() < (padA.ycor() + 60)) and (ball.ycor() > (padA.ycor() - 60)):
        ball.dx*=-1
        ball.setx(-440)

 padA.ht()
 padB.ht()
 ball.ht()
 pen.clear()
 wn.update()

 pen.color("red")
 pen.goto(0,50)
 pen.write("GAME OVER!",align="center", font=("Terminal",30,"normal"))
 pen.goto(0,0)
 pen.write("Congratulations {}, better luck next time {}.".format(w,l),align="center", font=("Terminal",20,"normal"))
 pen.goto(0,-250)
 pen.write("Press Enter to continue or Esc to exit",align= "center", font = ("Terminal", 18, "normal"))
 wn.listen()
 wn.onkeypress(Exit,"Escape")
 wn.onkeypress(Continue,"Return")
 
Pong()
