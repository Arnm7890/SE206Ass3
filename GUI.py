#!/usr/bin/python

# SOFTENG 206 Assignment 3
# Andrew Luey and Arunim Talwar
# Date: September 2011
# Description: Tk widget creation


from functools import partial
from Tkinter import *   # Tk, Frame, Button, Listbox, OptionMenu, Scrollbar, StringVar
from tkMessageBox import *
from tkFileDialog import *
from Speak import *
from Word import *
from Ass3 import *



class GUI:

    def __init__(self, master):
		
        self.newWordName = StringVar()
        self.newWordExampleName = StringVar()
        self.newWordDefName = StringVar()
        self.newWordLevelName = StringVar()

        self.data = []
        self.filename = StringVar()

        self.menubar = Menu(root)

        # Top Level 
        self.fileMenu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="File", menu=self.fileMenu)
        self.editMenu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Edit", menu=self.editMenu)
        self.helpMenu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Help", menu=self.helpMenu)


        # File Menu
        self.fileMenu.add_command(label="Manage lists", command=self.manageLists)
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label="Exit", command=self.exit)

        # Edit Menu
        self.editMenu.add_command(label="Add", command=self.newWord)
        self.editMenu.add_command(label="Remove", command=self.removeWordFn)


        # Help Menu

        self.helpMenu.add_command(label="About us", command=self.aboutUs)

        root.config(menu=self.menubar)


        # Word lists
        self.listNames = ["Child", "ESOL", "BEE"]
        self.childList = ("child1", "child2", "child3")      # This will hold the child list
        self.esolList = ("esol1", "esol2", "esol3")          # This will hold the ESOL list
        self.beeList = ("bee1", "bee1", "bee1")              # This will hold the BEE list

        # Listbox Frame
        self.listFrame = Frame(root)
        self.listFrame.grid(column=0, row=0, padx=10, pady=10)

        # Listbox
        columnNames = (('Word', 10), ('Difficulty', 8), ('Definition', 60), ('Example', 60))
        self.wordList = StringVar()
        self.createMultiListBox(self.listFrame, columnNames, 0, 1, self.wordList)

        # Listbox Frame
        self.optFrame = Frame(self.listFrame)
        self.optFrame.grid(column=0, row=0, columnspan=len(columnNames), sticky="ew")

        # Option menu
        self.currentListName = StringVar(master)
        self.currentListName.set("Please select a list")
        self.optMenu = self.createOptionMenu(self.optFrame, 0, 0, self.currentListName, self.listNames)
        self.createButton(self.optFrame, 1, 0, "Manage lists", self.manageLists, colour="light grey")

        def updateList(*args):
            if self.currentListName.get() == "Child":
                self.wordList.set(self.childList)
            elif self.currentListName.get() == "ESOL":
                self.wordList.set(self.esolList)
            elif self.currentListName.get() == "BEE":
                self.wordList.set(self.beeList)

        self.currentListName.trace("w", updateList)

        # Speech Frame
        self.speechFrame = Frame(self.listFrame, width=120)
        self.speechFrame.grid(column=0, row=3, columnspan=len(columnNames), padx=10, pady=10)

        # Speech buttons
        self.createButton(self.speechFrame, 0, 0, "Play", self.speakSelected, colour="green")            ### This method (speakSelected) shows an error when clicked, saying that
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
        optMenu.grid(column=x, row=y, sticky="ew")
        return optMenu

    def createListBox(self, parent, x, y, val):

        """ Listbox to show the spelling list """
        self.lstbox = Listbox(parent, listvariable=val, selectmode="extended", height=20)
        self.lstbox.grid(column=x, row=y)
        sbar = Scrollbar(parent, orient="vertical", command=self.lstbox.yview)
        sbar.grid(column=x+1, row=y, sticky="ns")
        self.lstbox['yscrollcommand'] = sbar.set
        return self.lstbox
        	
    def createMultiListBox(self, parent, columnNames, x, y, val):
        """ Listbox to show the spelling list """

        self.columns = []

        for l,w in columnNames:
        
	        # Column headings
	        Label(parent, text=l, borderwidth=1, relief=RAISED).grid(column=x+columnNames.index((l,w)), row=y, sticky="ew")
	        
	        # Column listboxes
	        lstbox = Listbox(parent, width=w, listvariable=val,
	                         selectmode="extended", height=20, borderwidth=0,
	                         selectborderwidth=0, relief=FLAT, exportselection=FALSE)
	        lstbox.grid(column=x+columnNames.index((l,w)), row=y+1)
	        self.columns.append(lstbox)

        Label(parent, borderwidth=1, relief=RAISED).grid(column=0, row=0)
        sbar = Scrollbar(parent, orient="vertical", command=self.scroll)
        sbar.grid(column=len(columnNames)+1, row=y+1, sticky="ns")
        self.columns[0]['yscrollcommand'] = sbar.set
            

