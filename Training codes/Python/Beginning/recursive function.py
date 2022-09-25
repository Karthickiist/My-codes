def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)

x=int(input("Enter a number: "))
print("The factorial of the number is %d"%(fact(x)))