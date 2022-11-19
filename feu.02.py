import sys
from os.path import exists as file_exists

def checkArgs():
	if len(sys.argv) == 3:
		if not (file_exists(sys.argv[1]) and file_exists(sys.argv[2])):
			print('error')
			exit()
	else:
		print("error")
		exit()

def getLines(file):
	with open(file,'r') as f:
		return f.readlines()

def indexOfline(lines):
	indexes = []
	for line in lines:
		nbr = 0
		for index in range(len(line)):
			if line[index] == ' ':
				nbr += 1
		if len(indexes) == 0:
			indexes.append(nbr)
		else:
			if nbr < indexes[0]:
				indexes.append(nbr - indexes[0])
			else:
				indexes.append(nbr)
	return indexes

def removeSpaces(lines):
	new_form = []
	for index in range(len(lines)):
		new_line = ''
		array = lines[index].split(' ')
		for elm in array:
			new_line += elm	
		if new_line[-1] == '\n':
			new_form.append(new_line[:-1])
		else:
			new_form.append(new_line)
	return new_form

def examine(form,lines):
	new_form = removeSpaces(form)
	found = False
	for line in range(len(lines) - len(new_form) +1):
		for col in range(len(lines[line]) - len(new_form[0])+1):
			if lines[line][col] == new_form[0][0]:
				if searchForForm(form,lines,col,line):
					found = True
					x = col
					y = line
					break
	if found:
		print("Trouvé !\nCoordonnées: %d,%d"%(x,y))
		fillWithHyphen(form,lines,x,y)
	else:
		print("Introuvable")

def searchForForm(form,lines,x,y):
	new_form = removeSpaces(form)
	foundLine = False
	line = 0
	index = 0
	while line < len(new_form):
		if line != 0:
			index = indexOfline(form)[line]
		if len(lines[y+line])>=len(form[line]):
			col = 0
			while col < len(new_form[line]):
				if lines[y+line][x+col+index] != new_form[line][col]:
					print(lines[y+line][x+col+index],new_form[line][col],x+col+index)
					return False
				col+=1
		else:
			return False
		line+=1
	return True

def fillWithHyphen(form,lines,x,y):
	index = 1
	lineOfForm = 0
	new_form = removeSpaces(form)
	for line in range(len(lines)):

		string = ''
		if line > y and lineOfForm<len(new_form)-1:
			lineOfForm+=1
			x+=indexOfline(form)[lineOfForm]

		for col in range(len(lines[line])):
			if line ==y+lineOfForm and col>=x and col< x+len(new_form[lineOfForm]):
				if lines[line][col] == '\n':
					string = string + '\t'
				else:
					string= string +lines[line][col]
			else:
				if lines[line][col] != '\n':
					string = string + '-'
				elif lines[line][col] == '\n':
					string = string + '\t'
		print(string)

checkArgs()
examine(getLines(sys.argv[2]),getLines(sys.argv[1]))
