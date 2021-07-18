from turtle import *
from random import randint

'''
print('Введите кол-во беговых дорожек:')
n = int(input('Введите кол-во беговых дорожек:\n'))
print('Введите длину беговых дорожек:')
l = int(input('Введите длину беговых дорожек:\n'))
'''
n = 4
l = 200

x = (n - 1) * 10
y = l / 2

penup()
speed(0)
goto(-x, y)

for i in range(n):
    pendown()
    write(i)
    right(90)
    for i in range(5):
        forward(10)
        penup()
        forward(5)
        pendown()
        forward(10)
        penup()
        forward(5)
        pendown()
        forward(10)

    penup()
    backward(l)
    left(90)
    forward(50)

red = Turtle()
red.shape("turtle")
red.color("red")
red.penup()
red.goto(-x - 20, y - 20)

blue = Turtle()
blue.shape("turtle")
blue.color("blue")
blue.penup()
blue.goto(-x - 20, y - 60)

yellow = Turtle()
yellow.shape("turtle")
yellow.color("yellow")
yellow.penup()
yellow.goto(-x - 20, y - 100)

green = Turtle()
green.shape("turtle")
green.color("green")
green.penup()
green.goto(-x - 20, y - 140)

black = Turtle()
black.shape("turtle")
black.penup()
black.goto(-x - 20, y - 180)

result = []

while (len(result) < 5):
    if (red.position()[0] < 140):
        red.forward(randint(0, 10))
    elif "red" not in result:
        result.append("red")
    if (blue.position()[0] < 140):
        blue.forward(randint(0, 10))
    elif "blue" not in result:
        result.append("blue")
    if (yellow.position()[0] < 140):
        yellow.forward(randint(0, 10))
    elif "yellow" not in result:
        result.append("yellow")
    if (green.position()[0] < 140):
        green.forward(randint(0, 10))
    elif "green" not in result:
        result.append("green")
    if (black.position()[0] < 140):
        black.forward(randint(0, 5))
    elif "black" not in result:
        result.append("black")
print(result)

'''
turtles = [red, blue, yellow, green, black]
for i in range (len(turtles)):
    turtles[i].goto(0,i*20)
'''
