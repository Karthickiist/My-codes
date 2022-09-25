import os

def logo():
    logo = """
     _____________________
    |  _________________  |
    | | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
    | |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
    |  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
    | | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
    | |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
    | | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
    | |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
    | | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
    | |___|___|___| |___| | | |              | || |              | || |              | || |              | |
    | | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
    | |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
    |_____________________|
    """
    print(logo)


def add(n1,n2):
    return n1+n2


def subtract(n1,n2):
    return n1-n2


def multiply(n1,n2):
    return n1*n2


def divide(n1,n2):
    return n1/n2


calc={
    '+':add,
    '-':subtract,
    '*':multiply,
    '/':divide
}


def calculation():
    os.system('cls')
    logo()
    num1=float(input("Enter the first number: "))
    res='y'
    while res=='y':
        for i in calc:
            print(i)
        ope=input("Select the operator: ")
        num2=float(input("Enter the next number: "))
        answer=calc[ope](num1,num2)
        print(f"{num1}{ope}{num2}={answer}")
        res=input("Do you want to continue the calculation with this number(y/n)?: ")
        if res=='y':
            num1=answer
        else:
            calculation()


calculation()

