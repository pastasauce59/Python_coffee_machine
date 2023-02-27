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
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
on = True
while on:
    choice = input("What would you like? (espresso/latte/capuccino): ").lower()
    if choice == 'espresso':
        print('make esspresso')
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