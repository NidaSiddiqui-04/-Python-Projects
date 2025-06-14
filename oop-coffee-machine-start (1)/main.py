from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
my_money_machine=MoneyMachine()
my_coffee_maker=CoffeeMaker()
my_menu=Menu()
machine=False
while not machine:
    ask_user=input(f"What would you like? ({my_menu.get_items()}):")
    if ask_user=="off":
        machine=True
    elif ask_user=="report":
        my_coffee_maker.report(),my_money_machine.report()
    else:
        drink=my_menu.find_drink(ask_user)
        if my_coffee_maker.is_resource_sufficient(drink):
           if my_money_machine.make_payment(drink.cost):
                my_coffee_maker.make_coffee(drink)

