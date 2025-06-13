def add(a, b):
	return a + b

def subtract(a,b):
	return a-b

def mul(a,b):
	return a*b

def div(a,b):
	return a/b

Num1=(int(input("Enter the first number:")))
Num2=(int(input("Enter the second number:")))
operator = input("Enter the operator(+,-,*,/): ")
if operator == '+':
	print("Ans: ", add(Num1, Num2))
elif operator == '-':
	print("Ans: ",subtract(Num1, Num2))
elif operator == '*':
	print("Ans: " + str(mul(Num1, Num2)))
elif operator == '/':
	print("Ans: " + str(div(Num1, Num2)))

else:
	print("Error: Invalid operator. Please use +, -, *, or /.")

