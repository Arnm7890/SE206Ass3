#!/usr/bin/python

# SOFTENG 206 Assignment 3
# Andrew Luey and Arunim Talwar
# Date: September 2011


from functools import partial
from Tkinter import *           # Tk, Frame, Button, Listbox, OptionMenu, Scrollbar, StringVar
from Speak import *

    
# Widget creation functions
    
def createButton(parent, x, y, txt, fn, colour):
    """ Button which runs the function fn when pressed """
    btn = Button(parent, text=txt, command=fn, bg=colour, width=6)
    btn.grid(column=x, row=y)
    return btn

def createOptionMenu(parent, x, y, val, var):
    """ Option menu to show the spelling list """
    optMenu = OptionMenu(parent, val, *var)
    optMenu.grid(column=x, row=y, columnspan=2, sticky="ew")
    return optMenu
    
def createListBox(parent, x, y, val):
    """ Listbox to show the spelling list """
    lstbox = Listbox(parent, listvariable=val, selectmode="extended", height=20)
    lstbox.grid(column=x, row=y)
    sbar = Scrollbar(parent, orient="vertical", command=lstbox.yview)
    sbar.grid(column=x+1, row=y, sticky="ns")
    lstbox['yscrollcommand'] = sbar.set
    return lstbox


# About Us window

def aboutUs():

    auWindow = Toplevel(root)
    
    auFrame = Frame(auWindow)
    auFrame.grid(column=0, row=0, padx=10, pady=12)
    
    auLabel = Label(auFrame, text='Made by Arunim Talwar and Andrew Luey')
    auLabel.grid(column=0, row=0)
    
    auBtnFrame = Frame(auFrame)
    auBtnFrame.grid(column=0, row=1, pady=10)
    
    createButton(auBtnFrame, 0, 1, "Back", auWindow.destroy, "grey")
    

# New word window

def newWord():

    newWordWindow = Toplevel(root)
    
    newWordFrame = Frame(newWordWindow)
    newWordFrame.grid(column=0, row=0, padx=10, pady=20)
    
    newWordLabel = Label(newWordFrame, text='Word:')
    newWordLabel.grid(column=0, row=0)
    newWordName = StringVar()
    newWordEntry = Entry(newWordFrame, textvariable=newWordName)
    newWordEntry.grid(column=1, row=0)
    
    newWordExampleLabel = Label(newWordFrame, text='Example:')
    newWordExampleLabel.grid(column=0, row=1)
    newWordExampleName = StringVar()
    newWordExampleEntry = Entry(newWordFrame, textvariable=newWordExampleName)
    newWordExampleEntry.grid(column=1, row=1)
    
    newWordDefLabel = Label(newWordFrame, text='Definition:')
    newWordDefLabel.grid(column=0, row=2)
    newWordDefName = StringVar()
    newWordDefEntry = Entry(newWordFrame, textvariable=newWordDefName)
    newWordDefEntry.grid(column=1, row=2)
    
    newWordBtnFrame = Frame(newWordFrame)
    newWordBtnFrame.grid(column=0, row=3, columnspan=2, pady=10, sticky="e")
    
    createButton(newWordBtnFrame, 0, 0, "Add", newWordFn, "grey")
    createButton(newWordBtnFrame, 1, 0, "Back", newWordWindow.destroy, "grey")
    
def newWordFn():

    ######################### ADD FUNCTION ###################################
    # Take the word in the newWordDefName variable (in the function above) and
    # add it to the spelling list
    
    pass

def removeWordFn():

    ######################### ADD FUNCTION ###################################
    # Take the selected words in the list and remove them from the spelling
    # list
    
    pass
    

# Exit window

def exit():

    exitWindow = Toplevel(root)
    
    exitFrame = Frame(exitWindow)
    exitFrame.grid(column=0, row=0, padx=10, pady=20)
    
    exitLabel = Label(exitFrame, text='Are you sure you wish to exit?')
    exitLabel.grid(column=0, row=0, columnspan=2)
    
    exitBtnFrame = Frame(exitFrame)
    exitBtnFrame.grid(column=0, row=1, pady=10)
    
    createButton(exitBtnFrame, 0, 0, "Yes", root.quit, "grey")
    createButton(exitBtnFrame, 1, 0, "No", exitWindow.destroy, "grey")
    

