def odd(n):
    res=[]
    for i in range(1,n+1,2):
        res.append(i)
    return res

x=int(input("Enter a number: "))
print(odd(x))