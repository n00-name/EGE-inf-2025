import turtle as t

k = 10
t.tracer(0,0)
t.right(90)

t.right(90)
t.forward(4*k)
t.right(90)
t.forward(48*k)
t.right(90)
t.forward(4*k)
t.right(30)

for i in range(8):
    t.forward(6*k)
    t.right(120)
    t.forward(6*k)
    t.right(240)


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