import turtle as t

t.tracer(0)

k = 30

for i in range(15):
    t.forward(15*k)
    t.left(120)

t.penup()

for x in range(-2, 30):
    for y in range(-2, 30):
        t.setpos(x*k, y*k)
        t.dot()

t.done()