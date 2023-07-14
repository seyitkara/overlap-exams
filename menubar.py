import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import tkinter
from tkinter import filedialog
from tkinter import Tk,ttk
import os
import openpyxl
from selectFile import *
from tkinter import *

def menubar01():
    root = tkinter.Tk()
    root.withdraw() #use to hide tkinter window
  
    def search_for_excel1 ():
        currdir = os.getcwd()
        tempdir = filedialog.askopenfilename(parent=root, initialdir=currdir, title='Please select a directory')
        if len(tempdir) > 0:
            print ("You chose: %s" % tempdir)
        return tempdir
    
    def search_for_excel2 ():
        currdir = os.getcwd()
        tempdir = filedialog.askopenfilename(parent=root, initialdir=currdir, title='Please select a directory')
        if len(tempdir) > 0:
            print ("You chose: %s" % tempdir)
        return tempdir

    def about01():
        root = Tk()

        ttk.Label(root, text="Bu Uygulama Seyit Ali KARA tarafından Hazırlanmıştır!").grid(column=0, row=0)
        ttk.Button(root, text="Quit", command=destroy).grid(column=1, row=0)

        root.mainloop()
            