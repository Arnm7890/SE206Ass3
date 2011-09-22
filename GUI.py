#!/usr/bin/python

# SOFTENG 206 Assignment 3
# Andrew Luey and Arunim Talwar
# Date: September 2011
# Description: Tk widget creation


from functools import partial
from Tkinter import *   # Tk, Frame, Button, Listbox, OptionMenu, Scrollbar, StringVar
from tkMessageBox import *
from tkFileDialog import *
import Speak
from Word import *




class GUI:

    def __init__(self, master):
    
        self.root = master    
        
        self.speakObj = Speak.Festival()     # Festival functionality
        self.CreateBaseMenus()          # Create menus
        
        self.newListBool = False
        self.newFileBool = False

        self.addListName = StringVar()
        self.entryListName = StringVar()

        self.data = []
        self.fileName = StringVar()
                
        self.newWordName = StringVar()
        self.newWordExampleName = StringVar()
        self.newWordDefName = StringVar()
        self.newWordLevelName = StringVar()
        


        # Word lists
        self.listNames = ["Child", "ESOL", "BEE"]
        
        self.childWords = ["word[0]", "word[1]", "word[2]", "word[3]", "word[4]", "word[5]", "word[6]", "word[7]", "word[8]", "word[9]", "word[10]", "word[11]", "word[12]", "word[13]", "word[14]", "word[15]", "word[16]", "word[17]", "word[18]", "word[19]", "word[20]", "word[21]", "word[22]", "word[23]", "word[24]", "word[25]", "word[26]", "word[27]", "word[28]", "word[29]"]
        self.childDif = ["dif[0]", "dif[1]", "dif[2]", "dif[3]", "dif[4]", "dif[5]", "dif[6]", "dif[7]", "dif[8]", "dif[9]", "dif[10]", "dif[11]", "dif[12]", "dif[13]", "dif[14]", "dif[15]", "dif[16]", "dif[17]", "dif[18]", "dif[19]", "dif[20]", "dif[21]", "dif[22]", "dif[23]", "dif[24]", "dif[25]", "dif[26]", "dif[27]", "dif[28]", "dif[29]"]
        self.childDef = ["def[0]", "def[1]", "def[2]", "def[3]", "def[4]", "def[5]", "def[6]", "def[7]", "def[8]", "def[9]", "def[10]", "def[11]", "def[12]", "def[13]", "def[14]", "def[15]", "def[16]", "def[17]", "def[18]", "def[19]", "def[20]", "def[21]", "def[22]", "def[23]", "def[24]", "def[25]", "def[26]", "def[27]", "def[28]", "def[29]"]
        self.childExp = ["exp[0]", "exp[1]", "exp[2]", "exp[3]", "exp[4]", "exp[5]", "exp[6]", "exp[7]", "exp[8]", "exp[9]", "exp[10]", "exp[11]", "exp[12]", "exp[13]", "exp[14]", "exp[15]", "exp[16]", "exp[17]", "exp[18]", "exp[19]", "exp[20]", "exp[21]", "exp[22]", "exp[23]", "exp[24]", "exp[25]", "exp[26]", "exp[27]", "exp[28]", "exp[29]"]
        
        
        self.esolWords = ["esol word"]
        self.esolDif = ["esol dif"]
        self.esolDef = ["esol def"]
        self.esolExp = ["esol exp"]
        
        self.beeWords = ["bee word"]
        self.beeDif = ["bee dif"]
        self.beeDef = ["bee def"]
        self.beeExp = ["bee exp"]

        self.fileWords = []
        self.fileDif = []
        self.fileDef = []
        self.fileExp = []

        self.addWords = []
        self.addDif = []
        self.addDef = []
        self.addExp = []

        self.words = []
        self.dif = []
        self.defn = []
        self.exp = []
        
        self.setup()
        
    def CreateBaseMenus(self):

        self.menubar = Menu(self.root)

        # Top Level 
        fileMenu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="File", menu=fileMenu)
        editMenu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Edit", menu=editMenu)
        helpMenu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Help", menu=helpMenu)

        # File Menu
        fileMenu.add_command(label="Manage lists", command=self.manageLists)
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", command=self.exit)

        # Edit Menu
        editMenu.add_command(label="Add", command=self.newWord)
        editMenu.add_command(label="Remove", command=self.removeWordFn)

        # Help Menu
        helpMenu.add_command(label="About us", command=self.aboutUs)

        self.root.config(menu=self.menubar)
        

    def setup(self):

        # Listbox Frame
        self.listFrame = Frame(self.root)
        self.listFrame.grid(column=0, row=0, padx=10, pady=10)

        # Listbox
        columnNames = (('Word', 10), ('Difficulty', 8), ('Definition', 60), ('Example', 60))
