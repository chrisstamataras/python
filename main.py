MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
continue_serving = True
user_input = ""
money = 0
bag = 0
water_in_tank = resources["water"]
milk_in_tank = resources["milk"]
coffee_in_tank = resources["coffee"]
while continue_serving:
    while user_input != "espresso" and user_input != "latte" and user_input != "cappuccino":
        user_input = input("What would you like? (espresso/latte/cappuccino): ")
        if user_input == "off":
            print("\nSystem turning off....")
            break
        if user_input == "report":
            print("Water: " + str(water_in_tank) + "ml\nMilk: " + str(milk_in_tank) + "ml\nCoffee: " + str(coffee_in_tank) + "g\nMoney: $" + str(money))
    if user_input == "off":
        break
    user_choice = MENU[user_input]
    user_ingredients = user_choice["ingredients"]
    if user_ingredients["water"] > water_in_tank:
        print("Sorry there is not enough water")
        user_input = ""
    if user_ingredients["milk"] > milk_in_tank:
        print("Sorry there is not enough milk")
        user_input = ""
    if user_ingredients["coffee"] > coffee_in_tank:
        print("Sorry there is not enough coffee")
        user_input = ""
    if user_ingredients["water"] < water_in_tank and user_ingredients["milk"] < milk_in_tank and user_ingredients["coffee"] < coffee_in_tank:
        print("Please insert coins.")
        quarters = int(input("How many quarters?: ")) * 0.25
        dimes = int(input("How many dimes?: ")) * 0.10
        nickles = int(input("How many nickles?: ")) * 0.05
        pennies = int(input("How many pennies?: ")) * 0.01
        total = quarters + dimes + nickles + pennies
        change = round(total - user_choice["cost"], 2)
        if total >= user_choice["cost"]:
            money += user_choice["cost"]
            water_in_tank -= user_ingredients["water"]
            milk_in_tank -= user_ingredients["milk"]
            coffee_in_tank -= user_ingredients["coffee"]
            print(f"Hare is ${change} in change")
            print(f"Here is your {user_input} ☕ Enjoy!!")
            user_input = ""
        else:
            print("Sorry that's not enough money. Money refunded.")
            user_input = ""
