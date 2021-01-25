# Final Project 1 :
import turtle
t=turtle.Pen()
scr=turtle.Screen()
scr.bgcolor("black")
scr.setup(1200,650)
t.color("red")
t.width(3)
colors=['red','blue','orange','cyan','green','white']
a=turtle.textinput("Race game...","Enter Player 1 name : ")
b=turtle.textinput("Race game...","Enter Player 2 name : ")
c=turtle.textinput("Race game...","Enter Player 3 name : ")
d=turtle.textinput("Race game...","Enter Player 4 name : ")
e=turtle.textinput("Race game...","Enter Player 5 name : ")
f=("")
names=[a,b,c,d,e,f]


t.speed(0)
x=450
y=250
t.up()
t.goto(-x,y)
t.down()


for i in range(6) :
    t.color(colors[i])
    t.up()
    t.goto(-x,y)
    t.down()
    t.write(names[i],font=("arial",20))
    for i in range(40):
        t.forward(10)
        t.up()
        t.forward(10)
        t.down()
    y=y-100

t.color('pink')
t.begin_fill()
t.left(90)
t.backward(100)
t.forward(700)
t.end_fill()

# Player 1 :
p1=turtle.Pen()
x=450
y=250
p1.shape('turtle')
p1.color(colors[0])
p1.begin_fill()
p1.up()
p1.goto(-x,y=y-50)
p1.down()
p1.end_fill()


# Player 2 :
p2=turtle.Pen()
x=450
y=250
p2.shape('turtle')
p2.color(colors[1])
p2.begin_fill()
p2.up()
p2.goto(-x,y=y-150)
p2.down()
p2.end_fill()

# Player 3 :
p3=turtle.Pen()
x=450
y=250
p3.shape('turtle')
p3.color(colors[2])
p3.begin_fill()
p3.up()
p3.goto(-x,y=y-250)
p3.down()
p3.end_fill()

# Player 4 :
p4=turtle.Pen()
x=450
y=250
p4.shape('turtle')
p4.color(colors[3])
p4.begin_fill()
p4.up()
p4.goto(-x,y=y-350)
p4.down()
p4.end_fill()

# Player 5 :
p5=turtle.Pen()
x=450
y=250
p5.shape('turtle')
p5.color(colors[4])
p5.begin_fill()
p5.up()
p5.goto(-x,y=y-450)
p5.down()
p5.end_fill()

'''
---------------------------------------
'''
# Text :

x=450
y=250
import random
turtle.colormode(255)
r=random.randint(222,222)
g=random.randint(27,27)
b=random.randint(243,243)
t.up()
t.goto(-x,y=y+50)
t.down()
t.color(r,g,b)
t.write("Let's Start The Race!!!!",font=("candara",30))
'''
----------------------------------------

'''
# starting race
p1.width(3)
p2.width(3)
p3.width(3)
p4.width(3)
p5.width(3)

p1_p=0
p2_p=0
p3_p=0
p4_p=0
p5_p=0
for i in range(155) :
    r1=random.randint(1,10)
    p1.forward(r1)
    p1_p = p1_p+r1
    
    r2=random.randint(1,10)
    p2.forward(r2)
    p2_p = p2_p+r2
    
    r3=random.randint(1,10)
    p3.forward(r3)
    p3_p = p3_p+r3
    
    r4=random.randint(1,10)
    p4.forward(r4)
    p4_p = p4_p+r4
    
    r5=random.randint(1,10)
    p5.forward(r5)
    p5_p = p5_p+r5



print("Player 1 :",p1_p)
print("Player 2 :",p2_p)
print("Player 3 :",p3_p)
print("Player 4 :",p4_p)
print("Player 5 :",p5_p)

k=[p1_p,p2_p,p3_p,p4_p,p5_p]
print()

t.color("purple")
t.begin_fill()
t.up()
t.goto(-400,-300)
t.down()

if p1_p == max(k) :
    t.write("Winner with fastest run is " + str(names[k.index(max(k))]) + " in "+ str(max(k)) + " miliseconds",font=("candara",20))

elif p2_p == max(k) :
    t.write("winner with fastest run is " + str(names[k.index(max(k))]) + " in "+ str(max(k)) + " miliseconds",font=("candara",20))

elif p3_p == max(k) :
    t.write("winner with fastest run is " + str(names[k.index(max(k))]) + " in "+ str(max(k)) + " miliseconds",font=("candara",20))
            
elif p4_p == max(k) :
    t.write("winner with fastest run is " + str(names[k.index(max(k))]) + " in "+ str(max(k)) + " miliseconds",font=("candara",20))

elif p5_p == max(k) :
    t.write("winner with fastest run is " + str(names[k.index(max(k))]) + " in "+ str(max(k)) + " miliseconds",font=("candara",20))

t.end_fill()
print("winner with fastest run is", names[k.index(max(k))]," in ",max(k),"miliseconds")

input()





