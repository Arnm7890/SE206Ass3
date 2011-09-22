#!/usr/bin/python

#SOFTENG 206 Assignment 3
#Andrew Luey and Arunim Talwar
#September 2011

class Word(object):

    def __init__(self, word, definition, example, level):
		
        self.word = word
        self.definition = definition
        self.example = example
        self.level = level
    
    def getWord(self):
        return self.word

    def getDef(self):
        return self.definition

    def getExample(self):
        return self.example

    def getLevel(self):
        return self.level

    def serialize(self):
        return "{word}|{definition}|{example}|{level}".format(**self.__dict__)

    @classmethod
    def unserialize(cls, entry):
        return cls(*entry.split("|"))


def parseFile(tldrfile):	
    for line in tldrfile:
        if line[0] == "#":
            continue
        yield Word.unserialize(line)   # The use of the 'yield' keyword, to return an interable, was advised by Tony Young.
