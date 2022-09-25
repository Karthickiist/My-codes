h=int(input("Number of hours worked: "))
if h<40:
    print("The total wage is: ",h*150)
else:
    r=h-40
    print("The regular wage: ",40*150)
    print("Overtime wage: ",r*225)
    print("Net pay: ",((40*150)+(r*225)))
