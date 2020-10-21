import turtle
from random import randint,randrange,random
import time

def Target_Practice():
 global Coords,score,k          

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
         Main_Menu()

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
 pen.write("GAME OVER!", align='center', font = ("Terminal", 30, "normal"))
 pen.goto(0,0)
 pen.write("Your score: {}".format(score), align='center', font = ("Terminal", 25, "normal"))
 joe.goto(0,-250)
 joe.write("Press Enter to play again or Esc to go to menu",align= "center", font = ("Terminal", 18, "normal"))
 window.listen()
 window.onkeypress(Exit,"Escape")
 window.onkeypress(Continue,"Return")


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
 ball.dx = 1
 ball.dy = 1

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
     pen.clear()
     Main_Menu()

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
 pen.write("Press Enter to play again or Esc to go to menu",align= "center", font = ("Terminal", 18, "normal"))
 wn.listen()
 wn.onkeypress(Exit,"Escape")
 wn.onkeypress(Continue,"Return")

def Snake():
 delay = 0.03
 score = 0
 h_score = 0

 wn = turtle.Screen()
 wn.title("SNAKE")
 wn.bgcolor("black")
 wn.setup(width = 1000, height = 600) #diff
 wn.tracer(0) #turns off screen updates

 #head
 head = turtle.Turtle()
 head.speed(0)
 head.color("green")
 head.shape("square")
 head.penup()
 head.goto(0, 0)
 head.direction = "stop"

 #wall
 wall = turtle.Turtle()
 wall.speed(1000)
 wall.color("blue")
 wall.hideturtle()
 wall.width(10)
 wall.penup()
 wall.goto(-498, -290)
 wall.pendown()
 wall.goto(-498, 250)
 wall.goto(490, 250)
 wall.goto(490, -290)
 wall.goto(-498, -290)

 #food
 food = turtle.Turtle()
 food.speed(0)
 food.color("yellow")
 food.shape("circle")
 food.penup()
 food.goto(0, 100)

 segments = []

 #pen
 pen = turtle.Turtle()
 pen.speed(0)
 pen.shape("square")
 pen.color("red")
 pen.penup()
 pen.hideturtle()
 pen.write("WELCOME TO SNAKE", align= "center", font = ("Terminal", 30, "normal"))
 pen.goto(0,-40)
 pen.write("- On consuming food, the length of the snake increases", align= "center", font = ("Terminal",12, "normal"))
 pen.goto(0,-80)
 pen.write("- Ensure that the snake doesn't collide with the walls nor with its own body", align= "center", font = ("Terminal", 12, "normal"))
 time.sleep(3)
 pen.clear()
 pen.goto(0,262)
 pen.write("Score: 0                    High Score: 0", align = "center", font = ("Terminal", 18, "normal"))


 def go_up():
    if head.direction != "down":
        head.direction = "up"

 def go_down():
    if head.direction != "up":
        head.direction = "down"

 def go_right():
    if head.direction != "left":
        head.direction = "right"

 def go_left():
    if head.direction != "right":
        head.direction = "left"


 #move function
 def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 7)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 7)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 7)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 7)

 def Continue():
     pen.clear()
     Snake()

 def Exit():
     pen.clear()
     Main_Menu()

 #keyboard bindings
 wn.listen()
 wn.onkeypress(go_up, 'w')
 wn.onkeypress(go_down, 's')
 wn.onkeypress(go_right, 'd')
 wn.onkeypress(go_left, 'a') 

 c=0
 while True:
    wn.update()
    #collision check
    if head.xcor()>475 or head.ycor()<-273 or head.xcor()<-478 or head.ycor()>231:

        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
        c+=1
        
        for segment in segments:
            segment.goto(10000,10000)

        segments.clear()
        score = 0
        delay = 0.03
        if c>5:
            break
        else:
           pen.clear()
           pen.write("Score: {}                    High Score: {}".format(score, h_score), align = "center", font = ("Terminal", 18, "normal"))


    #snake eats food
    if head.distance(food) < 20:
        x = randint(-470, 470)
        y = randint(-260, 225)
        
        food.goto(x, y)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("light green")
        new_segment.penup()
        segments.append(new_segment)
        delay -= 0.0005

        #increase score
        score = score + 10

        if score > h_score:
            h_score = score

        pen.clear()
        pen.write("Score: {}                    High Score: {}".format(score, h_score), align = "center", font = ("Terminal", 18, "normal"))

    # move segments
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    #move segment to where head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    #collision with body
    for segment in segments:
        if segment.distance(head) < 7:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            for segment in segments:
                segment.goto(2000, 20000)

            segments.clear()
            score = 0
            delay = 0.03
            c+=1
            if c > 5:
                break
            else:
                pen.clear()
                pen.write("Score: {}          High Score: {}".format(score, h_score), align = "center", font = ("Terminal", 18, "normal"))

    time.sleep(delay)
 head.clear()
 food.clear()
 wall.clear()
 head.ht()
 food.ht()
 pen.clear()
 pen.goto(0,50)
 wn.update()
 pen.write("GAME OVER!",align="center", font=("Terminal",30,"normal"))
 pen.goto(0,0)
 pen.write("Your High Score : {}".format(h_score),align="center", font=("Terminal",20,"normal"))
 pen.goto(0,-250)
 pen.write("Press Enter to play again or Esc to go to menu",align= "center", font = ("Terminal", 18, "normal"))
 wn.listen()
 wn.onkeypress(Exit,"Escape")
 wn.onkeypress(Continue,"Return")

