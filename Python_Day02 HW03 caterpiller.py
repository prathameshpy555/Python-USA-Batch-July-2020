# Draw a caterpiller:

import turtle
z = turtle.Pen()
z . shape("turtle")

s = turtle.Screen()
s . bgcolor("green")
s . setup(1200,600)
z . width(4)





z . up()
z . backward(200)
z . down()
z . width("5")

z . color("black","yellow")
z . begin_fill()
z . circle(25)
z . end_fill()


z . up()
z . forward(50)
z . down()

z . color("black","red")
z . begin_fill()
z . circle(25)
z . end_fill()

z . up()
z . forward(50)
z . down()

z . color("black","orange")
z . begin_fill()
z . circle(25)
z . end_fill()

z . up()
z . forward(50)
z . down()

z . color("black","pink")
z . begin_fill()
z . circle(25)
z . end_fill()

z . up()
z . forward(50)
z . down()


z . color("black","cyan")
z . begin_fill()
z . circle(25)
z . end_fill()

z . up()
z . forward(50)
z . down()

z . color("black","blue")
z . begin_fill()
z . circle(25)
z . end_fill()

z . circle(25,110)

z . right(90)

z . circle(25,100)

z . color("black","yellow")
z . begin_fill()
z . circle(5)
z . end_fill()

z . right(45)

z . up()
z . backward(55)
z . down()

z . right(90)
z . circle(-25,100)

z . color("black","yellow")
z . begin_fill()
z . circle(-5)
z . end_fill()





z . hideturtle()

input()
