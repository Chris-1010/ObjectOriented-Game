# Student Number: 122332721
import os

from restaurant import Restaurant

restaurant = Restaurant()

order_amount = 3

restaurant.open()

os.system("cls")
while restaurant._open:
    restaurant.order
    restaurant.prompt()
    os.system("cls")
    restaurant.status()
    restaurant.work()
    if len(restaurant._ordersCompleted) == order_amount:
        restaurant._open = False

restaurant.end_of_day()
