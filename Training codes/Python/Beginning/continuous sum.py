def sums(n):
    t=1
    for i in range(n,101,2):
        print("{}  {}".format(t,i))
        t=t+1

te=1
while te==1:
    n=int(input("Enter a number: "))
    sums(n)
    res=input("Do you want to continue: ")
    if res=='y' or res=='Y':
        pass
    else:
        te=2