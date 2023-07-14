from Gui_001 import *
from tkinter import *
from tkinter import ttk

def donothing():
   x = 0

v02 = 1
t02 = v02+1

root = Tk()
frm = ttk.Frame(root, padding=200)
frm.grid()

ttk.Label(frm, text="label2!").grid(column=0, row=t02)
ttk.Button(frm, text="Quit", command=exit).grid(column=1, row=t02)

ttk.Label(frm, text="calling_Gui!").grid(column=0, row=v02)
ttk.Button(frm, text="calling_Gui", command=calling_Gui).grid(column=1, row=v02)

root.mainloop()
    
if __name__ == "__main__":
    print("Hello, World!")
