a=int(input("Enter the number of terms "))
n2=1
n1,n0=(0,1)
count=0
if (a==1):
    print("Fibonacci sequence upto:",a)
    print(n1)
else:
    print("Fibonacci sequence")
    while (count<a):
         print(n1)
         nth=n1+n2
         n1=n2
         n2=nth
         count=count+1