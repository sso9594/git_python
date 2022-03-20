import turtle
i,k,tx,ty=[0]*4
zwidth,zheight=800,450
##2019038073 신승용##
if __name__=="__main__":
    turtle.title('거북 구구단')
    turtle.shape('turtle')
    turtle.setup(width=zwidth+50,height=zheight+50)
    turtle.screensize(zwidth,zheight)
    turtle.penup()
    tx,ty=-500,250
    turtle.goto(tx,ty)
##2019038073 신승용##
    for i in range(1,10):
        for k in range(2,10):
            turtle.goto(tx+80*k,ty-40*i)
            mult=str(k)+' x '+str(i)+' = '+str(k*i)
            turtle.write(mult,font=('Arial',12,'bold'))
##2019038073 신승용##
    turtle.done()
