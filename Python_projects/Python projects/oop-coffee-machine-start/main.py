from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu=Menu()
coffee=CoffeeMaker()
money=MoneyMachine()

res=True
while res:
    req_option=['off','report','cappuccino','latte','espresso']
    option = input(f"What would you like to have ({menu.get_items()})?: ")
    while not option in req_option:
        print("Invalid option, try again...")
        option = input(f"What would you like to have ({menu.get_items()})?: ")
    if option == 'report':
        coffee.report()
        money.report()
    elif option=='off':
        res=False
    else:
        drink = menu.find_drink(option)
        if drink=='':
            res=False

        elif coffee.is_resource_sufficient(drink):
            if money.make_payment(drink.cost):
                coffee.make_coffee(drink)

