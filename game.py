import turtle
import os
import math
import random

def move_left():          #for moving the player
    x = player.xcor()
    x -= playerspeed
    if x < -630:
        x = -630
    player.setx(x)

def move_right():          #for moving the player
    x = player.xcor()
    x += playerspeed
    if x > 630:
        x = 630
    player.setx(x)

def move_up():
    y = player.ycor()
    y += playerspeed
    if y > 350:
        y = 350
    player.sety(y)

def move_down():
    y = player.ycor()
    y -= playerspeed
    if y < -350:
        y = -350
    player.sety(y)

def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor() - t2.ycor(),2))
    if distance < 35:
        return True
    else:
        return False


#main settings
cookiespeed = 2
broccolispeed = 1
playerspeed = 30

lifes = 3
score = 0

lifes_pen = turtle.Turtle()
lifes_pen.speed(0)
lifes_pen.penup()
lifes_pen.color("Black")
lifes_pen.setposition(-540, 320)
lifesstring = "Lifes: %s" %lifes
lifes_pen.write(lifesstring, False, align="right", font=("Arial", 14, "normal"))
lifes_pen.hideturtle()

score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.penup()
score_pen.color("black")
score_pen.setposition(540,320)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align="left", font=("Arial" , 14, "normal"))
score_pen.hideturtle()

wn = turtle.Screen() #setting up the playing field
wn.screensize(canvwidth = 1920, canvheight = 1080, bg = "white")
wn.title("CookEIE Monster")

border_pen = turtle.Turtle() #setting up boarder
border_pen.speed(0)
border_pen.color("Black")
border_pen.penup()
border_pen.setposition(-640,-360)
border_pen.pendown()
border_pen.pensize(3)
for side in range(2):
    border_pen.fd(1280)
    border_pen.lt(90)
    border_pen.fd(720)
    border_pen.lt(90)
border_pen.hideturtle()

turtle.register_shape("cookie.gif")
turtle.register_shape("art.gif")

player = turtle.Turtle() #creating the player
player.color("red")
player.shape("square")
player.penup()
player.speed(0)
player.setposition(0,-350)

number_of_cookies = 3
cookies = []

for i in range(number_of_cookies):
    cookies.append(turtle.Turtle())

for cookie in cookies:    #creating cookie
    cookie.color("Brown")
    cookie.shape("cookie.gif")
    cookie.penup()
    cookie.speed(0)
    x = random.randint(-620, 620)
    cookie.setposition(x,350)

broccoli = turtle.Turtle()  #creating broccoli
broccoli.color("Red")
broccoli.shape("art.gif")
broccoli.penup()
broccoli.speed(0)
xb = random.randint(-620, 620)
broccoli.setposition(xb,350)



turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(move_up, "Up")
turtle.onkey(move_down, "Down")

game = True

#game loop
while game:

    for cookie in cookies:
        y = cookie.ycor() #Cookie Move
        y -= cookiespeed
        if y < -350:
           lifes = lifes - 1
           lifesstring = "Lifes: %s" %lifes
           lifes_pen.clear()
           lifes_pen.write(lifesstring, False, align="right", font=("Arial", 14, "normal"))
           x = random.randint(-620,620)
           cookie.setposition(x,350)
        else:
            cookie.sety(y)
        if isCollision(player, cookie):
            score += 10
            if score%50 == 0:
                cookiespeed += 1
                broccolispeed += 1
            scorestring = "Score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial" , 14, "normal"))
            x = random.randint(-620,620)
            cookie.setposition(x,350)

    if lifes == 0:
        game = False;

    yb = broccoli.ycor()
    yb -= broccolispeed
    if yb < -350:
        xb = random.randint(-620,620)
        broccoli.setposition (xb,350)
    else:
        broccoli.sety(yb)

    if isCollision(player, broccoli):
        xb = random.randint(-620,620)
        broccoli.setposition (xb,350)
        lifes = lifes - 1
        lifesstring = "Lifes: %s" %lifes
        lifes_pen.clear()
        lifes_pen.write(lifesstring, False, align="right", font=("Arial", 14, "normal"))


    if lifes == 0:
        game = False;

print(score)
