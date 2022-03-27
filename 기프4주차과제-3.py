import random
import turtle
##2019038073신승용##
myTurtle, tX, tY, tColor, tSize, tShape, tSum = [None] * 7
playerTurtles = []
swidth, sheight = 500, 500
##2019038073신승용##
if __name__ == "__main__" :
    turtle.title('거북 리스트 활용(정렬)')
    turtle.setup(width = swidth + 50, height = sheight + 50)
    turtle.screensize(swidth, sheight)

    for i in range(0, 5) :
        myTurtle = turtle.Turtle('turtle')
        tX = random.randrange(-swidth / 2, swidth / 2)
        tY = random.randrange(-sheight / 2, sheight / 2)
        r = random.random(); g = random.random(); b = random.random()
        tSize = random.randrange(1,100)/10
        tSum = tX + tY
        playerTurtles.append([myTurtle, tX, tY, tSize, r, g, b, tSum])
##2019038073신승용##
    sortedTurtles = sorted(playerTurtles, key = lambda turtles : turtles[3], reverse = True)
    for index, tList in enumerate(sortedTurtles[0:]):
        myTurtle = tList[0]
        myTurtle.color((tList[4], tList[5], tList[6]))
        myTurtle.pencolor((tList[4], tList[5], tList[6]))
        myTurtle.turtlesize(tList[3])
        myTurtle.penup()
        if index == 0:
            myTurtle.goto(tList[1], tList[2])
            continue
        myTurtle.goto(sortedTurtles[index-1][1], sortedTurtles[index-1][2])
 
        myTurtle.pendown()
        myTurtle.goto(tList[1], tList[2])
##2019038073신승용##
turtle.done()