def Hangman():
 global string,let_used,num,clues
 num=0
 s=turtle.Screen()
 s.setup(width=1000, height=600) 
 s.bgcolor('black')
 s.tracer(0)
 s.delay(0.5)
 pen = turtle.Turtle()
 pen.speed(0)
 pen.penup()
 pen.ht()
 pen.goto(0,20)
 pen.color("red")
 pen.write("WELCOME TO HANGMAN",align="center", font=("Terminal",30,"normal"))
 pen.goto(0,-20)
 pen.write("- You have 3 clues for guessing the word or phrase or name", align= "center", font = ("Terminal",12, "normal"))
 pen.goto(0,-60)
 #pen.write("- You can commit a maximum of nine mistakes", align= "center", font = ("Terminal", 12, "normal"))
 time.sleep(3)
 pen.clear()
 face=turtle.Turtle()
 face.hideturtle()
 face.pu()
 face.goto(-50,0)
 torso=turtle.Turtle()
 torso.hideturtle()
 torso.pu()
 leg1=turtle.Turtle()
 leg1.hideturtle()
 leg1.pu()
 vstand=turtle.Turtle()
 vstand.hideturtle()
 vstand.pu()
 extra=turtle.Turtle()
 extra.hideturtle()
 extra.pu()
 extra.goto(-50,50)
 extra.setheading(180)
 torso.goto(-50,-57.284)
 torso.setheading(270)
 leg1.goto(-50,-157.284)
 leg2=turtle.Turtle()
 leg2.hideturtle()
 leg2.pu()
 leg2.goto(-50,-157.284)
 leg1.right(60)
 leg2.right(120)
 hand1=turtle.Turtle()
 hand1.hideturtle()
 hand1.pu()
 hand1.right(60)
 hand2=turtle.Turtle()
 hand2.hideturtle()
 hand2.pu()
 hand2.right(120)
 hand1.goto(-50,-77.284)
 hand2.goto(-50,-77.284)
 vstand.goto(100,-250)
 vstand.setheading(90)
 letter=turtle.Turtle()
 letter.hideturtle()
 letter.pu()
 letter.goto(0,150)
 used=turtle.Turtle()
 used.ht()
 used.pu()
 used.goto(0,-290)
 let_used='LETTERS USED: '
 used.hideturtle()
 used.pencolor('white')
 used.write(let_used,align='center',font=('Arial','16','bold'))
 writeclue=turtle.Turtle()
 writeclue.hideturtle()
 writeclue.pu()
 writeclue.goto(300,-50)
 writeclue.pencolor('red')
 writeclue.write('CLUES (Press space)',align='center',font=('Arial','14','bold'))
 for i in s.turtles():
    i.pd()
    i.pensize(3)
    i.pencolor('white')
 def head():
    s.tracer(2)
    for i in range(600):
        face.fd(0.3)
        face.right(0.6)
    face.ht()
 def line(a,x):
    s.tracer(2)
    for i in range(x):
        a.fd(1)

 word=['PEWDIEPIE','KOBE BRYANT','RICKY PONTING','MR BEAST','ELON MUSK','MARK ZUCKERBERG','STEVE JOBS','DON BRADMAN','ROWAN ATKINSON','KEANU REEVES']
 clue1=['The king of YouTube','Late basketball player','Retired Cricketer','Performs expensive stunts and philanthropy','Real-life Tony Stark.','He is color blind','A pioneer of the personal computer revolution of 1970-1980s','The greatest batsman of all time','An English actor, comedian and writer','Canadian Actor']
 clue2=['Leader of the Floor Gang','Got an award named after him in 2020','Played in the Ashes','Took an initiative to plant 20 million trees','The coolest billionaire','Internet entrepreneur, and philanthropist','American business magnate, investor','Was an Australian International cricketer','Suffered from a speech impediment as a child ','Down-to-earth and charismatic']
 clue3=['Has over a 100 million subscribers on YouTube','Played for the Los Angeles Lakers',"Was the Australian cricket team's captain",'Real name is Jimmy Donaldson','CEO of Tesla,Inc and SpaceX','Co-founder and CEO of Facebook','Co-founder and late CEO of Apple','His Test batting average is 99.94','Mr.Bean','John Wick']
 category=['YouTuber','Sports','Sports','YouTuber','Personality','Personality','Personality','Sports','Celebrity','Celebrity']
 tc=turtle.Turtle()
 tc.hideturtle()
 tc.pu()
 tc.goto(-400,-200)
 tc.pencolor('blue')
 tc.write('CATEGORY',align='center',font=('Arial','20','bold'))
 tc.goto(-400,-250)
 ender=turtle.Turtle()
 ender.hideturtle()
 ender.pencolor('red')
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
 s.update()
 choice=randint(0,9)
 string=''
 clues=[clue1[choice],clue2[choice],clue3[choice],'ALL CLUES REVEALED']
 s.tracer(True)

 def Continue():
     ender.clear()
     s.turtles().clear()
     Hangman()

 def Exit():
     ender.clear()
     s.turtles().clear()
     Main_Menu()

 def draw(i):
    global pen
    if i==0:
        head()
    elif i==1:
        line(torso,100)
    elif i==2:
        line(hand1,50)
    elif i==3:
        line(hand2,50)
    elif i==4:
        line(leg1,50)
    elif i==5:
        line(leg2,50)
    elif i==6:
        line(vstand,300)
    elif i==7:
        vstand.left(90)
        line(vstand,150)
        line(extra,20)
    elif i==8:
        vstand.left(90)
        line(vstand,50)
        for i in s.turtles()[0:-2]:
            i.clear()
            i.reset()
            i.hideturtle()
        ender.hideturtle()
        time.sleep(0.5)
        ender.pu()
        ender.goto(0,50)
        ender.write("GAME OVER!!! YOU LOST!!!",align="center", font=("Terminal",30,"normal"))
        ender.goto(0,-250)
        ender.write("Press Enter to play again or Esc to go to menu",align= "center", font = ("Terminal", 18, "normal"))
        s.listen()
        s.onkeypress(Exit,"Escape")
        s.onkeypress(Continue,"Return")

 def reset(x):
    s.tracer(0)
    global string
    global let_used
    global num
    no_gap=[]
    for i in range(1,len(string)-1,3):
        no_gap.append(string[i])
    for i in range(len(word[choice])):
        if word[choice][i]==x:
            no_gap[i]=x
    string=''
    check=''
    for i in no_gap:
        string+=' '+i+' '
        check+=i
    letter.clear()
    letter.write(string,align='center',font=('Arial',32,'bold'))
    s.update()
    s.tracer(True)
    if x not in word[choice] and x not in let_used[12::]:
        draw(num)
        num+=1
    if x  not in let_used[12::]:
        let_used+=x+' '
        used.clear()
        used.write(let_used,align='center',font=('Arial','16','bold'))
    if check==word[choice]:
        for i in s.turtles()[0:-2]:
            i.clear()
            i.reset()
            i.hideturtle()
        ender.hideturtle()
        ender.pu()
        ender.goto(0,50)
        ender.write("CONGRATULATIONS!!! YOU WON!!!",align="center", font=("Terminal",30,"normal"))
        ender.goto(0,-250)
        ender.write("Press Enter to play again or Esc to go to menu",align= "center", font = ("Terminal", 18, "normal"))
        s.listen()
        s.onkeypress(Exit,"Escape")
        s.onkeypress(Continue,"Return")
        #ender.write('CONGRATULATIONS!!!YOU WON!!!',align='center',font=('Arial',32,'bold'))
        #time.sleep(3)
        #s.bye()
                
 def reseta():
    reset('A')
 def resetb():
    reset("B")
 def resetc():
    reset('C')
 def resetd():
    reset('D')
 def resete():
    reset('E')
 def resetf():
    reset('F')
 def resetg():
    reset('G')
 def reseth():
    reset('H')
 def reseti():
    reset('I')
 def resetj():
    reset('J')
 def resetk():
    reset('K')
 def resetl():
    reset('L')
 def resetm():
    reset('M')
 def resetn():
    reset('N')
 def reseto():
    reset('O')
 def resetp():
    reset('P')
 def resetq():
    reset('Q')
 def resetr():
    reset('R')
 def resets():
    reset('S')
 def resett():
    reset('T')
 def resetu():
    reset('U')
 def resetv():
    reset('V')
 def resetw():
    reset('W')
 def resetx():
    reset('X')
 def resety():
    reset('Y')
 def resetz():
    reset('Z')
 def initiate(x):
    global string
    under=' _ '
    space='   '
    for i in word[choice]:
        if i.isspace():
            string+=space
        else:
            string+=under
    tc.write(category[x].upper(),align='center',font=('Arial','12','bold'))
    letter.write(string,align='center',font=('Arial','32','bold'))
 def clue():
    global clues
    if len(clues)!=0:
        writeclue.pu()
        writeclue.goto(300,writeclue.ycor()-50)
        writeclue.write(clues[0],align='center',font=('Arial',10,'bold'))
        clues=clues[1::]

 initiate(choice)
 s.onkeypress(reseta,'a')
 s.onkeypress(resetb,'b')
 s.onkeypress(resetc,'c')
 s.onkeypress(resetd,'d')
 s.onkeypress(resete,'e')
 s.onkeypress(resetf,'f')
 s.onkeypress(resetg,'g')
 s.onkeypress(reseth,'h')
 s.onkeypress(reseti,'i')
 s.onkeypress(resetj,'j')
 s.onkeypress(resetk,'k')
 s.onkeypress(resetl,'l')
 s.onkeypress(resetm,'m')
 s.onkeypress(resetn,'n')
 s.onkeypress(reseto,'o')
 s.onkeypress(resetp,'p')
 s.onkeypress(resetq,'q')
 s.onkeypress(resetr,'r')
 s.onkeypress(resets,'s')
 s.onkeypress(resett,'t')
 s.onkeypress(resetu,'u')
 s.onkeypress(resetv,'v')
 s.onkeypress(resetw,'w')
 s.onkeypress(resetx,'x')
 s.onkeypress(resety,'y')
 s.onkeypress(resetz,'z')
 s.onkeypress(clue,'space')
 s.listen()
 s.mainloop()

