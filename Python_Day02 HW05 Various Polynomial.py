import turtle

z = turtle.Pen()
s = turtle.Screen()
z . shape("turtle")
s . bgcolor("white")
s . setup(1200,600)

z . color("white")
z . begin_fill()
z . backward(550)
z . end_fill()

z . color("red")
z . width("3")
z . circle(30)

z .up()
z . forward(100)
z . down()

z . circle(30,steps = 3)

z .up()
z . forward(50)
z . down()

z . forward(100)
z . left(90)
z . forward(40)
z . left(90)
z . forward(100)
z . left(90)
z . forward(40)
z . left(90)

z . up()
z . forward(150)
z . down()


z . circle(30,steps = 4)

z .up()
z . forward(100)
z . down()

z . circle(30,steps = 5)

z .up()
z . forward(100)
z . down()

z . circle(30,steps = 6)

z .up()
z . forward(100)
z . down()

z . circle(30,steps = 7)

z .up()
z . forward(100)
z . down()

z . width("3")
z . circle(50,steps = 8)

z .up()
z . forward(150)
z . down()

z . width("3")
z . circle(50,steps = 9)

z .up()
z . forward(150)
z . down()

z . width("3")
z . circle(50,steps = 10)

z .up()
z . forward(50)
z . down()


input ()
