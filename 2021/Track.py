import turtle, random
from turtle import *

number = int(input('Введите число беговых дорожек: '))
length = []
colors = ['red', 'blue', 'green', 'grey', 'orange', 'brown']
for i in range(number):
    length.append(int(input('Введите длину дорожки №' + str(i) + ':')))
print(length)

speed(6)
penup()
goto(-100, 0)
for x in range(number):
    pendown()
    color('black')
    write(x)
    color(random.choice(colors))
    right(90)
    fd(length[x])
    backward(length[x])
    left(90)
    penup()
    fd(10)

hideturtle()
turtle.Screen().exitonclick()
