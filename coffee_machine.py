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


def check_resources(selected_drink):
    """Takes in a dictionary of type of drink with it's ingredients and returns if there is sufficent resources in the coffee machine to make it."""

    ingredients = selected_drink['ingredients']

    for item in ingredients:
        if resources[item] < ingredients[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    
    return True


def add_coins(quarters, dimes, nickels, pennies):
    """Takes in coins, multiplies them by their respective value and then returns total money given by user."""
    total = (quarters * .25) + (dimes * .10) + (nickels * .05) + (pennies * .01)
    return total


def make_drink(money_given, choice_name, drink, resources_on_hand):
    """Takes in money given by user and sees it if covers the cost of users desired drink,
    if so then updates coffee machine resources less ingredients needed for drink and returns made drink."""
    if money_given >= drink['cost']:
        resources_on_hand['money'] += drink['cost']
        change = money_given - drink['cost']
        print(f"Here is ${change} in change.")
        
        ingredients = drink['ingredients']
        for key in ingredients:
            resources_on_hand[key] = resources_on_hand[key] - ingredients[key]
        return f"Here is your {choice_name} ☕️. "
    else:
        return "Sorry, that is not enough. Money refunded."

machine_on = True
while machine_on:
    choice = input("What would you like? (espresso/latte/capuccino): ").lower()
    if choice == 'espresso' or choice == 'latte' or choice == 'cappuccino':
        sufficient_resources = check_resources(MENU[choice])
        if sufficient_resources:
            print("Please insert coins.")
            quarters = float(input("how many quarters?: "))
            dimes = float(input("how many dimes?: "))
            nickels = float(input("how many nickels?: "))
            pennies = float(input("how many pennies?: "))

            money = add_coins(quarters, dimes, nickels, pennies)
            drink = make_drink(money, choice, MENU[choice], resources )
            print(drink)
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
        