from tkinter import *
##2019038073신승용##
def myFunc() :
    if var.get()==1:
        labelImage.configure(image=photo1)
    elif var.get()==2:
        labelImage.configure(image=photo2)
    else:
        labelImage.configure(image=photo3)
##2019038073신승용##
var,labelImage=0,None
photo1,photo2,photo3=[None]*3

window=Tk()
window.geometry("400x500")
window.title("애완동물 선택하기")
labelText=Label(window,text="좋아하는 동물 투표",fg="blue",font=("궁서체",20))
##2019038073신승용##
var=IntVar()
rb1=Radiobutton(window,text="강아지",variable=var,value=1)
rb2=Radiobutton(window,text="고양이",variable=var,value=2)
rb3=Radiobutton(window,text="토끼",variable=var,value=3)
button0k=Button(window,text="사진보기",command=myFunc)

photo1=PhotoImage(file="dog3.gif")
photo2=PhotoImage(file="cat.gif")
photo3=PhotoImage(file="rabbit.gif")
##2019038073신승용##
labelImage=Label(window,width=300,height=300,bg="yellow",image=None)

labelText.pack(padx=5,pady=5)
rb1.pack(padx=5,pady=5)
rb2.pack(padx=5,pady=5)
rb3.pack(padx=5,pady=5)
button0k.pack(padx=5,pady=5)
labelImage.pack(padx=5,pady=5)
##2019038073신승용##
window.mainloop()
