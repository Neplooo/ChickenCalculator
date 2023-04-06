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
root.iconbitmap("Your Icon Here")

#Creates an object for where the widgets will go.
frame = tk.Frame(root)
frame.grid(row=0, column=0)

#Configure the columns and rows
Grid.rowconfigure(root,0,weight=1)
Grid.columnconfigure(root,0,weight=1)

#Create the title
title = tk.Label(frame, text="Chicken Calculator", font=("Helvetica", 11))
title.grid(row=1, columnspan=7, column=0, sticky="NSEW")

#Create the result box
listbox = tk.Listbox(frame)
listbox.grid(row=2, columnspan=3, column=0, sticky="NSEW")

#Creates the object for instructions
header = tk.Label(frame, text="Input your age below:", font=("Helvetica", 9))
header.grid(row=3, columnspan=3, column=0, sticky="NSEW")

#Creates the Spot to enter age
entrybox = tk.Entry(frame)
entrybox.grid(row=4, columnspan=3, column=0, sticky="NSEW")

#This function calculates the chickens you've eaten based on age
def calculate():
    #Defines an age variable
    age = 0
    #Sets the age variable to what was inside the entrybox
    age = float(entrybox.get())
    #Multiplies the average amount of chickens eaten per year by your age
    chickensEaten = age * 33.80
    #If you are a vegan, it sets the amount of chickens eaten to 0
    #If not, it continues
    if vegan.get() == 1:
        chickensEaten = 0
    elif vegan.get() == 0:
        pass
    #We insert our value back into the listbox
    listbox.insert(count + 1, round(chickensEaten))
    #Deletes the value from the entrybox so you can enter a new value
    entrybox.delete(0, END)

#Check box to signal if your a vegan
veganCheck = tk.Checkbutton(frame, text="Vegan", onvalue=1, offvalue=0,variable=vegan, command=calculate)
veganCheck.grid(row=5, columnspan=3, column=0, sticky="NSEW")

#Creates a submit box that runs the calculate command
submitbox = tk.Button(frame, text="Submit", command=calculate)
submitbox.grid(row=6, columnspan=3, column=0, sticky="NSEW")

#This function opens another program. (About us page)
def openAbout():
    os.system("About Us directory here")

#Creates a button that opens the about menu
aboutButton = tk.Button(frame, text="What is this?", command=openAbout)
aboutButton.grid(row=7 , columnspan=3, column=0, sticky="NSEW")

#Runs the app
root.mainloop()
