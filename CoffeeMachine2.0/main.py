from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

m = Menu()
mm = MoneyMachine()
cm = CoffeeMaker()

still_on = True

while still_on:
    s = input(f"What would you like to have? ({m.get_items()}): ")
    if s == "report":
        cm.report()
        mm.report()
    elif s == "off":
        still_on = False
    else:
        drink = m.find_drink(s)
        if cm.is_resource_sufficient(drink) and mm.make_payment(drink.cost):
            cm.make_coffee(drink)
