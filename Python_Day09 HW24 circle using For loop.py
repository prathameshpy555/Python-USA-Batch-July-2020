
# Circle using For loop:

import turtle
t = turtle.Pen()
scr = turtle.Screen()
scr . setup(1200,600)
t . width(5)
t . up()
t . backward(300)
t . down()
t . color("black","green")
t . begin_fill()
for i in range (10) :
              t . circle(30)
              t . up()
              t . forward(70)
              t . down()
t . end_fill()    
