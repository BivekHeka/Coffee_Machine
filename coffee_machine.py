# Menu dictionary
menu = {
    "espresso": {
        "ingredients": {"water": 50, "coffee": 18},
        "cost": 1.5
    },
    "latte": {
        "ingredients": {"water": 200, "milk": 150, "coffee": 24},
        "cost": 2.5
    },
    "cappuccino": {
        "ingredients": {"water": 250, "milk": 100, "coffee": 24},
        "cost": 3.0
    }
}

# Resources in the machine
resources = {
    "water": 500,
    "coffee": 500,
    "milk": 500
}

money_earned = 0  # Track total money earned

# Function to check if resources are enough
def check_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources.get(item, 0):
            print(f"Sorry, not enough {item}")
            return False
    return True

# Function to process coins
def process_coins():
    print("Please insert the coins.")
    total = int(input("How many 1 rupee coins? ")) * 1
    total += int(input("How many 2 rupee coins? ")) * 2
    total += int(input("How many 5 rupee coins? ")) * 5
    return total

# Function to display the menu
def display_menu():
    print("\n--- Coffee Menu ---")
    for drink_name, drink_info in menu.items():
        print(f"{drink_name.capitalize()}: {drink_info['cost']} rupees")
    print("-------------------\n")

# Main program loop
while True:
    display_menu()
    choice = input("What would you like to drink? (espresso/latte/cappuccino) or 'report'/'off': ").lower()

    if choice == "off":
        print("Turning off the coffee machine. Goodbye!")
        break

    if choice == "report":
        print("\nResources remaining:")
        for item in resources:
            print(f"{item}: {resources[item]}ml")
        print(f"Money earned: {money_earned} rupees\n")
        continue

    if choice in menu:
        drink = menu[choice]

        # Show ingredients for selected drink
        print(f"\nYou selected: {choice.capitalize()}")
        print("Ingredients needed:")
        for item, amount in drink["ingredients"].items():
            print(f"  {item}: {amount}ml")
        print(f"Cost: {drink['cost']} rupees\n")

        # Check resources
        if check_resources(drink["ingredients"]):
            payment = process_coins()
            print(f"You inserted: {payment} rupees")

            if payment >= drink["cost"]:
                change = round(payment - drink["cost"], 2)
                money_earned += drink["cost"]

                print("Payment accepted.")
                if change > 0:
                    print(f"Here is your change: {change} rupees")

                # Deduct resources
                for item in drink["ingredients"]:
                    resources[item] -= drink["ingredients"][item]

                print(f"Please wait... Making your {choice} ☕ Enjoy!\n")
            else:
                print("Not enough money. Order cancelled.\n")
        else:
            print("Order cancelled due to insufficient resources.\n")
    else:
        print("!! Invalid Order !!\n")
