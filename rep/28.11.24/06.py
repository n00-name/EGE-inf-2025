import turtle as t

k = 15
t.tracer(0,0)


for i in range(2):
    t.forward(50*k)
    t.right(90)
    t.forward(80*k)
    t.right(90)

t.up()

t.forward(8*k)
t.right(90)
t.back(5)
t.left(90)

t.down()

for i in range(2):
    t.forward(20*k)
    t.right(90)
    t.forward(12*k)
    t.right(90)

t.up()

for x in range(-20, 20):
    for y in range(-20, 20):
        t.goto(x*k, y*k)
        if x==0 or y==0:
            t.dot(6)
        else:
            t.dot(4)

t.update()
t.mainloop()