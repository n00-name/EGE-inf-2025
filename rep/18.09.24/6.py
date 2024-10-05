import turtle as t

k = 15
t.tracer(0,0)
t.right(90)

for i in range(9):
    t.forward(15*k)
    t.right(90)
    t.forward(25*k)
    t.right(90)

t.up()

t.back(10*k)
t.right(90)

t.down()

for i in range(8):
    t.forward(15*k)
    t.left(90)
    t.forward(25*k)
    t.left(90)

t.up()

t.forward(6*k)
t.left(90)

t.down()

for i in range(7):
    t.forward(15*k)
    t.right(90)
    t.forward(25*k)
    t.right(90)

for x in range(-20, 20):
    for y in range(-20, 20):
        t.goto(x*k, y*k)
        if x==0 or y==0:
            t.dot(6)
        else:
            t.dot(4)

t.update()
t.mainloop()