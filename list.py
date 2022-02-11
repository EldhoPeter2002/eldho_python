list=[]
n=int(input("Enter the size of list"))
i=0
flag=0
for i in range(0,n):
     num=int(input("Enter the elements"))
     list.append(num)
print(list)
a=int(input("Enter the number to be searched"))
for i in range(0,n):
	if(list[i]==a):
		flag=flag+1
		break;
if(flag==0):
	print("Element not found")
else:
	print(a,"Found at",i+1)
                     
         