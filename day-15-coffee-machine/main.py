import random
import time

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
    "money": 0.0
}


# TODO-4: Check resources sufficient?
def check_resources(order_ingredients):
    for ingredient in order_ingredients:
        if order_ingredients[ingredient] > resources[ingredient]:
            print(f"Sorry, there's not enough {ingredient}. :(")
            return False
    return True


# TODO-5: Process coins.
def process_coins(drink_cost):
    print(f"Please insert coins: (${drink_cost:.2f})")
    quarters = int(input("How many quarters? ($0.25): "))
    dimes = int(input("How many dimes? ($0.10): "))
    nickles = int(input("How many nickles? ($0.05): "))
    pennies = int(input("How many pennies? ($0.01): "))

    total_inserted = (quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)
    return round(total_inserted, 2)


# TODO-6: Check transaction successful?
def check_transaction(money_received, drink_cost):
    if money_received < drink_cost:
        if random.random() < 0.4:
            print("Sorry that's not enough money. The money has been eaten. Thanks! 😋")
            return False
        else:
            print("Sorry that's not enough money. Money refunded. 🪙")
            return False
    elif money_received == drink_cost:
        resources["money"] += drink_cost
        return True
    else:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change:.2f} dollars in change.")
        resources["money"] += drink_cost
        return True


# TODO-7: Make Coffee.
def make_coffee(drink_name, order_ingredients):
    print("Payment accepted! Preparing your drink...")
    time.sleep(1)
    print("Grinding fresh coffee beans... 🫘⚙️")
    time.sleep(1.75)
    print("Boiling water... 🔥")
    time.sleep(3)
    for ingredient in order_ingredients:
        resources[ingredient] -= order_ingredients[ingredient]
    print(f"Here is your {drink_name}. Enjoy! ☕✨")


# TODO-1: Prompt user by asking "What would you like? (espresso/latte/cappuccino): "
is_on = True

while is_on:
    choice = input("What would you like? (espresso → $1.5 / latte → $2.5 / cappuccino → $3): ").lower().strip()
    if choice in MENU:
        drink = MENU[choice]
        if check_resources(drink["ingredients"]):
            confirm_payment = input("Would you like to proceed to payment? "
                                    "(Press Enter to continue or type 'cancel' to exit): ").lower().strip()

            while confirm_payment not in ["", "cancel"]:
                print("Invalid option. Type only 'Enter' or 'cancel'.")
                confirm_payment = input("Would you like to proceed to payment? "
                                        "(Press Enter to continue or type 'cancel' to exit): ").lower().strip()

            if confirm_payment == "cancel":
                print("Transaction cancelled. Have a nice day! 👋")
            else:
                payment = process_coins(drink["cost"])
                if check_transaction(payment, drink["cost"]):
                    make_coffee(choice, drink["ingredients"])


    # TODO-2: Turn off the Coffee Machine by entering “ off ” to the prompt.
    elif choice == "off":
        is_on = False
        print("Powering down... See you next time! :)")


    # TODO-3: Print report.
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${resources['money']:.2f}")

    else:
        print("Invalid choice. Please select espresso, latte, or cappuccino.")
