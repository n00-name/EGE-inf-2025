import turtle as t

k = 10
t.tracer(0,0)


t.forward(25*k)
t.right(90)
t.forward(5*k)
t.left(90)

t.down()

for i in range(9):
    t.forward(53*k)
    t.right(90)
    t.forward(75*k)
    t.right(90)

t.up()
for x in range(-30, 30):
    for y in range(-20, 20):
        t.goto(x*k, y*k)
        if x==0 or y==0:
            t.dot(6)
        else:
            t.dot(4)

t.update()
t.mainloop()