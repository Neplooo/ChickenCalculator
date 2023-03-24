#-- Import Libraries--#
import tkinter as tk
from tkinter import *
from tkinter import ttk
import os

#Sets variables that will be used
count = 0

#Establishes page root object
root = tk.Tk()

#Creates variables for widgets
vegan = IntVar()

#Specifes base conditions for root window
root.geometry("200x300")
root.title("Chicken Calculator")
root.iconbitmap("C:/Users/alber/Downloads/ChickenCalculator/GUI/Assets/pythontutorial-1-150x150.ico")

#Creates an object for where the widgets will go.
frame = tk.Frame(root)
frame.grid(row=0, column=0)

Grid.rowconfigure(root,0,weight=1)
Grid.columnconfigure(root,0,weight=1)

title = tk.Label(frame, text="Chicken Calculator", font=("Helvetica", 11))
title.grid(row=1, columnspan=7, column=0, sticky="NSEW")

listbox = tk.Listbox(frame)
listbox.grid(row=2, columnspan=3, column=0, sticky="NSEW")

header = tk.Label(frame, text="Input your age below:", font=("Helvetica", 9))
header.grid(row=3, columnspan=3, column=0, sticky="NSEW")

entrybox = tk.Entry(frame)
entrybox.grid(row=4, columnspan=3, column=0, sticky="NSEW")

def calculate():
    #pass
    age = 0
    age = float(entrybox.get())
    chickensEaten = age * 33.80
    if vegan.get() == 1:
        chickensEaten = 0
    elif vegan.get() == 0:
        pass
    listbox.insert(count + 1, round(chickensEaten))
    entrybox.delete(0, END)

veganCheck = tk.Checkbutton(frame, text="Vegan", onvalue=1, offvalue=0,variable=vegan, command=calculate)
veganCheck.grid(row=5, columnspan=3, column=0, sticky="NSEW")

submitbox = tk.Button(frame, text="Submit", command=calculate)
submitbox.grid(row=6, columnspan=3, column=0, sticky="NSEW")

def openAbout():
    os.system("C:/Users/alber/OneDrive/Documents/ChickenCalculator/GUI/AboutUs.py")

aboutButton = tk.Button(frame, text="What is this?", command=openAbout)
aboutButton.grid(row=7 , columnspan=3, column=0, sticky="NSEW")

root.mainloop()