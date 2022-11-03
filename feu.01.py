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

def expression_between_brackets(expression):
	index =0 
	index_of_brackets = 0
	expr = []

	while index <len(expression):

		if expression[index][0]=='(':
			index_of_brackets = index
			while expression[index][-1]!=')':
				if len(expression[index])>1:
					expr.append(expression[index][1:])
				else:
					expr.append(expression[index])
				expression[index] = ''
				index+=1
			expr.append(expression[index][:-1])
			expression[index]=''
			return (expr,index_of_brackets)
		index+=1

def priority_operation(expression):
	result=0
	index=0
	while index < (len(expression)):
		if expression[index]== '*':
			expression[index]=''
			result=int(expression[index-1])*int(expression[index+1])
			expression[index-1]=result
			expression[index+1]=''
			remove_blanks(expression)
			index-=1
			continue

		elif expression[index]== '/':
			expression[index]=''
			result=int(expression[index-1])/int(expression[index+1])
			expression[index-1]=result
			expression[index+1]=''
			remove_blanks(expression)
			index-=1
			continue
		elif expression[index]== '%':
			expression[index]=''
			result=int(expression[index-1])%int(expression[index+1])
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
			result=int(expression[index-1])-int(expression[index+1])
			expression[index-1]=result
			expression[index+1]=''
			remove_blanks(expression)
			index-=1
			continue

		elif expression[index]== '+':
			expression[index]=''
			result=int(expression[index-1])+int(expression[index+1])
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
	return expression,index

def nbrOfBrackets(expression):
	nbr = 0
	for elm in expression:
		if elm == '(':
			nbr +=1
	return nbr


expression = '3 * 4 + ((2 * 5) + (4 * 5))'
nbrOfBrackets = nbrOfBrackets(expression)
expression = expression.split()


for nbr in range(nbrOfBrackets):
	(expression_btw_brackets,index_of_brackets)=expression_between_brackets(expression)
	priority_operation(expression_btw_brackets)
	non_priority_operation(expression_btw_brackets)
	expression[index_of_brackets] = str(expression_btw_brackets[0])
	remove_blanks(expression)
	print(expression,expression_btw_brackets)

priority_operation(expression)
non_priority_operation(expression)
print(expression[0])