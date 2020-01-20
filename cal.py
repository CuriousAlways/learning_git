'''basic command line based calclator(python version 2.x)'''

flag = True
while flag:

	try:
		expr_str = input(">> ")
	except NameError: 
		flag = False
	else:
		print(expr_str)


