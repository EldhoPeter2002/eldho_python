string=str(input("Enter the string: "))
c=0
v=0
q=0
w=1
for i in string:
	if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
	       v=v+1
	elif(i==' '):
	       w=w+1
	elif(i=='?'):
	       q=q+1
	else:
	       c=c+1
print("Vowels=",v)
print("words=",w)
print("consonents=",c)
print("question mark=",q)

