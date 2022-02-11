def add(a,b):
	c=a+b
	return c
def sub(a,b):
	c=a-b
	return c
def multi(a,b):
	c=a*b
	return c
def div(a,b):
	c=a/b
	return c
def exp(a,b):
	c=a**b
	return c
a=int(input("Enter the first number"))
b=int(input("Enter the second number"))
print("Enter the operation")
print("a for ADDITION")
print("s for SUBTRACTION")
print("m for MULTIPLICATION")
print("d for DIVISION")
print("e for EXPONENT")
choice=str(input("a,s,m,d,e: "))
if(choice=="a"):
	print("result =",add(a,b))
elif(choice=="s"):
	print("result =",sub(a,b))
elif(choice=="m"):
	print("result =",multi(a,b))
elif(choice=="d"):
	print("result =",div(a,b))
elif(choice=="e"):
	print("result =",exp(a,b))
else:
	print("INVALID INPUT")