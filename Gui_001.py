from selectFile import *
from tkinter import *
from tkinter import ttk

def donothing():
    x = 0

v02 = 1
t02 = v02+1

def calling_Gui():
    root = Tk()

    ###########################

    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="New", command=donothing)
    filemenu.add_command(label="Open", command=donothing)
    filemenu.add_command(label="Save", command=donothing)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=root.destroy)
    menubar.add_cascade(label="File", menu=filemenu)
    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Help Index", command=donothing)
    helpmenu.add_command(label="About...", command=donothing)
    menubar.add_cascade(label="Help", menu=helpmenu)
    root.config(menu=menubar)

    ###########################

    frm = ttk.Frame(root, padding=200)
    frm.grid()

    ttk.Label(frm, text="label2!").grid(column=0, row=t02)
    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=t02)

    ttk.Label(frm, text="Hello World!").grid(column=0, row=v02)
    ttk.Button(frm, text="window1", command=selectFile).grid(column=1, row=v02)

    ###########################

    root.mainloop()
