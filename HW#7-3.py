from tkinter import *
from tkinter import ttk

window=Tk()
##2019038073 신승용##

baseTab=ttk.Notebook(window)

tabDog=ttk.Frame(baseTab)
baseTab.add(tabDog,text='강아지')
tabCat=ttk.Frame(baseTab)
baseTab.add(tabCat,text='고양이')

baseTab.pack(expand=1,fill="both")

photoDog=PhotoImage(file="dog3.gif")
labelDog=Label(tabDog,image=photoDog)
labelDog.pack()
##2019038073 신승용##
photoCat=PhotoImage(file="cat.gif")
labelCat=Label(tabCat,image=photoCat)
labelCat.pack()

window.mainloop()
