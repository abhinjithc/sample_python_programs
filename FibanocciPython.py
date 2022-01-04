def fib(r):
    a=0
    b=1
    while(a<r):
        print(" ",a, end=" ")
        c=a+b
        a=b
        b=c
    print("\n")
a=int(input("Enter No. : "))
fib(no)
