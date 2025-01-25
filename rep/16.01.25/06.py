import turtle as t

k = 15
t.tracer(0,0)
t.right(90)

for i in range(5):
    t.forward(30*k)
    t.right(90)
    t.forward(5*k)
    t.right(90)


t.up()

t.forward(20*k)
t.right(90)
t.forward(5*k)
t.right(90)

t.down()

for i in range(7):
    t.forward(10*k)
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