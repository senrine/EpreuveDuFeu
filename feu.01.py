import sys

def checkArguments():
	operation = ['*','+','-','/','%','(',')',' ']
	if len(sys.argv) == 2:
		try:
			for elm in sys.argv[1]:
				if elm not in operation:
					int(elm)
		except:
			print('error')
			exit()

	else:
		print("error")
		exit()
 
def checkExpression():
	expression = sys.argv[1]
	brackets = ['(',')']
	operation = ['*','+','/','-','%']
	numbers = ['0','1','2','3','4','5','6','7','8','9']

	if expression[0] in operation or expression[-1] in operation:
		print('error')
		exit()

	for index in range(len(expression)-1):
		if expression[index] in brackets and expression[index+1] in brackets:
			print('error')
			exit()
		
		try:
			if expression[index] in operation and expression[index+2] not in numbers and expression[index+2] not in brackets:
				print("error")
				exit()
		except:
			exit()

		if (expression[index] in operation or expression[index] in numbers) and expression[index+1] in operation:
			print("error")
			exit()


def priority_operation(expression):
	result=0
	index=0
	while index < (len(expression)):
		if expression[index]== '*':
			expression[index]=''
			result=float(expression[index-1])*float(expression[index+1])
			expression[index-1]=result
			expression[index+1]=''
			remove_blanks(expression)
			index-=1
			continue

		elif expression[index]== '/':
			expression[index]=''
			result=float(expression[index-1])/float(expression[index+1])
			expression[index-1]=result
			expression[index+1]=''
			remove_blanks(expression)
			index-=1
			continue
		elif expression[index]== '%':
			expression[index]=''
			result=float(expression[index-1])%float(expression[index+1])
			expression[index-1]=result
			expression[index+1]=''
			remove_blanks(expression)
			index-=1
		
		index+=1

	return expression


def non_priority_operation(expression):
	result=0
	index=0
	while index < (len(expression)):
		if expression[index]== '-':
			expression[index]=''
			result=float(expression[index-1])-float(expression[index+1])
			expression[index-1]=result
			expression[index+1]=''
			remove_blanks(expression)
			index-=1
			continue

		elif expression[index]== '+':
			expression[index]=''
			result=float(expression[index-1])+float(expression[index+1])
			expression[index-1]=result
			expression[index+1]=''
			remove_blanks(expression)
			index-=1
			continue
		index+=1
	return expression


def remove_blanks(expression):
	index = 0
	while index < len(expression):
		if expression[index] == '' or expression[index] ==' ':
			expression.remove(expression[index])
			index-=1
		index+=1
	return expression

def open_brackets(expression):
	for index in range(len(expression)-1,0,-1):
		if expression[index][0] == '(':
			return index


def close_brackets(expression,index):
	while index<len(expression):
		if expression[index][-1] == ')':
			return index
		index+=1
	print("error")
	exit()

def remove_expression(expression,start,end):
	while start<=end:
		expression[start] = ''
		start += 1

def calculate(expression):
	while open_brackets(expression):
		expression_btw_brackets = []
		last_open_bracket = open_brackets(expression)
		last_closed_bracket = close_brackets(expression,last_open_bracket)

		beginningOfExpression = expression[last_open_bracket][1:]
		restOfExpression = expression[last_open_bracket+1:last_closed_bracket]
		endOfExpression = expression[last_closed_bracket][:-1]

		expression_btw_brackets.append(beginningOfExpression)
		expression_btw_brackets.extend(restOfExpression)
		expression_btw_brackets.append(endOfExpression)

		priority_operation(expression_btw_brackets)
		non_priority_operation(expression_btw_brackets)

		remove_expression(expression,last_open_bracket,last_closed_bracket)

		expression[last_open_bracket] = str(expression_btw_brackets[0])

		remove_blanks(expression)

	priority_operation(expression)
	non_priority_operation(expression)
	return expression


checkArguments()
expression = sys.argv[1].split()
checkExpression()
print(int(calculate(expression)[0]))