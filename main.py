MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk" : 0
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

machine_on = True
profit = 0

def report(resources):
    global profit
    for item in resources:
        print(f"{item}: {resources[item]} ml")
    print(f"money: ${profit}")

def question() :
    global machine_on
    order = input("What would you like? (espresso/latte/cappuccino): ")
    if order == "off":
        print("Machine off.")
        machine_on = False
    elif order == "report":
        report(resources)
    else:
        check_resources(order, resources)

def insert_coin():
    # quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
    print("Please insert coins.")
    quarters = float(input("How many quarters?: "))
    dimes = float(input("How many dimes?: "))
    nickles = float(input("How many nickles?: "))
    pennies = float(input("How many pennies?: "))
    total_paid = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    return total_paid


def price_calculate(order):
    global profit
    price = MENU[order]["cost"]
    total_paid = insert_coin()
    while total_paid < price :
        print("Sorry that's not enough money. Money refunded.")
        insert_coin()
    if total_paid > price:
        change = round(total_paid - price, 2)
        profit += price
        print(f"Here is {change} in change.")
    print(f"Here is your {order}. Enjoy!")
    make_coffee(order, resources)
    question()

# TODO check_resources
def check_resources(order, resources):
    order_ingredient = MENU[order]["ingredients"]
    is_sufficient = True
    for item in resources:
        if order_ingredient[item] > resources[item] :
            print(f"Sorry there is not enough {item}.")
            is_sufficient = False
    if not is_sufficient :
        question()
    else:
        price_calculate(order)
   

# TODO 
def make_coffee(order, resources):
    for item in resources:
        resources[item] -= MENU[order]["ingredients"][item]
    return resources

while machine_on:
    question()


