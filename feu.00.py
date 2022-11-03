import sys

def checkArguments():
	return len(sys.argv)==3

def checkValueError():
	try:
		for nbr in sys.argv[1:]:
			int(nbr)
	except ValueError:
		print("error")
		exit()

def forms(col,line):
	for i in range(line):
		word = ''
		if i==0 or i==line-1:
			for j in range(col):
				if j==0 or j ==col-1:
					word += 'o'
				else:
					word += '-'
		else:
			for j in range(col):
				if j==0 or j==col-1:
					word+='|'
				else:
					word+=' '
		print(word)

if checkArguments():
	checkValueError()
	forms(int(sys.argv[1]),int(sys.argv[2]))
else:
	print("error")