# New list window    
    
def addListFn():

    addListWindow = Toplevel(root)
    
    addListFrame = Frame(addListWindow)
    addListFrame.grid(column=0, row=0, padx=10, pady=20)
    
    addListLabel = Label(addListFrame, text='New list name:')
    addListLabel.grid(column=0, row=0)
    addListName = StringVar()
    addListEntry = Entry(addListFrame, textvariable=addListName)
    addListEntry.grid(column=1, row=0)
    
    createButton(addListFrame, 2, 0, "Add", addListFn, "grey")
    createButton(addListFrame, 3, 0, "Back", addListWindow.destroy, "grey")


# Add/remove list window

def manageLists():

    newListWindow = Toplevel(root)

    # Listbox Frame
    manageListFrame = Frame(newListWindow)
    manageListFrame.grid(column=0, row=0, padx=10, pady=20)

    # Listbox
    listNamesVar = StringVar()
    createListBox(manageListFrame, 0, 0, listNamesVar)
    
    manageListBtnFrame = Frame(newListWindow)
    manageListBtnFrame.grid(column=0, row=1, columnspan=2, padx=10, pady=10)
    
    createButton(manageListBtnFrame, 2, 0, "Add", addListFn, "grey")
    createButton(manageListBtnFrame, 3, 0, "Remove", removeWordFn, "grey")
    createButton(manageListBtnFrame, 4, 0, "Back", newListWindow.destroy, "grey")


def SpeakSelected():

    ######################### ADD FUNCTION ###################################
    # This function must take the selected words from the listbox (variable name
    # = wordList) and speak those words

    pass
    

# Initialise GUI
root = Tk()
root.title("Teacher Interface")


# Initialise Menu

menubar = Menu(root)

# Top Level 
fileMenu = Menu(menubar, tearoff=0)
editMenu = Menu(menubar, tearoff=0)
helpMenu = Menu(menubar, tearoff=0)

menubar.add_cascade(label="File", menu=fileMenu)
menubar.add_cascade(label="Edit", menu=editMenu)
menubar.add_cascade(label="Help", menu=helpMenu)

# File Menu

fileMenu.add_command(label="Import list")
fileMenu.add_command(label="Export list")
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=exit)

# Edit Menu

editMenu.add_command(label="Add/remove lists", command=manageLists)
editMenu.add_command(label="Add word", command=newWord)
editMenu.add_command(label="Remove selected word/s")
editMenu.add_command(label="Merge lists")

# Help Menu

helpMenu.add_command(label="About us", command=aboutUs)

root.config(menu=menubar)


# Word lists
listNames = ["Child", "ESOL", "BEE"]
childList = ("child1", "child2", "child3")      # This will hold the child list
esolList = ("esol1", "esol2", "esol3")          # This will hold the ESOL list
beeList = ("bee1", "bee1", "bee1")              # This will hold the BEE list

# Listbox Frame
listFrame = Frame(root, width=120)
listFrame.grid(column=0, row=0, padx=10, pady=10)

# Listbox
wordList = StringVar()
createListBox(listFrame, 0, 1, wordList)

# Option menu
currentListName = StringVar(value="Please select a list")
optMenu = createOptionMenu(listFrame, 0, 0, currentListName, listNames)

############### ADD FUNCTIONALITY #############
# Need to add event binding so that when the option menu is changed the listbox
# is updated to show that list

# Speech Frame
speechFrame = Frame(listFrame, width=120)
speechFrame.grid(column=0, row=2, columnspan=2, padx=10, pady=10)

# Speech buttons
createButton(speechFrame, 0, 0, "Test", SpeakSelected, colour="green")
createButton(speechFrame, 1, 0, "Stop", restartFest, colour="red")

root.mainloop()
