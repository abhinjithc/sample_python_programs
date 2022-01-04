def isPrime(n):
    f=0
    i=2
    while(i<n):
        if(n%i==0):
            f=1
            return 1
        i+=1
    return 0
"""  NEW CHANGES MADE """
def Prime(a,b):
    i=a
    while(i<=b):
        if(isPrime(i)==0):
            print(i)
        i+=1

Prime(0,200)

    
