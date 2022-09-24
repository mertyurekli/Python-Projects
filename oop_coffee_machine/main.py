from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

off = False
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

while not off:
    items = menu.get_items()
    choice = input(f"What would you like? {items}: ")
    if choice == 'off':
        off = True
    elif choice == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)

