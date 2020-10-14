#HANGMAN code

num=0
import turtle
import random
import time
face=turtle.Turtle()
s=face.getscreen()
s.screensize(1000,600)
s.bgcolor('black')
s.tracer(0)
s.delay(0.5)
face.hideturtle()
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
choice=random.randint(0,9)
string=''
clues=[clue1[choice],clue2[choice],clue3[choice],'ALL CLUES REVEALED']
s.tracer(True)
def draw(i):
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
            i.reset()
        time.sleep(1)
        ender.write('GAME OVER!!! YOU LOST!!!',align='center',font=('Arial',32,'bold'))
        time.sleep(3)
        s.bye()
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
            i.reset()
        ender.write('CONGRATULATIONS!!!YOU WON!!!',align='center',font=('Arial',32,'bold'))
        time.sleep(3)
        s.bye()
        
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
