def prime(n):
    if n==1:
        return True
    else:
        c=0
        for i in range(1,n+1):
            if n%i==0:
                c=c+1
        if c==2:
            return True
        else:
            return False

x=int(input("Enter the number: "))
if prime(x):
    print("The number is prime")
else:
    print("The number is not prime")