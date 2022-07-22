from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
resources = CoffeeMaker()
money = MoneyMachine()

while True:
    drink = input(f"What would you like?({menu.get_items()}): ")

    if drink == 'report':
        resources.report()
        money.report()

    elif drink == 'off':
        break

    else:
        coffee_details = menu.find_drink(drink)
        if resources.is_resource_sufficient(coffee_details):
            if money.make_payment(coffee_details.cost):
                resources.make_coffee(coffee_details)
