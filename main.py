from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine_on = True
coffee_machine = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

while coffee_machine_on:

    customer_order = input("What would you like? (espresso/latte/cappuccino/): ").lower()

    if customer_order == "off":
        coffee_machine_on = False
        continue
    elif customer_order == "report":
        print(coffee_machine.report())
        continue

    if customer_order in menu.get_items():
        drink = menu.find_drink(customer_order)
        coffee_machine.is_resource_sufficient(drink)
    else:
        print("Item not available, try again.")
        continue

    for item in menu.menu:
        if item.name == customer_order:
            customer_order = item

    if money_machine.make_payment(customer_order.cost):
        coffee_machine.make_coffee(customer_order)
        money_machine.report()


