import turtle as t

t.tracer(0)
t.screensize(5000, 5000)

k = 40
t.left(90)
t.down()

for i in range(2):
    t.forward(9*k)
    t.right(90)
    t.forward(15*k)
    t.right(90)

t.penup()
t.forward(12*k)
t.right(90)
t.down()

for i in range(2):
    t.forward(6*k)
    t.right(90)
    t.forward(12*k)
    t.right(90)

t.penup()

for x in range(-30, 30):
    for y in range(-30, 30):
        t.setpos(x*k, y*k)
        t.dot()
t.update()
t.done()