n=int(input("enter how many numbers "))
a=0
b=1
for i in range(n):
    print(a)
    x=a
    a=b
    b=x+b
