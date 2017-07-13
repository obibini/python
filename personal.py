#def get_age():
	#age = (int)(raw_input("What's your age?"))
	#return age
	
#def get_name():
	#return raw_input("What's your name?")
	
#ge = get_age() 
#name = get_name()
#print "Hey, " + name + ", you are " + str(age) + "years old, dude!"

def calculate (op1, op2, f):
	if f == "add":
		return op1 + op2
	elif f == "subtract":
		return op1 - op2
	elif f == "multiply":
		return op1 * op2
	else f == "divide":
		return op1 / op2
