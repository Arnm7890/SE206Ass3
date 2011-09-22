#!/usr/bin/python

# SOFTENG 206 Assignment 3
# Andrew Luey and Arunim Talwar
# Date: September 2011
# Description: The screen which shows when the program starts up


from Tkinter import Tk, Button, Frame, Label, Toplevel
from tkMessageBox import askyesno
import GUI

  
def teacherInterface():
    """ Staroots the teacher interface """
    global root
    student = Toplevel(root)
    student.title("Teacher Interface")
    gui = GUI.GUI(student)

def exit():
    """ Confirms program quit """
    if askyesno('Exit', 'Are you sure you wish to exit?', icon="warning"):
        root.destroy()
        
        
# Initialize GUI
root = Tk()
root.title("Spelling Quiz Game")
Label(root, text='Spelling Quiz Game').pack(pady=20, padx=60) 

# Frame for buttons
btnContainer = Frame(root)
btnContainer.pack(pady=10)

# Buttons
QuizBtn = Button(btnContainer, text="Start Quiz")
QuizBtn.grid(row=0, column=0, padx=10)
StudentRecBtn = Button(btnContainer, text="Student Records")
StudentRecBtn.grid(row=0, column=1, padx=10)
manageListsBtn = Button(btnContainer, text="Manage Lists", command=teacherInterface)
manageListsBtn.grid(row=0, column=2, padx=10)
exitBtn = Button(btnContainer, text="Exit", command=exit, bg="grey")
exitBtn.grid(row=1, column=0, columnspan=3, padx=10, pady=20)

root.mainloop()
