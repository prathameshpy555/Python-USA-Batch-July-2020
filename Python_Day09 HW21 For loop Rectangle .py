
# Rectangle using For loop:

import turtle
c=turtle.Pen()
scr = turtle.Screen()
scr . setup(600,600)
c.width(5)
c.color("blue","yellow")
c.begin_fill()

for i in range (2) :
              c.forward(200)
              c.left(90)
              
              c.forward(100)
              c.left(90)
              
c.end_fill()

input()
