# 🚧 Coffee Machine Under Construction 🚧

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


def check_resources(current_resources, selected_drink):
    """Takes in a dictionary of resources and a dictionary of type of drink with ingredients and returns if there is sufficent resources to make it."""
    water = current_resources['water']
    milk = current_resources['milk']
    coffee = current_resources['coffee']

    ingredients = selected_drink['ingredients']

    for key in ingredients:
        if key == 'water':
            if water < ingredients[key]:
                print("Sorry, there is not enough water.")
                return False
        elif key == 'milk':
            if milk < ingredients[key]:
                print("Sorry, there is not enough milk.")
                return False
        elif key == 'coffee':
            if coffee < ingredients[key]:
                print("Sorry, there is not enough coffee.")
                return False
    
    # return "Sufficient resources on hand."
    return True


def add_coins(quarters, dimes, nickels, pennies):
    """Takes in coins, multiplies them by their respective value and then returns total money given by user."""
    total = (quarters * .25) + (dimes * .10) + (nickels * .05) + (pennies * .01)
    return f"${total}"

machine_on = True
while machine_on:
    choice = input("What would you like? (espresso/latte/capuccino): ").lower()
    if choice == 'espresso' or choice == 'latte' or choice == 'capuccino':
        sufficient_resources = check_resources(resources, MENU[choice])
        if sufficient_resources:
            # print(f'Making an order of {choice}')
            print("Please insert coins.")
            quarters = int(input("how many quarters?: "))
            dimes = int(input("how many dimes?: "))
            nickels = int(input("how many nickels?: "))
            pennies = int(input("how many pennies?: "))

            money = add_coins(quarters, dimes, nickels, pennies)
            print(money)
    elif choice == 'report':
        map = {
            'water': 'ml',
            'milk': 'ml',
            'coffee': 'g',
            'money': '$'
        }
        for key in resources:
            if key != 'money':
                print(f"{key}: {resources[key]}{map[key]}")
            else:
                print(f"{key}: {map[key]}{resources[key]}")
    elif choice == 'off':
        machine_on = False
        