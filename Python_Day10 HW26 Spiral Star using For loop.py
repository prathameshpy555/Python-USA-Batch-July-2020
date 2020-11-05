# Spiral Star using For loop :

import turtle

p = turtle.Pen()
scr = turtle.Screen()
p . width(1)
n=int(turtle.numinput("Spiral Square","How many spirals?"))
p . speed(0)
for i in range (1,n+2) :
              p . forward(i*5)
              p . left(145)


input()
