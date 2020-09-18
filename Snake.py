import turtle
import time
import random

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
wall.goto(-498, 298)
wall.goto(490, 298)
wall.goto(490, -290)
wall.goto(-498, -290)

#food
food = turtle.Turtle()
food.speed(0)
food.color("red")
food.shape("circle")
food.penup()
food.goto(0, 100)

segments = []

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,200)
pen.write("Score: 0  High Score: 0", align = "center", font = ("Terminal", 18, "normal"))

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

#keyboard bindings
wn.listen()
wn.onkeypress(go_up, 'w')
wn.onkeypress(go_down, 's')
wn.onkeypress(go_right, 'd')
wn.onkeypress(go_left, 'a')


while True:
    wn.update()

    #collision check
    if head.xcor()>475 or head.ycor()<-272 or head.xcor()<-478 or head.ycor()>280:

        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        for segment in segments:
            segment.goto(10000,10000)

        segments.clear()
        score = 0
        delay = 0.03

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, h_score), align = "center", font = ("Terminal", 18, "normal"))


    #snake eats food
    if head.distance(food) < 20:
        x = random.randint(-470, 470)
        y = random.randint(-260, 270)
        
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
        pen.write("Score: {}  High Score: {}".format(score, h_score), align = "center", font = ("Terminal", 18, "normal"))

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

            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, h_score), align = "center", font = ("Terminal", 18, "normal"))


    time.sleep(delay)


