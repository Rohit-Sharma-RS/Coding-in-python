from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
latte = MenuItem('latte', 100, 30, 16,2.0)
capuccino = MenuItem('capuccino', 150, 100, 20,3.0)
espresso = MenuItem('espresso', 100, 0, 16,1.5)

menu = Menu()
money = MoneyMachine()
making = CoffeeMaker()


choice = input("What do you want\n1.latte\n2.espresso\n3.capuccino")
ch=Menu.find_drink(menu,choice)

if choice == "report":
    making.report()
if making.is_resource_sufficient(ch):
    if money.make_payment(ch.cost):
        making.make_coffee(ch)