#        self.wordList = StringVar()
        self.createMultiListBox(self.listFrame, columnNames, 0, 1, self.words, self.dif, self.defn, self.exp)


        # Listbox Frame
        self.optFrame = Frame(self.listFrame)
        self.optFrame.grid(column=0, row=0, columnspan=len(columnNames), sticky="ew")

        # Option menu
        self.currentListName = StringVar()
        self.currentListName.set("Please select a list")
        self.optMenu = self.createOptionMenu(self.optFrame, 0, 0, self.currentListName, self.listNames)
        self.createButton(self.optFrame, 1, 0, "Manage lists", self.manageLists, colour="light grey")

        # Speech Frame
        self.speechFrame = Frame(self.listFrame, width=120)
        self.speechFrame.grid(column=0, row=3, columnspan=len(columnNames), padx=10, pady=10)

        # Speech buttons
        self.createButton(self.speechFrame, 0, 0, "Play", self.ss, colour="green")            ### This method (speakSelected) shows an error when clicked, saying that
                                                                                                    ### it requires one argument, none given, even when item is selected. Have to
                                                                                                    ### have some way to actually use whats selected in the list box
        self.createButton(self.speechFrame, 1, 0, "Stop", self.speakObj.restartFest, colour="pink")


    def ss(self):
#        partial(, self.listOfColumns[0].curselection())
        for index in self.listOfColumns[0].curselection():
            self.speakObj.speakSelected(self.listOfColumns[0].get(index))


    def updateList(self, *args):
        if self.currentListName.get() == "Child":
            self.words = self.childWords
            self.dif = self.childDif
            self.defn = self.childDef
            self.exp = self.childExp

        elif self.currentListName.get() == "BEE":
            self.words = self.beeWords
            self.dif = self.beeDif
            self.defn = self.beeDef
            self.exp = self.beeExp
        elif self.currentListName.get() == "ESOL":
            self.words = self.esolWords
            self.dif = self.esolDif
            self.defn = self.esolDef
            self.exp = self.esolExp
        elif self.newListBool:
            if self.currentListName.get() == self.addListName.get():
                self.words = self.addWords
                self.dif = self.addDif
                self.defn = self.addDef
                self.exp = self.addExp
        elif self.newFileBool:
            if self.currentListName.get() == self.fucking_file_name[self.fucking_index]:
                self.words = self.fileWords
                self.dif = self.fileDif
                self.defn = self.fileDef
                self.exp = self.fileExp
        self.listFrame.destroy()
        self.setup()
           
    def createButton(self, parent, x, y, txt, fn, colour):
        
        """ Button which runs the function fn when pressed """
        btn = Button(parent, text=txt, command=fn, bg=colour, width=6)
        btn.grid(column=x, row=y)
        return btn


    def createOptionMenu(self, parent, x, y, val, var):

        """ Option menu to show the spelling list """
        optMenu = OptionMenu(parent, val, *var)
        optMenu.grid(column=x, row=y, sticky="ew")
        val.trace("w", self.updateList)
        return optMenu

    def addMenuOptions():
        """ Add Menu options dynamically """

        global optionMenuWidget

        optionMenuWidget["menu"].delete(0, END)
        # Add options from 1 to 5
        for i in range(1, 6):
            optionMenuWidget["menu"].add_command(label=i, command=lambda temp = i: optionMenuWidget.setvar(optionMenuWidget.cget("textvariable"), value = temp))

    def createListBox(self, parent, x, y, val):

        """ Listbox to show the spelling list """
        self.lstbox = Listbox(parent, listvariable=val, selectmode="extended", height=20)
        self.lstbox.grid(column=x, row=y)
        sbar = Scrollbar(parent, orient="vertical", command=self.lstbox.yview)
        sbar.grid(column=x+1, row=y, sticky="ns")
        self.lstbox['yscrollcommand'] = sbar.set
        return self.lstbox
            
            
            
            
    def createMultiListBox(self, parent, columnNames, x, y, *sList):
        listOfLists = []
        
        for sl in sList:
            listOfLists.append(sl)

        if len(columnNames) == len(listOfLists):
            pass
        else:
            print "help!"
            return
        
        Label(parent, borderwidth=1, relief=RAISED).grid(column=len(columnNames)+1, row=y, sticky="ew")
        sbar = Scrollbar(parent, orient="vertical", command=self.onVsb)
        sbar.grid(column=len(columnNames)+1, row=y+1, sticky="ns")

        self.listOfColumns = []
        self.columnsSelected = []
        self.selectedItems = []
        
        self.listSelected = []

        for l,w in columnNames:
        
            # Column headings
            Label(parent, text=l, borderwidth=1, relief=RAISED)\
                .grid(column=x+columnNames.index((l,w)), row=y, sticky="ew")
            
            self.var=StringVar()
            
            # Column listboxes
            lstbox = Listbox(parent, width=w,
                             selectmode=EXTENDED, height=20, borderwidth=0,
                             selectborderwidth=0, relief=FLAT, exportselection=FALSE,
                             yscrollcommand=sbar.set, listvariable=self.var)
            lstbox.grid(column=x+columnNames.index((l,w)), row=y+1)
            self.columnsSelected.append(self.var)
            lstbox.bind("<MouseWheel>", self.onScroll)
            lstbox.bind("<Button-4>", self.onScroll)
            lstbox.bind("<Button-5>", self.onScroll)
            lstbox.bind("<Button-1>", lambda e, s=self: s._select1(e.y))
            lstbox.bind("<Control-Button-1>", lambda e, s=self: s._select2(e.y))            
            for element in listOfLists[columnNames.index((l,w))]:
                s = str(element)
                lstbox.insert("end", s)
            self.listOfColumns.append(lstbox)



    def _select1(self, y):
        row = self.listOfColumns[0].nearest(y)
        self.selection_clear(0, END)
        self.selection_set(row)
        return 'break'

    def _select2(self, y):
        row = self.listOfColumns[0].nearest(y)
        self.selection_set(row)
        return 'break'
                    
    def selection_set(self, first, last=None):
        for l in self.listOfColumns:
            l.selection_set(first, last)
            self.selectedItems.append(l)
            
    def selection_clear(self, first, last=None):
        for l in self.listOfColumns:
            l.selection_clear(first, last)

    def onScroll(self, event):
        """
        Convert mousewheel motion to scrollbar motion.
        """
        if (event.num == 4):    # Linux encodes wheel as 'buttons' 4 and 5
            delta = -1
        elif (event.num == 5):
            delta = 1
        else:                   # Windows & OSX
            delta = event.delta
        for lb in self.listOfColumns:
            lb.yview("scroll", delta, "units")
        # Return 'break' to prevent the default bindings from
        # firing, which would end up scrolling the widget twice.
        return "break"

    def onVsb(self, *args):
        """ scroll bar moves all listboxes """
        for lb in self.listOfColumns:
            lb.yview(*args)



    def scroll(self, *args):
        for l in self.columns:
            apply(l.yview, args)

    def aboutUs(self):
        """ Displays About Us dialog box """
        showinfo('About Us', 'Made by Arunim Talwar and Andrew Luey')

    # New word window

    def newWord(self):

        newWordWindow = Toplevel(self.root)
        
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
        if askyesno('Exit', 'Do you wish to exit the teacher interface?', icon="warning"):
            self.root.destroy()


    # New list window    
        
    def addListFn(self):

        self.addListWindow = Toplevel(self.root)
        
        addListFrame = Frame(self.addListWindow)
        addListFrame.grid(column=0, row=0, padx=10, pady=20)
        
        addListLabel = Label(addListFrame, text='New list name:')
        addListLabel.grid(column=0, row=0)

        self.addListName = StringVar()
        addListEntry = Entry(addListFrame, textvariable=self.addListName)
        addListEntry.grid(column=1, row=0)
        
        self.createButton(addListFrame, 2, 0, "Add", self.newListFn, "grey")
        self.createButton(addListFrame, 3, 0, "Back", self.addListWindow.destroy, "grey")

    def newListFn(self):
        self.listNames.append(self.addListName.get())
        self.w.insert(END, self.addListName.get())
        self.addListWindow.destroy()
        self.optMenu.destroy()
        self.optMenu = self.createOptionMenu(self.optFrame, 0, 0, self.currentListName, self.listNames)
        self.newListBool = True      

    def removeListFn(self):        
        if askyesno('Warning!', 'Are you sure you wish to delete this spelling list?', icon="warning"):
            while True:
                selection = self.w.curselection()
                if not selection: break
                x = int(selection[0])
                self.w.delete(x)
                del self.listNames[x]
                self.optMenu.destroy()
                self.optMenu = self.createOptionMenu(self.optFrame, 0, 0, self.currentListName, self.listNames)
            

    # Add/remove list window

    def manageLists(self):

        self.newListWindow = Toplevel(self.root) 

        # Listbox Frame
        manageListFrame = Frame(self.newListWindow)
        manageListFrame.grid(column=0, row=0, padx=10, pady=20)

        # Listbox
        self.listNamesVar = StringVar(value=tuple(self.listNames))
        self.w = self.createListBox(manageListFrame, 0, 0, self.listNamesVar)
        
        manageListBtnFrame = Frame(self.newListWindow)
        manageListBtnFrame.grid(column=0, row=1, columnspan=2, padx=10, pady=10)
        
        self.createButton(manageListBtnFrame, 2, 0, "Add", self.addListFn, "grey")
        self.createButton(manageListBtnFrame, 3, 0, "Remove", self.removeListFn, "grey")
        self.createButton(manageListBtnFrame, 4, 0, "Back", self.newListWindow.destroy, "grey")
        
        self.manageListMenubar = Menu(self.newListWindow)

        # Top Level 
        
        self.listFileMenu = Menu(self.menubar, tearoff=0)
        self.manageListMenubar.add_cascade(label="File", menu=self.listFileMenu)
        
        self.listEditMenu = Menu(self.menubar, tearoff=0)
        self.manageListMenubar.add_cascade(label="Edit", menu=self.listEditMenu)

        self.listFileMenu.add_command(label="Import", command=self.importList)
        self.listFileMenu.add_command(label="Export", command=self.exportList)
        self.listFileMenu.add_separator()
        self.listFileMenu.add_command(label="Close", command=self.newListWindow.destroy)

        self.listEditMenu.add_command(label="Add", command=self.addListFn)
        self.listEditMenu.add_command(label="Remove", command=self.removeListFn)
        self.listEditMenu.add_command(label="Merge", command=self.mergeLists)

        self.newListWindow.config(menu=self.manageListMenubar)

    # Import/Export as tldr file functions

    def importList(self):

        tldr_files = askopenfilenames(filetypes = [("Word List", ".tldr")])
        for tldr_file in tldr_files:
            try:
                with open(tldr_file, "r") as c:
                    self.data = list(parseFile(c))
                    self.fucking_file_name = tldr_file.split("/")
                    self.fucking_index = len(self.fucking_file_name) - 1
                    self.listNames.append(self.fucking_file_name[self.fucking_index])
                    self.optMenu.destroy()
                    self.optMenu = self.createOptionMenu(self.optFrame, 0, 0, self.currentListName, self.listNames)
                    self.w.insert(END, self.fucking_file_name[self.fucking_index])
                    for i in range(len(self.data)):
                        self.addImportedFile(self.data[i])
                    self.updateList()
                    self.newFileBool = True

            except IOError as e:
                showwarning("Import Error", "Could not import file!")
           # except Exception as e:
            #    showwarning("Parse error", "Could not parse file!")


    def addImportedFile(self, importedFile):

        self.fileWords.append(importedFile.getWord())
        self.fileDif.append(importedFile.getLevel())
        self.fileDef.append(importedFile.getDef())
        self.fileExp.append(importedFile.getExample())


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
