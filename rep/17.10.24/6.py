import turtle as t

k = 30
t.tracer(0,0)
t.right(90)


for i in range(8):
    t.right(45)
    t.forward(3*k)


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