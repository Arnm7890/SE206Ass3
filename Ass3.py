from Word import *

def parseFile(tldrfile):
	
	for line in tldrfile:
		if line[0] == "#": continue
		yield Word.unserialize(line)

		


