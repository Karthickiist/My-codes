def primelist():
    count=1
    pri=[1]
    n=2
    while count<=100:
        c=0
        for i in range(1,n+1):
            if n%i==0:
                c=c+1
        if c==2:
            pri.append(n)
            count=count+1
        n=n+1
    return pri

c=0
for i in primelist():
    print("%4d "%i,end="")
    c=c+1
    if c%10==0:
        print()