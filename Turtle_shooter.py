import turtle
import math
import random

#
wn = turtle.Screen()
wn.bgcolor('black')
wn.title('Space Invaders')
pen = turtle.Turtle()
pen.speed(0)
pen.color('red')
pen.penup()
pen.setposition(-300, -300)
pen.pensize(4)
pen.pendown()

for side in range(4):
    pen.fd(600)
    pen.lt(90)
pen.hideturtle()

player = turtle.Turtle()
player.color('red')
player.shape('turtle')
player.penup()
player.speed(0)

#
playerspeed = 30


def mowe_right():
    x = player.xcor()
    x += playerspeed
    player.setx(x)


def mowe_left():
    x = player.xcor()
    x -= playerspeed
    player.setx(x)


def mowe_up():
    y = player.ycor()
    y += playerspeed
    player.sety(y)


def mowe_down():
    y = player.ycor()
    y -= playerspeed
    player.sety(y)


def fire_bullet():
    global bulletstate
    if bulletstate == 'ready':
        bulletstate = 'fire'
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()


def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if distance < 15:
        return True

    else:

        return False


turtle.listen()
turtle.onkey(mowe_right, 'Right')
turtle.onkey(mowe_left, 'Left')
turtle.onkey(mowe_up, 'Up')
turtle.onkey(mowe_down, 'Down')
turtle.onkey(fire_bullet, 'space')

#
number_of_enemies = 5
enemies = []
for i in range(number_of_enemies):
    enemies.append(turtle.Turtle())

for enemy in enemies:
    enemy.color('red')
    enemy.shape('circle')
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 200)
    enemy.setposition(x, y)
enemyspeed = 1
#

bullet = turtle.Turtle()
bullet.color('blue')
bullet.shape('circle')
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.2, 0.8)
bullet.pendown()
bullet.hideturtle()
bulletspeed = 20
bulletstate = 'ready'
bullet.penup()

#
while True:
    for enemy in enemies:
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        if enemy.xcor() > 280:
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemyspeed *= -1

        if enemy.xcor() < -280:
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemyspeed *= -1
        if isCollision(bullet, enemy):
            bullet.hideturtle()
            bulletstate = 'ready'
            bullet.setposition(0, -400)
            x = random.randint(-200, 200)
            y = random.randint(100, 200)
            enemy.setposition(x, y)

        if isCollision(player, enemy):
            player.hideturtle()
            enemy.hideturtle()
            break

    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = 'ready'
