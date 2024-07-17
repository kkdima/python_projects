from initial_data import MENU

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.00
}


def check_resources(drink):
    for ingredient in drink["ingredients"]:
        if resources[ingredient] < drink["ingredients"][ingredient]:
            print(f"Sorry, there's not enough of {ingredient}.")
            return False
    return True


def process_payment(drink):
    global resources
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))

    if quarters * 0.25 >= drink["cost"]:
        total = quarters * 0.25
        resources['money'] += drink['cost']
    else:
        dimes = int(input("How many dimes?: "))
        nickles = int(input("How many nickles?: "))
        pennies = int(input("How many pennies?: "))
        total = (quarters * 0.25) + (dimes * 0.10) + \
            (nickles * 0.05) + (pennies * 0.01)
        resources['money'] += drink['cost']

    if total < drink["cost"]:
        print("Sorry, that's not enough money. Money refunded.")
        return False

    change = round(total - drink["cost"], 2)
    print(f"Here is ${change} in change.")


def make_coffee(drink):
    for ingredient in drink["ingredients"]:
        resources[ingredient] -= drink["ingredients"][ingredient]


def show_report():
    print("\n")
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")
    print("\n")


def coffee_machine_start():
    machine_on = True
    while machine_on:
        print("\n")
        print("Welcome to the Coffee Machine!")
        print("What would you like to drink? (espresso/latte/cappuccino)")
        print("Type 'report' to see the current resource levels.")
        print("Type 'off' to turn off the machine.")
        print("\n")

        user_input = input("Type your choice: ").lower()

        if user_input == "report":
            show_report()
        elif user_input == "off":
            print("Coffee Machine is turning off...")
            machine_on = False
        elif user_input in MENU:
            drink = MENU[user_input]
            print(f"That will be ${drink['cost']}.")
            if check_resources(drink):
                if process_payment(drink):
                    make_coffee(drink)
                    print(f"Here is your {user_input}. Enjoy!")
                    show_report()
                    return True
        else:
            print("Invalid input. Please try again.")


if __name__ == "__main__":
    coffee_machine_start()
