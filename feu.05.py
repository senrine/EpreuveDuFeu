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

def getMap(file):
	map = []

	for line in file:
		mapLine = []
		for elm in line:
			if elm != '\n':
				mapLine.append(elm)
		map.append(mapLine)
	setWidth(map)
	setChar(map)
	setHeight(map)
	return map

def isInt(num):
	try:
		int(num)
		return True
	except ValueError:
		return False

def setWidth(map):
	global width
	width = ''
	for index in range(len(map[0])):
		if map[0][index]=='x':
			i = index+1
			while isInt(map[0][i]):
				width = width + map[0][i]
				i+=1
			break
	try:
		width = int(width)
	except:
		print("=> Erreur")
		exit()

def setHeight(map):
	global height
	height = ''
	for index in range(len(map[0])):
		if map[0][index]=='x':
			break
		elif isInt(map[0][index]):
			height = height + map[0][index]
	try:
		height = int(height)
	except:
		print("=> Erreur")
		exit()

def setChar(map):
	global charachters
	try:
		charachters = map[0][-5:]
	except:
		print("=> Erreur")
		exit()

def get_exits(map):
	exits = []
	for raw in range(1,len(map)):
		pos = []
		for col in range(len(map[raw])):
			if map[raw][col] == charachters[-1]:
				pos.append(raw)
				pos.append(col)
		if len(pos)>0:
			exits.append(pos)
	if len(exits)>0:
		return exits
	else:
		print("=> Erreur: pas de sorties !")
		exit()

def checkMap(map):
	if len(map)==height+1:
		for index in range(1,len(map)):
			if len(map[index])!= width:
				print('=> Erreur')
				exit()
	else:
		print("=> Erreur")
		exit()

def get_start(map):
	start = []
	for raw in range(1,len(map)):
		pos = []
		for col in range(len(map[raw])):
			if map[raw][col] == charachters[-2]:
				pos.append(raw)
				pos.append(col)
		if len(pos)>0:
			start.append(pos)
	if len(start)>0:
		return start
	else:
		print("=> Erreur: pas d'entrées !")
		exit()

def solve(labyrinth,exit,start):
	trys = []

	for exit_pos in exit:
		steps = []
		removed = []
		if bad_step(labyrinth,exit_pos[0],exit_pos[1],steps):
			continue

		for start_pos in start:

			if bad_step(labyrinth,start_pos[0],start_pos[1],steps):
				continue
			pos = start_pos
			steps.append(pos)
		
			while pos != exit_pos:
				if pos not in steps:
					steps.append(pos)
		
				possibilities = next_step(labyrinth,pos[0],pos[1],steps,exit_pos)
				pos = best_step(labyrinth,possibilities,exit_pos,steps)
		
				if pos!=steps[-1]:
					steps.append(pos)
		
				elif pos == exit_pos:
					break
		
				elif pos == steps[-1]:
					removed.append(pos)
					pos = resolve(labyrinth,steps,removed,exit_pos)
			trys.append(steps)
	if len(trys) !=0:
		print_best_try(labyrinth,trys)
	else:
		print("=> Erreur")

def resolve(labyrinth,steps,removed,exit_pos):
	index = len(steps) - 1
	while index >=0:
		pos = steps[index]

		possibilities = next_step(labyrinth,pos[0],pos[1],steps,exit_pos)

		for p in possibilities:

			if p not in steps and p not in removed:
				return p
				index +=1

		steps.remove(pos)
		removed.append(pos)
		index-=1

def next_step(labyrinth,raw,col,steps,exit_pos):
	possibilities = []

	if [raw,col] == exit_pos:
		return [exit_pos]

	for x,y in [(raw+1,col),(raw-1,col),(raw,col+1),(raw,col-1)]:
		if (x>=0 and x<height 
			and y>=0 and y<width 
			and labyrinth[x][y] != charachters[0] 
			and [x,y] not in steps
			and not bad_step(labyrinth,x,y,steps,exit_pos)):
			possibilities.append([x,y])

	return possibilities

def best_step(labyrinth,possibilities,exit_pos,steps):

	diff_x = abs(exit_pos[0] - steps[-1][0])
	diff_y = abs(exit_pos[1] - steps[-1][1])
	best= steps[-1]

	for pos in possibilities:
		if abs(exit_pos[0]-pos[0]) == diff_x and abs(exit_pos[1]-pos[1]) < diff_y:
			best = pos

		if abs(exit_pos[1]-pos[1]) == diff_y and abs(exit_pos[0]-pos[0]) < diff_x:
			best = pos

	return best

def bad_step(labyrinth,raw,col,steps):
	bad = True

	if raw-1>0:
		if [raw-1,col] not in steps and labyrinth[raw-1][col] != charachters[0]:
			bad = False
	if col-1>0:
		if [raw,col-1] not in steps and labyrinth[raw][col-1] != charachters[0]:
			bad = False
	if raw+1<height:
		if [raw+1,col] not in steps and labyrinth[raw+1][col] != charachters[0]:
			bad = False
	if col+1<width:
		if [raw,col+1] not in steps and labyrinth[raw][col+1] != charachters[0]:
			bad = False

	return bad

def print_best_try(labyrinth,trys):
	short_path = trys[0]
	for index in range(1,len(trys)):
		if len(trys[index]) < len(short_path):
			short_path = trys[index]
	
	for pos in short_path[1:-1]:
		labyrinth[pos[0]][pos[1]] = charachters[-3]

	for line in labyrinth:
		for elm in line:
			print(elm,end='')
		print('\t')

	print(f'=> SORTIE ATTEINTE EN {len(short_path)-2} COUPS')

with open(sys.argv[1],'r') as f:
	lines = f.readlines()
labyrinth = getMap(lines)
checkMap(labyrinth)
start = get_start(labyrinth)
exit = get_exits(labyrinth)
solve(labyrinth,exit,start)