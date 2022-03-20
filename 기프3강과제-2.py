import turtle
import math
import random
##2019038073 신승용##


t1=list(range(3))
t2=list(range(3))
t3=list(range(3))
t1X=list(range(6))
t1Y=list(range(6))
t2X=list(range(6))
t2Y=list(range(6))
t3X=list(range(6))
t3Y=list(range(6))
zwidth,zheight=300,300
##2019038073 신승용##

          
if __name__=="__main__":
    turtle.title('거북이 만나기')
    turtle.setup(width=zwidth+30,height=zheight+30)
    turtle.screensize(zwidth,zheight)

    t1 = turtle.Turtle('turtle'); t1.color('red'); t1.speed(10); t1.penup()
    t2 = turtle.Turtle('turtle'); t2.color('green'); t2.speed(10); t2.penup()
    t3 = turtle.Turtle('turtle'); t3.color('blue'); t3.speed(10); t3.penup()
    t1.goto(-100, -100); t2.goto(0, 0); t3.goto(100, 100)
    while True:
        angle = random.randrange(0, 360)
        dist = random.randrange(1, 50)
        t1.left(angle); t1.forward(dist)
        angle = random.randrange(0, 360)
        dist = random.randrange(1, 50)
        t2.left(angle); t2.forward(dist)
        angle = random.randrange(0, 360)
        dist = random.randrange(1, 50)
        t3.left(angle); t3.forward(dist)

        t1X = t1.xcor(); t1Y = t1.ycor()
        t2X = t2.xcor(); t2Y = t2.ycor()
        t3X = t3.xcor(); t3Y = t3.ycor()
##2019038073 신승용##


        if math.sqrt(((t1X-t2X)*(t1X-t2X))+((t1Y-t2Y)*(t1Y-t2Y)))<= 30 or \
            math.sqrt(((t1X-t3X)*(t1X-t3X))+((t1Y-t3Y)*(t1Y-t3Y)))<= 30 or \
            math.sqrt(((t2X-t3X)*(t2X-t3X))+((t2Y-t3Y)*(t2Y-t3Y)))<= 30 :

            t1.turtlesize(3); t2.turtlesize(3); t3.turtlesize(3)
            break

##2019038073 신승용##
 

turtle.done()
