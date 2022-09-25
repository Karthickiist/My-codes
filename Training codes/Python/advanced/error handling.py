
n=int(input("numerator: "))
d=int(input("Denominator: "))
try:
    print("Value is {}".format(n/d))
except ZeroDivisionError:
    print("Indivisible values")
except Exception as e:
    print("Eroor: ")
    print(e.message)