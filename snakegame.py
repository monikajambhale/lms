import time
import turtle
import random
delay=0.1

score=0
highscore=0

wn=turtle.Screen()
wn.title("Snake game")
wn.bgcolor('yellow')
wn.setup(width=600,height=600)
wn.tracer(0)

head=turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction="stop"

food=turtle.Turtle()
food.speed(0)
food.shape("square")
food.color('red')
food.penup()
food.goto(0,100)

segments=[]

sc=turtle.Turtle()
sc.speed(0)
sc.shape("square")
sc.color('black')
sc.penup()
sc.hideturtle()
sc.goto(0,260)
sc.write("Score: 0 High score: 0",align="center")

def go_up():
    if head.direction!="down":
        head.direction="up"
def go_down():
    if head.direction!="up":
        head.direction="down"
def go_left():
    if head.direction!="right":
        head.direction="left"
def go_right():
    if head.direction!="left":
        head.direction="right"
def move():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y+20)
    if head.direction=="down":
        y=head.ycor()
        head.sety(y-20)
    if head.direction=="left":
        x=head.xcor()
        head.setx(x-20)
    if head.direction=="right":
        x=head.xcor()
        head.setx(x+20)

wn.listen()
wn.onkeypress(go_up,"w")
wn.onkeypress(go_down,"s")
wn.onkeypress(go_left,"a")
wn.onkeypress(go_right,"d")

while True:
    wn.update()

    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction="stop"

        for segment in segments:
            segment.goto(1000,1000)

        segments.clear()

        score=0

        delay=0.1

        sc.clear()

        sc.write("Score:{} High score:{}".format(score,highscore),align="center")
    if head.distance(food)<20:
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        food.goto(x,y)

        new_segment=turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color('black')
        new_segment.penup()
        segments.append(new_segment)

        delay-=0.001
        score+=10

        if score>highscore:
            highscore=score
        sc.clear()
        sc.write("Score:{} High score:{}".format(score,highscore),align="center")

    for index in range(len(segments)-1,0,-1):
        x=segments[index-1].xcor()
        y=segments[index-1].ycor()
        segments[index].goto(x,y)
    
    if len(segments)>0:
        x=head.xcor()
        y=head.ycor()
        segments[0].goto(x,y)

    move()

    for segment in segments:
        if segment.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction="stop"

            for segment in segments:
                segment.goto(1000,1000)
            segments.clear()
            score=0
            delay=0.1

            sc.clear()
            sc.write("Score:{} High score:{}".format(score,highscore),align="center")
    time.sleep(delay)
wn.mainloop()