def Obstacle_Course():
 win=turtle.Screen()
 win.setup(width=1000, height=600)
 win.bgcolor('black')
 win.tracer(0)
 Block_color=['red','cyan','blue','purple']
 t_color=['cyan','orange','yellow','lightgreen']
 col=randint(0,3)
 t=turtle.Turtle()
 t.hideturtle()
 t.color(t_color[col])
 t.pu()
 t.setpos(-500,0)
 t.showturtle()
 block_color=Block_color[col]
 block1=turtle.Turtle()
 block1.pu()
 block1.color(block_color)
 block1.shape("square")
 block2=turtle.Turtle()
 block2.pu()
 block2.color(block_color)
 block2.shape("square")
 block3=turtle.Turtle()
 block3.pu()
 block3.color(block_color)
 block3.shape("square")
 block4=turtle.Turtle()
 block4.pu()
 block4.color(block_color)
 block4.shape("square")
 block5=turtle.Turtle()
 block5.pu()
 block5.color(block_color)
 block5.shape("square")
 block6=turtle.Turtle()
 block6.pu()
 block6.color(block_color)
 block6.shape("square")
 block7=turtle.Turtle()
 block7.pu()
 block7.color(block_color)
 block7.shape("square")
 block8=turtle.Turtle()
 block8.pu()
 block8.color(block_color)
 block8.shape("square")
 block9=turtle.Turtle()
 block9.pu()
 block9.color(block_color)
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
 ender = turtle.Turtle()
 ender.penup()
 ender.ht()
 ender.goto(0,20)
 ender.color("red")
 ender.write("WELCOME TO OBSTACLE COURSE",align="center", font=("Terminal",30,"normal"))
 ender.goto(0,-20)
 ender.write("- Reach the end by avoiding the obstaclea", align= "center", font = ("Terminal",12, "normal"))
 ender.goto(0,-60)
 ender.write("- Make sure you don't go out of the screen", align= "center", font = ("Terminal", 12, "normal"))
 time.sleep(3)
 ender.clear()
 ender.goto(0,20)
 ender.pd()
 #for i in s.turtles()[1::]:
   # i.pencolor('yellow')    
 win.update()
 win.tracer(1)
 win.delay(0.5)
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
     for i in win.turtles()[1:10]:
         if t.distance(i)<=15:
             win.tracer(0)
             for i in win.turtles():
                i.hideturtle()
 L=[]
 for i in range(-300,-279):
    L.append(i)
 for i in range(280,301):
    L.append(i)
 l=[]
 for i in range(9):
    a=randint(1,2)
    if a==1:
        l.append(90)
    else:
        l.append(270)
 for i in range(9):
    win.turtles()[i+1].setheading(l[i])
 def fun():
    overlap()
    if t.xcor()>=-500:
        win.onkeypress(up,'Up')
        win.onkeypress(down,'Down')
        win.onkeypress(left,'Left')
        win.onkeypress(right,'Right')
        win.listen()
    if win.tracer()==0:
        ender.pu()
        ender.write("GAME OVER!! YOU LOST!!",align="center",font=("Terminal",30,"normal"))
        win.update()
    elif t.ycor()>=300 or t.xcor()<=-500 or t.ycor()<=-300:
        win.tracer(0)
        for i in win.turtles():
            i.hideturtle()
        ender.pu()
        ender.write("OUT OF BOUNDS!! YOU LOSE!!",align="center",font=("Terminal",30,"normal"))
        win.update()
    elif t.xcor()>=500:
        win.tracer(0)
        for i in win.turtles():
            i.hideturtle()
        ender.pu()
        ender.write("CONGRATULATIONS!! YOU WON!!",align="center",font=("Terminal",30,"normal"))
        win.update()
    else:
        pass

 def Continue():
     ender.clear()
     win.turtles().clear()
     Obstacle_Course()

 def Exit():
     ender.clear()
     win.turtles().clear()
     Main_Menu()

 while win.tracer()!=0:
    for i in win.turtles()[1:10]:
        if i.ycor() in L:
            i.right(180)
            i.fd(2)
        else:
            i.fd(2)
    t.fd(0.8)
    fun()

 ender.goto(0,-250)
 ender.write("Press Enter to play again or Esc to go to menu",align= "center", font = ("Terminal", 18, "normal"))
 win.listen()
 win.onkeypress(Exit,"Escape")
 win.onkeypress(Continue,"Return")
 
