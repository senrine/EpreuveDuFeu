import sys
from os.path import exists

def checkArgs():
	if len(sys.argv)==2:
		if not exists(sys.argv[1]):
			print("error")
			exit()
	else:
		print("error")
		exit()

def getMatrix(lines):
	matrix = []
	for line in lines:
		arrayLine = []
		for elm in line:
			if elm != '\n':
				arrayLine.append(elm)
		matrix.append(arrayLine)
	return matrix

def solve(matrix):
	find = find_empty(matrix)

	if not find:
		return True
	else:
		raw,col = find

	for nbr in range(1,10):
		if valid(matrix,str(nbr),raw,col):
			matrix[raw][col]=str(nbr)

			if solve(matrix):
				return True

			matrix[raw][col]='.'

	return False

def valid(matrix,nbr,raw,col):

	for i in range(len(matrix)):
		if i!=raw and matrix[i][col]==nbr:
			return False

	for i in range(len(matrix[raw])):
		if i!= col and matrix[raw][i]==nbr:
			return False

	col_box = col//3
	raw_box = raw//3

	for i in range(raw_box*3,raw_box*3+3):
		for j in range(col_box*3,col_box*3+3):
			if matrix[i][j] == nbr and i!=raw and j!=col:
				return False

	return True

def find_empty(matrix):
	for raw in range(len(matrix)):
		for col in range(len(matrix[raw])):
			if matrix[raw][col]=='.':
				return raw,col

def printMatrix(matrix):

	for raw in range(len(matrix)):
		content=''
		for col in range(len(matrix[raw])):
			content= content+matrix[raw][col]
		content= content+'\t'
		print(content)

checkArgs()
with open(sys.argv[1],'r') as f:
	lines = f.readlines()
matrix = getMatrix(lines)
if solve(matrix):
	printMatrix(matrix)
