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
		
        """		
        >>> Word("dog", "a member of the genus Canis", "the dog ate the bone", "easy").serialize()
        'dog|a member of the genus Canis|the dog ate the bone|easy'
        """

        return "{word}|{definition}|{example}|{level}".format(**self.__dict__)

    @classmethod
    def unserialize(cls, entry):

        """
        >>> w = Word.unserialize("dog|a member of the genus Canis|the dog ate the bone|easy")
        >>> w.word
        'dog'
        >>> w.definition
        'a member of the genus Canis'
        >>> w.example
        'the dog ate the bone'
        >>> w.level
        'easy'
        """

        return cls(*entry.split("|"))


if __name__ == "__main__":
    import doctest
    doctest.testmod()