#        sbar = Scrollbar(parent, orient="vertical", command=self.lstbox.yview)
#        sbar.grid(column=x+1, row=y, sticky="ns")
#        self.columns['yscrollcommand'] = sbar.set


    def scroll(self, *args):
	    for l in self.columns:
	        apply(l.yview, args)

    def aboutUs(self):
        """ Displays About Us dialog box """
        showinfo('About Us', 'Made by Arunim Talwar and Andrew Luey')
		

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
        word_name = self.newWordName.get()
        word_example = self.newWordExampleName.get()
        word_def = self.newWordDefName.get()
        word_level = self.newWordLevelName.get()

        new_word = Word(word_name, word_example, word_def, word_level)
        self.lstbox.insert(END, word_name)
	

    def removeWordFn(self):
        if askyesno('Warning!', 'Are you sure you wish to delete the selected words?', icon="warning"):
            while True:
                selection = self.lstbox.curselection()
                if not selection: break
                self.lstbox.delete(selection[0])


    # Exit window    
    def exit(self):
        """ Confirms program quit """
        global root
        if askyesno('Exit', 'Do you wish to exit the teacher interface?', icon="warning"):
            root.destroy()


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
		
        self.createButton(addListFrame, 2, 0, "Add", addListWindow.destroy, "grey")
        self.createButton(addListFrame, 3, 0, "Back", addListWindow.destroy, "grey")

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
        
        if askyesno('Warning!', 'Are you sure you wish to delete this spelling list?', icon="warning"):
            print "temporary test message: list removed"
            

    # Add/remove list window

    def manageLists(self):

        newListWindow = Toplevel(root) 

        # Listbox Frame
        manageListFrame = Frame(newListWindow)
        manageListFrame.grid(column=0, row=0, padx=10, pady=20)

        # Listbox
        listNamesVar = StringVar(value=tuple(self.listNames))
        self.createListBox(manageListFrame, 0, 0, listNamesVar)
		
        manageListBtnFrame = Frame(newListWindow)
        manageListBtnFrame.grid(column=0, row=1, columnspan=2, padx=10, pady=10)
		
        self.createButton(manageListBtnFrame, 2, 0, "Add", self.addListFn, "grey")
        self.createButton(manageListBtnFrame, 3, 0, "Remove", self.removeListFn, "grey")
        self.createButton(manageListBtnFrame, 4, 0, "Back", newListWindow.destroy, "grey")
        
        self.manageListMenubar = Menu(newListWindow)

        # Top Level 
        
        self.listFileMenu = Menu(self.menubar, tearoff=0)
        self.manageListMenubar.add_cascade(label="File", menu=self.listFileMenu)
        
        self.listEditMenu = Menu(self.menubar, tearoff=0)
        self.manageListMenubar.add_cascade(label="Edit", menu=self.listEditMenu)

        self.listFileMenu.add_command(label="Import", command=self.importList)
        self.listFileMenu.add_command(label="Export", command=self.exportList)
        self.listFileMenu.add_separator()
        self.listFileMenu.add_command(label="Close", command=newListWindow.destroy)

        self.listEditMenu.add_command(label="Add", command=self.addListFn)
        self.listEditMenu.add_command(label="Remove", command=self.removeListFn)
        self.listEditMenu.add_command(label="Merge", command=self.mergeLists)

        newListWindow.config(menu=self.manageListMenubar)

    # Import/Export as tldr file functions

    def importList(self):

	    tldr_files = askopenfilenames(filetypes = [("Word List", ".tldr")])
	    for tldr_file in tldr_files:
            #self.addToOptMenu(tldr_file)
	        try:
	            with open(tldr_file, "r") as c:
	                data = list(parseFile(c))
	        except IOError as e:
	            tkMessageBox.showwarning("Import Error", "Could not import file!")
	        except Exception as e:
	            tkMessageBox.showwarning("Parse error", "Could not parse file!")

        
    def exportList(self):

        ######################### ADD FUNCTION ###################################
        # This function takes a spelling list and exports it as a tldr file. It will
        # therefore have to let you browse to let you choose where to save the file.
        
        print "temporary test message: list exported"  


    # Functions to remove lists

    def mergeLists(self):

        ######################### ADD FUNCTION ###################################
        # I have no idea how we want to do this. The basic idea is this should let
        # you copy words from other lists.

        print "temporary test message: list merged"
        
        
    # Speak button functions

    def speakSelected(self):

        ######################### ADD FUNCTION ###################################
        # This function must take the selected words from the listbox (variable name
        # = wordList) and speak those words

        print "temporary test message: selected words spoken"
		

# Initialise GUI
root = Tk()
root.title("Teacher Interface")
gui = GUI(root)
root.mainloop()
