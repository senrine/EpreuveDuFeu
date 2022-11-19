import sys
from os.path import exists

def checkArgs():
	if not (len(sys.argv) == 2 and exists(sys.argv[1])):
		print('error')
		exit()

def getPlate(file):
	plate = []
	for line in file:
		plate_line = []
		for elm in line:
			if elm != '\n':
				plate_line.append(elm)
		plate.append(plate_line)
	return plate

def getObstacle(plate):
	return plate[0][-2]

def getFull(plate):
	return plate[0][-1]

def checkPlate(plate):
	if isInt(plate[0][:-3]):
		if int(lines[0][:-3][0])==len(lines)-1:
			size = len(lines[-1])
			for index in range(1,len(lines)):
				if len(lines[index]) != size:
					print('error')
					exit()
		else:
			print('error')
			exit()
	else:
		print('error')
		exit()

def isInt(num):
	try:
		for elm in num:
			int(elm)
		return True
	except ValueError:
		return False


def searchForSquares(plate):
	length = 0
	squares = []

	for raw in range(1,len(plate)):
		for col in range(len(plate[raw])):
			length = min(obstacle_col(raw,col,plate),obstacle_raw(raw,col,plate))
			for l in range(length,0,-1):
				if isSquare(raw,col,l,plate):
					squares.append([l,raw,col])
	return squares

def isSquare(raw,col,length,plate):
	obstacle = getObstacle(plate)

	for index1 in range(raw+1, raw+length, 1):
		for index2 in range(col+1, col+length, 1):
			if plate[index1][index2] == obstacle:
				return False
	return True
			
def obstacle_raw(raw,col,plate):
	obstacle = getObstacle(plate)

	for index in range(col,len(plate[raw])):
		if plate[raw][index] == obstacle:
			return (index - col )
	return len(plate[raw]) - col 

def obstacle_col(raw,col,plate):
	obstacle = getObstacle(plate)

	for index in range(raw,len(plate)):
		if plate[index][col] == obstacle:
			return (index - raw )
	return len(plate) - raw 

def largest_square(plate):
	squares = searchForSquares(plate)
	max = 0
	largest = []
	for index in range(len(squares)):
		if squares[index][0]> max:
			max = squares[index][0]
			largest = squares[index]
	return largest

def print_plate(plate):
	square = largest_square(plate)
	raw = square[1]
	col = square[2]
	length = square[0]

	for index1 in range(len(plate)):
		for index2 in range(len(plate[index1])):
			if index1>=raw and index1<raw+length and index2>=col and index2<col+length:
				print('o',end='')
			else:
				print(plate[index1][index2],end='')
		print('\t')

checkArgs()
with open(sys.argv[1],'r') as f:
	lines = f.readlines()
lines = getPlate(lines)
checkPlate(lines)
print_plate(lines)