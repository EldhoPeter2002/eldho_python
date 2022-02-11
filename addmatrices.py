A=[]
B=[]
row=int(input("Enter the no of rows "))
coloumn=int(input("Enter the no of coloumns "))
print("Enter the first matrix")
for i in range(0,row):
	r=[]
	for j in range(0,coloumn):
		a=int(input())
		r.append(a)
	A.append(r)
print(A)
print("Enter the second matrix")
for i in range(0,row):
	r=[]
	for j in range(0,coloumn):
		b=int(input())
		r.append(b)
	B.append(r)
print(B)
result=[]
for i in range(0,row):
	r=[]
	for j in range(0,coloumn):
		z=A[i][j]+B[i][j]
		r.append(z)
	result.append(r)
print("Result=")
for i in range(0,row):
	print(result[i])	  