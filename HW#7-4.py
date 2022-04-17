from tkinter import *
from tkinter.filedialog import *
from tkinter.simpledialog import *
##2019038073신승용##
def func_open():
    global filename
    filename = askopenfilename(parent = window, filetypes = (("GIF 파일", "*.gif"),
                ("모든 파일", "*.*")))
    photo = PhotoImage(file = filename)
    pLabel.configure(image = photo)
    pLabel.image = photo
##2019038073신승용##
def func_exit():
    window.quit()
    window.destroy() 
##2019038073신승용##
def func_zoom(up):
    value = 2
    photo = PhotoImage(file = filename)
    photo = photo.zoom(value,value)
    pLabel.configure(image = photo)
    pLabel.image = photo
##2019038073신승용##
def func_subsample(down):
    value = 2
    photo = PhotoImage(file = filename)
    photo = photo.subsample(value,value)
    pLabel.configure(image = photo)
    pLabel.image = photo


##2019038073신승용##    
window = Tk()
window.geometry("400x400")
window.title("귀여운 강아지")

photo = PhotoImage()
pLabel = Label(window,image = photo)
pLabel.pack(expand = 1, anchor = CENTER)

mainMenu = Menu(window)
window.config(menu = mainMenu)

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label = '파일',menu = fileMenu)
fileMenu.add_command(label = '파일 열기', command = func_open)
fileMenu.add_separator()
fileMenu.add_command(label = '프로그램 종료', command = func_exit)

window.bind("<Up>",func_zoom)
window.bind("<Down>",func_subsample)

window.mainloop()

