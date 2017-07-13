def calculate(num1, num2, f):
    if f =="add":
        return num1 + num2
    elif f == "subtract":
        return num1 - num2
    elif f == "multiply":
        return num1 * num2
    elif f == "divide":
        return num1 / num2
    else:
        print ('invalid')

print("Select operation.")
print("Add")
print("Subtract")
print("Multiply")
print("Divide")

choice = raw_input("Enter choice:")

op1 = int(raw_input("Enter first number: "))
op2 = int(raw_input("Enter second number: "))

results = calculate(op1, op2, choice)
print results
