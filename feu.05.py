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
	return map

def setWidth():
	global width
	width = 10

def setHeight():
	global height
	height = 10

def setChar():
	global charachters
	charachters = ['*',' ','o','1','2']

setWidth()
setChar()
setHeight()

def get_exits(map):
	exit = []
	for raw in range(1,len(map)):
		pos = []
		for col in range(len(map[raw])):
			if map[raw][col] == charachters[-1]:
				pos.append(raw)
				pos.append(col)
		if len(pos)>0:
			exit.append(pos)
	if len(exit)>0:
		return exit
	else:
		print("=> Erreur: pas de sorties !")
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

def solve(labyrinth,exit_pos,pos,steps,removed):
	if pos not in steps and pos not in removed:
		steps.append(pos)

	if pos == exit_pos:
		return True

	possibilities = next_step(labyrinth,pos[0],pos[1],steps,exit_pos)
	pos = best_step(labyrinth,possibilities,exit_pos,steps)

	if pos == steps[-1]:
		removed.append(pos)
		return False

	steps.append(pos)

	if solve(labyrinth,exit_pos,pos,steps,removed):
		return True
	else:
		new_pos = pos
		if len(possibilities)>1:
			for p in possibilities:
				if p not in steps and p not in removed:
					new_pos = p
			steps.remove(pos)
			solve(labyrinth,exit_pos,new_pos,steps,removed)
		else:
			steps.remove(pos)
			return False

def next_step(labyrinth,raw,col,steps,exit_pos):
	possibilities = []

	if [raw,col] == exit_pos:
		return exit_pos

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

def bad_step(labyrinth,raw,col,steps,exit_pos):
	bad = True

	if [raw,col] == exit_pos:
		return False

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


map2=['10x10* o12\n',
'*****2****\n',
'* *   ****\n',
'*    *** *\n',
'* **  ****\n',
'*  *******\n',
'* **     2\n',
'*    *   *\n',
'*    **  *\n',
'1  *******\n',
'**********\n']

map2 = getMap(map2)
start = get_start(map2)
exit = get_exits(map2)

steps = []
removed = []
steps.append(start[0])

solve(map2,exit[0],start[0],steps,removed)

print(steps)
print(removed)