list=[]
n=int(input("Enter the size of list "))
i=0
for i in range(0,n):
     num=int(input("Enter the elements "))
     list.append(num)
print(list)
sum=0
for i in range(0,n):
        sum=sum+int(list[i])
avg=sum/n
print("Average is",avg)
for i in list:
	sqr=i*i
	print("Square is ",sqr)
