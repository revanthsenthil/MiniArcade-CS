import turtle
from random import randint,randrange,random
import time
 
def Target_Practice():
 global Coords,score,k          # Very very very important statement in the whole program.
 
 #Window and Pens
 window = turtle.Screen()
 window.title("Target Practice")
 window.setup(width=1000, height=600)
 window.tracer(0)
 window.bgcolor("black")
 
 pen = turtle.Turtle()
 pen.speed(0)
 pen.shape("square")
 pen.color("red")
 pen.pu()
 pen.ht()
 pen.goto(0,0)
 #pen.write("X: {}  Y: {}".format(pac1.xcor(), pac1.ycor()), align = "center", font = ("Terminal", 18, "normal"))
 pen.write("WELCOME TO TARGET PRACTICE", align= "center", font = ("Terminal", 30, "normal"))
 pen.goto(0,-40)
 pen.write("- Click as many targets as possible before the time runs out", align= "center", font = ("Terminal",12, "normal"))
 pen.goto(0,-80)
 pen.write("- Click the bullseye for maximum points", align= "center", font = ("Terminal", 12, "normal"))
 time.sleep(3)
 pen.clear()
 pen.goto(-400,250)
 
 joe = turtle.Turtle()
 joe.speed(0)
 joe.shape("square")
 joe.color("red")
 joe.pu()
 joe.ht()
 joe.goto(350,250)
 
 #Targets
 bing=turtle.Turtle()
 bing.color('white')
 bing.width(35)
 bing.ht()
 
 bing1=turtle.Turtle()
 bing1.color("red")
 bing1.width(25)
 bing1.ht()
 
 bing2=turtle.Turtle()
 bing2.color("white")
 bing2.width(15)
 bing2.ht()
 
 bing3=turtle.Turtle()
 bing3.color("red")
 bing3.width(5)
 bing3.ht()
 
 mask=turtle.Turtle()
 mask.color('black')
 mask.width(35)
 mask.ht()
 mask.pu()
 
 Coords=[]
 score=0
 k=30
 
 #Funtions
 def click(X,Y):
        global score
        global Coords
        for i in Coords:
                Xcor=i[0]
                Ycor=i[1]
                if Xcor-4 <= X <= Xcor+4 and Ycor-4 <= Y <= Ycor+4:
                        mask.goto(Xcor,Ycor)
                        mask.pd()
                        mask.dot()
                        mask.pu()
                        Coords.remove(i)
                        score+=10
                        break                
                if Xcor-15 <= X <= Xcor+15 and Ycor-15 <= Y <= Ycor+15:
                        mask.goto(Xcor,Ycor)
                        mask.pd()
                        mask.dot()
                        mask.pu()
                        Coords.remove(i)
                        score+=5
                        break
                if Xcor-25 <= X <= Xcor+25 and Ycor-25 <= Y <= Ycor+25:
                        mask.goto(Xcor,Ycor)
                        mask.pd()
                        mask.dot()
                        mask.pu()
                        Coords.remove(i)
                        score+=2
                        break
                if Xcor-35 <= X <= Xcor+35 and Ycor-35 <= Y <= Ycor+35:
                        mask.goto(Xcor,Ycor)
                        mask.pd()
                        mask.dot()
                        mask.pu()
                        Coords.remove(i)
                        score+=1
                        break
                
 def target():
        global Coords
        x=randint(-450,450)
        y=randint(-250,200)
        bing.pu()
        bing1.pu()
        bing2.pu()
        bing3.pu()
        if len(Coords) == 0:
                Coords.append((x,y))
                bing.goto(x,y)
                bing1.goto(x,y)
                bing2.goto(x,y)
                bing3.goto(x,y)
                bing.pd()
                bing.dot()
                bing1.pd()
                bing1.dot()
                bing2.pd()
                bing2.dot()
                bing3.pd()
                bing3.dot()
                
        else:
                for i in Coords:
                     Xcor=i[0]
                     Ycor=i[1]
                     if  Xcor-70 <= x <= Xcor+70 and Ycor-70 <= y <= Ycor+70 :
                         break
                else:
                        bing.goto(x,y)
                        bing.pd()
                        bing.dot()
                        bing1.goto(x,y)
                        bing1.pd()
                        bing1.dot()
                        bing2.goto(x,y)
                        bing2.pd()
                        bing2.dot()
                        bing3.goto(x,y)
                        bing3.pd()
                        bing3.dot() 
                        Coords.append((x,y))
 
 def Exit():
         window.clear()
         window.bye()
 def Continue():
         window.clear()
         Target_Practice()
 
 #Main Loop
 while True:
 
        target()
        window.listen()
        time.sleep(0.5)
        pen.clear()
        joe.clear()
        pen.write("Score : {}".format(score), align= "center", font = ("Terminal", 18, "normal"))
        joe.write("Time left: {}".format(k),align= "center", font = ("Terminal", 18, "normal"))
        k-=1
        window.onclick(click)
        window.update()
        window.listen()
 
        if k == -2:
                break
              
 pen.clear()
 joe.clear()
 bing.clear()
 bing1.clear()
 bing2.clear()
 bing3.clear()
 mask.clear()
 pen.goto(0,50)
 pen.write("GAME OVER", align='center', font = ("Terminal", 30, "normal"))
 pen.goto(0,0)
 pen.write("Your score: {}".format(score), align='center', font = ("Terminal", 25, "normal"))
 joe.goto(0,-250)
 joe.write("Press Enter to continue or Esc to exit",align= "center", font = ("Terminal", 18, "normal"))
 window.listen()
 window.onkeypress(Exit,"Escape")
 window.onkeypress(Continue,"Return")
 
Target_Practice()
