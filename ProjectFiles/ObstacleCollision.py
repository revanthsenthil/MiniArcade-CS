#OBSTACLE COLLISION code
import turtle
import random
import time
t=turtle.Turtle()
t.hideturtle()
t.pencolor("blue")
t.pu()
t.setpos(-500,0)
t.showturtle()
s=t.getscreen()
s.screensize(1000,600)
s.bgcolor('black')
s.tracer(0)
block1=turtle.Turtle()
block1.pu()
block1.shape("square")
block2=turtle.Turtle()
block2.pu()
block2.shape("square")
block3=turtle.Turtle()
block3.pu()
block3.shape("square")
block4=turtle.Turtle()
block4.pu()
block4.shape("square")
block5=turtle.Turtle()
block5.pu()
block5.shape("square")
block6=turtle.Turtle()
block6.pu()
block6.shape("square")
block7=turtle.Turtle()
block7.pu()
block7.shape("square")
block8=turtle.Turtle()
block8.pu()
block8.shape("square")
block9=turtle.Turtle()
block9.pu()
block9.shape("square")
block1.setpos(-400,-120)
block2.setpos(-300,50)
block3.setpos(-200,-200)
block4.setpos(-100,50)
block5.setpos(100,150)
block6.setpos(200,260)
block7.setpos(300,-50)
block8.setpos(400,-250)
block9.setpos(0,10)
border=turtle.Turtle()
border.pu()
border.goto(-500,300)
border.pd()
border.pencolor('white')
border.setpos(500,300)
border.setpos(500,-300)
border.setpos(-500,-300)
border.setpos(-500,300)
border.hideturtle()
ender=turtle.Turtle()
ender.hideturtle()
for i in s.turtles()[1::]:
    i.pencolor('red')    
s.update()
s.tracer(True)
s.delay(0.5)
def up():
    if t.heading()!=270:
        t.setheading(90)
def down():
    if t.heading()!=90:
        t.setheading(270)
 
def right():
    if t.heading()!=180:
        t.setheading(0)
 
def left():
    if t.heading()!=0:
        t.setheading(180)
def overlap():
     for i in s.turtles()[1:10]:
         if t.distance(i)<=15:
             s.tracer(0)
             for i in s.turtles():
                i.hideturtle()
L=[]
for i in range(-300,-279):
    L.append(i)
for i in range(280,301):
    L.append(i)
l=[]
for i in range(9):
    a=random.randint(1,2)
    if a==1:
        l.append(90)
    else:
        l.append(270)
for i in range(9):
    s.turtles()[i+1].setheading(l[i])
def fun():
    overlap()
    if t.xcor()>=-500:
        s.onkeypress(up,'Up')
        s.onkeypress(down,'Down')
        s.onkeypress(left,'Left')
        s.onkeypress(right,'Right')
        s.listen()
    if s.tracer()==0:
        ender.pu()
        ender.write("GAME OVER!! YOU LOST!!",align="center",font=("Arial",32,"bold"))
        s.update()
    elif t.ycor()>=300 or t.xcor()<=-500 or t.ycor()<=-300:
        s.tracer(0)
        for i in s.turtles():
            i.hideturtle()
        ender.pu()
        ender.write("OUT OF BOUNDS!! YOU LOSE!!",align="center",font=("Arial",32,"bold"))
        s.update()
    elif t.xcor()>=500:
        s.tracer(0)
        for i in s.turtles():
            i.hideturtle()
        ender.pu()
        ender.write("CONGRATULATIONS!! YOU WON!!",align="center",font=("Arial",32,"bold"))
        s.update()
    else:
        pass
time.sleep(1)
while s.tracer()!=0:
    for i in s.turtles()[1:10]:
        if i.ycor() in L:
            i.right(180)
            i.fd(2)
        else:
            i.fd(2)
    t.fd(0.8)
    fun()
time.sleep(3)
s.bye()
