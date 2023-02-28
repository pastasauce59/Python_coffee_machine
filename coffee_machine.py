# 🚧 Coffee Machine Under Construction 🚧

# TODO: Print a report of all the coffee machine resources.

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
    "water": 49,
    "milk": 200,
    "coffee": 100,
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
                return "Sorry, there is not enough water"
        elif key == 'milk':
            if milk < ingredients[key]:
                return "Sorry, there is not enough milk"
        elif key == 'coffee':
            if coffee < ingredients[key]:
                return "Sorry, there is not enough coffee"
    
    return "Sufficient resources on hand."

on = True
while on:
    choice = input("What would you like? (espresso/latte/capuccino): ").lower()
    if choice == 'espresso':
        # print('make esspresso')
        drink = check_resources(resources, MENU["espresso"])
        print(drink)
    elif choice == 'latte':
        print('make latte')
    elif choice == 'capuccino':
        print('make capuccino')
    elif choice == 'report':
        for key in resources:
            map = {
                'water': 'ml',
                'milk': 'ml',
                'coffee': 'g',
                'money': '$'
            }
            if key != 'money':
                print(f"{key}: {resources[key]}{map[key]}")
            else:
                print(f"{key}: {map[key]}{resources[key]}")
    elif choice == 'off':
        on = False