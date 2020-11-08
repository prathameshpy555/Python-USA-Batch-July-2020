# spiral Triangle :

import turtle
t=turtle.Pen()
scr=turtle.Screen()
scr.setup(1200,600)
scr.title("My drawings")
t . width(3)
n=int(turtle.numinput("Spiral Square","How many spirals?"))
t . speed(0)

for i in range(1,n+1)   :
    t . forward(i*6)
    t . left(120)
