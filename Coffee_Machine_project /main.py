MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


while True:
    drink = input("What would you like? (espresso/latte/cappuccino): ")
    if drink == 'off':
        break

    elif drink == 'report':
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}ml")
        print(f"Money: ${profit}")
        continue
    elif resources['water'] - MENU[drink]['ingredients']['water'] < 0:
        print("Sorry there is not enough water")
        break
    elif resources['milk'] - MENU[drink]['ingredients']['milk'] < 0:
        print("Sorry there is not enough milk")
        break
    elif resources['coffee'] - MENU[drink]['ingredients']['coffee'] < 0:
        print("sorry there is not enough coffee")
        break
    print("Please insert coins")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    total = (quarters*0.25)+(dimes*0.1)+(nickles*0.05)+(pennies*0.01)
    change = total - MENU[drink]['cost']
    if change < 0:
        print("Sorry that's enough money. Money refunded.")
    else:
        print(f"Here is ${change: 0.2f} in change.")
        print(f"Here is your {drink} ☕️. Enjoy!")
        profit += MENU[drink]['cost']
        resources['water'] -= MENU[drink]['ingredients']['water']
        resources['milk'] -= MENU[drink]['ingredients']['milk']
        resources['coffee'] -= MENU[drink]['ingredients']['coffee']
