
# Triangle using For loop:

import turtle
p=turtle.Pen()
p.width(5)
scr = turtle.Screen()
scr . setup(600,600)
p.color("orange","pink")
p.begin_fill()

for i in range(3) :
              p . forward(200)
              p . left(120)
p.end_fill()

input()