def Main_Menu():
        win=turtle.Screen()
        win.title("Mini ARCADE")
        win.setup(width=1000, height=600)
        win.tracer(0)
        win.bgcolor("black")
        dub=turtle.Turtle()
        dub.color("yellow")
        dub.width(5)
        dub.ht()
        dub.pu()
        dub.goto(489,296)
        dub.pd()
        dub.goto(-496,296)
        dub.goto(-496,-288)
        dub.goto(489,-288)
        dub.goto(489,296)
        pen = turtle.Turtle()
        pen.speed(0)
        pen.color("red")
        pen.pu()
        pen.ht()
        pen.goto(0,200)
        pen.write("Mini ARCADE", align= "center", font = ("Terminal", 30, "normal"))
        pen.goto(0,120)
        pen.write("Click on any game that you wish to play.", align= "center", font = ("Terminal", 20, "normal"))
        box=turtle.Turtle()
        box.color("blue")
        box.ht()
        box.width(5)
        box.pu()
        box.goto(170,50)
        box.pd()
        box.goto(420,50)
        box.goto(420,-50)
        box.goto(170,-50)
        box.goto(170,50)
        box.pu()
        box.goto(-170,50)
        box.pd()
        box.goto(-420,50)
        box.goto(-420,-50)
        box.goto(-170,-50)
        box.goto(-170,50)
        box.pu()
        box.goto(-170,-100)
        box.pd()
        box.goto(-420,-100)
        box.goto(-420,-200)
        box.goto(-170,-200)
        box.goto(-170,-100)
        box.pu()
        box.goto(170,-100)
        box.pd()
        box.goto(420,-100)
        box.goto(420,-200)
        box.goto(170,-200)
        box.goto(170,-100)
        box.pu()
        box.goto(120,0)
        box.pd()
        box.goto(-120,0)
        box.goto(-120,-100)
        box.goto(120,-100)
        box.goto(120,0)
        box.pu()
        pen.goto(300,5)
        pen.color("red")
        pen.write("Target", align= "center", font = ("Terminal", 22, "normal"))
        pen.goto(300,-25)
        pen.write("PRACTICE", align= "center", font = ("Terminal", 22, "normal"))
        pen.goto(-295,5)
        pen.write("Obstacle", align= "center", font = ("Terminal", 22, "normal"))
        pen.goto(-295,-25)
        pen.write("COURSE", align= "center", font = ("Terminal", 22, "normal"))
        pen.goto(300,-168)
        pen.write("HANGMAN", align= "center", font = ("Terminal", 23, "normal"))
        pen.goto(-295,-168)
        pen.write("SNAKE", align= "center", font = ("Terminal", 23, "normal"))
        pen.goto(0,-70)
        pen.write("PONG", align= "center", font = ("Terminal", 23, "normal"))
        def game(x,y):
                if 170<x<420 and -50<y<50 :
                        pen.clear()
                        box.clear()
                        dub.clear()
                        Target_Practice()
                elif -420<x<-170 and -50<y<50 :
                        pen.clear()
                        box.clear()
                        dub.clear()
                        win.turtles().clear()
                        Obstacle_Course()
                elif -420<x<-170 and -200<y<-100 :
                        pen.clear()
                        box.clear()
                        dub.clear()
                        Snake()
                elif 170<x<420 and -200<y<-100:
                        pen.clear()
                        box.clear()
                        dub.clear()
                        Hangman()
                elif -120<x<120 and -100<y<0:
                        pen.clear()
                        box.clear()
                        dub.clear()
                        Pong()
                      
        while True:
                win.update()
                win.listen()
                win.onclick(game)
                
Main_Menu()
