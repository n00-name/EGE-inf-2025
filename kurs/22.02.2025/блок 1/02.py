import turtle as t

t.tracer(0)
t.screensize(5000, 5000)

k = 40
t.left(90)
t.down()

t.right(30)
for i in range(6):
    t.forward(7*k)
    t.right(120)
    t.forward(7 * k)
    t.right(60)

t.penup()

for x in range(-30, 30):
    for y in range(-30, 30):
        t.setpos(x*k, y*k)
        t.dot()
t.update()
t.done()