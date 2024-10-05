import turtle as t

k = 10
t.tracer(0,0)
t.right(90)

for i in range(2):
    t.forward(15*k)
    t.left(90)
    t.forward(20*k)
    t.left(90)


t.up()

t.right(90)
t.backward(7*k)
t.left(90)
t.forward(9*k)

t.down()

for i in range(2):
    t.forward(17*k)
    t.right(90)
    t.forward(15*k)
    t.right(90)


t.up()


for x in range(-50, 50):
    for y in range(-50, 50):
        t.goto(x*k, y*k)
        if x==0 or y==0:
            t.dot(6)
        else:
            t.dot(4)

t.update()
t.mainloop()