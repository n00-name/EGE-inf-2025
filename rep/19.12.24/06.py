import turtle as t

k = 15
t.tracer(0,0)
t.right(90)


for i in range(10):
    t.forward(22*k)
    t.right(90)
    t.forward(16*k)
    t.right(90)


t.up()
t.forward(1*k)
t.right(90)
t.forward(1*k)
t.left(90)

t.down()

for i in range(10):
    t.forward(72*k)
    t.right(90)
    t.forward(79*k)
    t.right(90)

t.up()

for x in range(-30, 30):
    for y in range(-30, 30):
        t.goto(x*k, y*k)
        if x==0 or y==0:
            t.dot(6)
        else:
            t.dot(4)

t.update()
t.mainloop()