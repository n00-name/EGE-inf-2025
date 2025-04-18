import turtle as t

t.tracer(0)
t.screensize(5000, 5000)

k = 40
t.left(90)
t.down()

for i in range(2):
    t.forward(10*k)
    t.right(90)
    t.forward(20*k)
    t.right(90)

t.penup()
t.back(15*k)
t.right(90)
t.back(10*k)
t.left(90)
t.down()

for i in range(2):
    t.forward(20*k)
    t.right(90)
    t.forward(25*k)
    t.right(90)

t.penup()

for x in range(-30, 30):
    for y in range(-30, 30):
        t.setpos(x*k, y*k)
        t.dot()
t.update()
t.done()