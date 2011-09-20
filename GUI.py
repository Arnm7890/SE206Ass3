#!/usr/bin/python

# SOFTENG 206 Assignment 3
# Andrew Luey and Arunim Talwar
# Date: September 2011


from functools import partial
from Tkinter import *           # Tk, Frame, Button, Listbox, OptionMenu, Scrollbar, StringVar
from Speak import *
from Word import *

    
# Widget creation class


################# MODIFICATION #######################
# Made GUI a class

class GUI:

    def __init__(self, master):
		
        self.newWordName = StringVar()
        self.newWordExampleName = StringVar()
        self.newWordDefName = StringVar()
        self.newWordLevelName = StringVar()

        self.menubar = Menu(root)

        # Top Level 
        self.fileMenu = Menu(self.menubar, tearoff=0)
        self.editMenu = Menu(self.menubar, tearoff=0)
        self.helpMenu = Menu(self.menubar, tearoff=0)

        self.menubar.add_cascade(label="File", menu=self.fileMenu)
        self.menubar.add_cascade(label="Edit", menu=self.editMenu)
        self.menubar.add_cascade(label="Help", menu=self.helpMenu)

        # File Menu

        self.fileMenu.add_command(label="Import list", command=self.importList)
        self.fileMenu.add_command(label="Export list", command=self.exportList)
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label="Exit", command=self.exit)

        # Edit Menu

        self.editMenu.add_command(label="Add/remove lists", command=self.manageLists)
        self.editMenu.add_command(label="Add word", command=self.newWord)
        self.editMenu.add_command(label="Remove selected word/s", command=self.removeWordFn)
        self.editMenu.add_command(label="Merge lists", command=self.mergeLists)

        # Help Menu

        self.helpMenu.add_command(label="About us", command=self.aboutUs)

        root.config(menu=self.menubar)


        # Word lists
        self.listNames = ["Child", "ESOL", "BEE"]
        self.childList = ("child1", "child2", "child3")      # This will hold the child list
        self.esolList = ("esol1", "esol2", "esol3")          # This will hold the ESOL list
        self.beeList = ("bee1", "bee1", "bee1")              # This will hold the BEE list

        # Listbox Frame
        self.listFrame = Frame(root, width=120)
        self.listFrame.grid(column=0, row=0, padx=10, pady=10)

        # Listbox
        self.wordList = StringVar()
        self.createListBox(self.listFrame, 0, 1, self.wordList)

        # Option menu
        self.currentListName = StringVar(value="Please select a list")
        self.optMenu = self.createOptionMenu(self.listFrame, 0, 0, self.currentListName, self.listNames)


        ############### ADD FUNCTIONALITY #############
        # Need to be changed to handle when new lists are added / removed

        def updateList(self, *args):
            if self.currentListName.get() == "Child":
                self.wordList.set(self.childList)
            elif self.currentListName.get() == "ESOL":
                self.wordList.set(self.esolList)
            elif currentListName.get() == "BEE":
                self.wordList.set(self.beeList)

        self.currentListName.trace("w", updateList)

        # Speech Frame
        self.speechFrame = Frame(self.listFrame, width=120)
        self.speechFrame.grid(column=0, row=2, columnspan=2, padx=10, pady=10)

        # Speech buttons
        self.createButton(self.speechFrame, 0, 0, "Test", self.speakSelected, colour="green")            ### This method (speakSelected) shows an error when clicked, saying that
                                                                                                    ### it requires one argument, none given, even when item is selected. Have to
                                                                                                    ### have some way to actually use whats selected in the list box
        self.createButton(self.speechFrame, 1, 0, "Stop", restartFest, colour="red")
    

    def createButton(self, parent, x, y, txt, fn, colour):
		
        """ Button which runs the function fn when pressed """
        btn = Button(parent, text=txt, command=fn, bg=colour, width=6)
        btn.grid(column=x, row=y)
        return btn


    def createOptionMenu(self, parent, x, y, val, var):

        """ Option menu to show the spelling list """
        optMenu = OptionMenu(parent, val, *var)
        optMenu.grid(column=x, row=y, columnspan=2, sticky="ew")
        return optMenu

		
    def createListBox(self, parent, x, y, val):

        """ Listbox to show the spelling list """
        self.lstbox = Listbox(parent, listvariable=val, selectmode="extended", height=20)
        self.lstbox.grid(column=x, row=y)
        sbar = Scrollbar(parent, orient="vertical", command=self.lstbox.yview)
        sbar.grid(column=x+1, row=y, sticky="ns")
        self.lstbox['yscrollcommand'] = sbar.set
        return self.lstbox


    # About Us window

    def aboutUs(self):

        auWindow = Toplevel(root)

        auFrame = Frame(auWindow)
        auFrame.grid(column=0, row=0, padx=10, pady=12)
		
        auLabel = Label(auFrame, text='Made by Arunim Talwar and Andrew Luey')
        auLabel.grid(column=0, row=0)
		
        auBtnFrame = Frame(auFrame)
        auBtnFrame.grid(column=0, row=1, pady=10)
		
        createButton(auBtnFrame, 0, 1, "Back", auWindow.destroy, "grey")
		

    # New word window

    def newWord(self):

        newWordWindow = Toplevel(root)
		
        newWordFrame = Frame(newWordWindow)
        newWordFrame.grid(column=0, row=0, padx=10, pady=20)
		
        newWordLabel = Label(newWordFrame, text='Word:')
        newWordLabel.grid(column=0, row=0)
        newWordEntry = Entry(newWordFrame, textvariable=self.newWordName)
        newWordEntry.grid(column=1, row=0)
		
        newWordExampleLabel = Label(newWordFrame, text='Example:')
        newWordExampleLabel.grid(column=0, row=1)
        newWordExampleEntry = Entry(newWordFrame, textvariable=self.newWordExampleName)
        newWordExampleEntry.grid(column=1, row=1)
		
        newWordDefLabel = Label(newWordFrame, text='Definition:')
        newWordDefLabel.grid(column=0, row=2)
        newWordDefEntry = Entry(newWordFrame, textvariable=self.newWordDefName)
        newWordDefEntry.grid(column=1, row=2)

        newWordLevelLabel = Label(newWordFrame, text='Level:')
        newWordLevelLabel.grid(column=0, row=3)
        newWordLevelEntry = Entry(newWordFrame, textvariable=self.newWordLevelName)
        newWordLevelEntry.grid(column=1, row=3)
		
        newWordBtnFrame = Frame(newWordFrame)
        newWordBtnFrame.grid(column=0, row=4, columnspan=2, pady=10, sticky="e")
		
        self.createButton(newWordBtnFrame, 0, 0, "Add", self.newWordFn, "grey")
        self.createButton(newWordBtnFrame, 1, 0, "Back", newWordWindow.destroy, "grey")
		
    def newWordFn(self):

    ######################### MODIFIED FUNCTION ###################################
    # Using the WordName, WordExampleName, WordDefName, and WordLevelName String variables, 
    # created a Word object with those as arguments, then appended this word to the list.
        word_name = self.newWordName.get
        word_example = self.newWordExampleName.get
        word_def = self.newWordDefName.get
        word_level = self.newWordLevelName.get

        new_word = Word(word_name, word_example, word_def, word_level)
        self.lstbox.insert(END, new_word)
	

    def removeWordFn(self):

    ######################### ADD FUNCTION ###################################
    # Take the selected words in the list and remove them from the spelling
    # list
		
        print "temporary test message: word removed"
        pass
		

    # Exit window

    def exit(self):

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
		
    def addListFn(self):

        addListWindow = Toplevel(root)
		
        addListFrame = Frame(addListWindow)
        addListFrame.grid(column=0, row=0, padx=10, pady=20)
		
        addListLabel = Label(addListFrame, text='New list name:')
        addListLabel.grid(column=0, row=0)
        addListName = StringVar()
        addListEntry = Entry(addListFrame, textvariable=addListName)
        addListEntry.grid(column=1, row=0)
		
        createButton(addListFrame, 2, 0, "Add", newListFn, "grey")
        createButton(addListFrame, 3, 0, "Back", addListWindow.destroy, "grey")

    def newListFn(self):

        ######################### ADD FUNCTION ###################################
        # Takes the value of the addListName variable and makes a list of that name
        # updating the listbox of names and the option menu from which you can
        # select lists. Also at the end of this it should close the window.
        
        print "temporary test message: list created"
        pass


    def removeListFn(self):

        ######################### ADD FUNCTION ###################################
        # Takes the list/s selected and deletes it
        
        print "temporary test message: list removed"
        pass

    # Add/remove list window

    def manageLists(self):

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
        createButton(manageListBtnFrame, 3, 0, "Remove", removeListFn, "grey")
        createButton(manageListBtnFrame, 4, 0, "Back", newListWindow.destroy, "grey")


    # Import/Export as tldr file functions

    def importList(self):

        ######################### ADD FUNCTION ###################################
        # This function let you browse to find a file then it will take the values
        # in this file and have it as a spelling list in the program. IDK how we
        # want this to work but the general idea is that.

        print "temporary test message: list imported"
        pass
        
    def exportList(self):

        ######################### ADD FUNCTION ###################################
        # This function takes a spelling list and exports it as a tldr file. It will
        # therefore have to let you browse to let you choose where to save the file.
        
        print "temporary test message: list exported"
        pass    


    # Functions to remove lists

    def mergeLists(self):

        ######################### ADD FUNCTION ###################################
        # I have no idea how we want to do this. The basic idea is this should let
        # you copy words from other lists.

        print "temporary test message: list merged"
        pass
        
        
    # Speak button functions

    def speakSelected(self):

        ######################### ADD FUNCTION ###################################
        # This function must take the selected words from the listbox (variable name
        # = wordList) and speak those words

        print "temporary test message: selected words spoken"
        pass
		

# Initialise GUI
root = Tk()
root.title("Teacher Interface")
gui = GUI(root)
root.mainloop()
