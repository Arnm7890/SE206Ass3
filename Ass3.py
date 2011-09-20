import SE206Ass3.Word

def parseFile(tldrfile):
	
	for line in tldrfile:
		if line[0] == "#": continue
		yield Word.deserialize(line)

		


