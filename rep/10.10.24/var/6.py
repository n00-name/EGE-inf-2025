from turtle import *
tracer(0)
screensize(400, 400)
m = 10
left(90)
pendown()
for i in range(4):
    forward(28 * m)
    right(90)
    forward(26 * m)
    right(90)
penup()
forward(8 * m)
right(90)
forward(7 * m)
left(90)
pendown()
for i in range(4):
    forward(67 * m)
    right(90)
    forward(98 * m)
    right(90)
penup()
for x in range(-100, 100):
    for y in range(-100, 100):
        goto(x * m, y * m)
        dot(3)
done()