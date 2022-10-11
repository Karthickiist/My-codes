import os
import datas
menu=datas.MENU
resources=datas.resources

def report():
    print("Report of available resources ")
    print("-------------------------------")
    print(f"Coffee: {resources['coffee']}")
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Money: {resources['money']}")


def makedrink(drink):
    can_make = 'yes'
    for i in menu[drink]['ingredients']:
        if menu[drink]['ingredients'][i]>resources[i]:
            print(f"There is not enough {i} to make {drink}")
            can_make='no'
    if can_make == 'no':
        print('Filling required')
    else:
        Money_status=transaction(getmoney(drink),drink)
        if Money_status:
            for i in menu[drink]['ingredients']:
                resources[i] -= menu[drink]['ingredients'][i]
            print(f"Your {drink} is ready! enjoy your drink...")
        else:
            print("There is no enough money, Your money has been refunded")
            print("Collect your money...")


def getmoney(item):
    total=0
    print(f"Insert the coins for ${menu[item]['cost']} ")
    total+=int(input("Penny: "))*0.01
    total += int(input("Dime: ")) * 0.05
    total += int(input("Nickel: ")) * 0.10
    total += int(input("Quarter: ")) * 0.25
    total += int(input("Dollar: ")) * 1
    return total


def transaction(money,item):
    balance=0
    if money>=menu[item]['cost']:
        resources['money']+=menu[item]['cost']
        if money > menu[item]['cost']:
            balance=money-menu[item]['cost']
            print(f"Please collect your balance ${balance}")
        return True
    else:
        return False


res=True
while res:
    os.system('cls')
    option_req=['espresso', 'latte', 'cappuccino', 'report', 'off']
    option=input("What would you like to have (Espresso/Latte/cappuccino)?: ").lower()
    while option not in option_req:
        print("Invalid option... Try again")
        option = input("What would you like to have (Espresso/Latte/cappuccino)?: ").lower()
    if option=="off":
        res=False
    elif option=="report":
        report()
        input("Press Enter")
    else:
        makedrink(option)
        input("Press Enter")



