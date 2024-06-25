# Student Number: 122332721
from order import Order

class Restaurant:
    def __init__(self):
        self._currentOrder = None
        self._ordersCompleted = []
        self._orderAmount = 0
        self._open = False
        self._income = 0
        self._expectedIncome = 0
        self._cooking = None

    def open(self):
        import time

        for second in range(3, 0, -1):
            print(f"\rRestaurant opening in {second} seconds", end="")
            time.sleep(1)
        self._open = True

    def newOrder(self):
        self.order = Order()
        self._expectedIncome += self.order._food._cost
        print(self.order)

    def getOrder(self):
        if self._currentOrder == None:
            self.newOrder()
        return self._currentOrder
    
    def setOrder(self, order):
        self._currentOrder = order


        
    def work(self):
        cooking_item = (input("\nWhat to cook?\t")).lower()
        if cooking_item != self.order._food.__str__().lower():
            self.order._customerSatisfaction -= 50
            self.badOrder(self.order, "Wrong Food Type")
            return
        self.status()
        self.cook(self.order)
        self.addToppings(self.order)
        self.completeOrder(self.order)
        

    def cook(self, order):
        import time
        import os

        second = 0
        in_for = None

        while in_for == None:
            in_for = input(f"Cook {order._food.__str__().lower()} for how long?\t")
            try:
                in_for = int(in_for)
            except ValueError:
                print("Invalid Time!")
                in_for = None
                continue

        if (abs(in_for - order._cookingTime) >= 20):
            self.badOrder(self.order, "Cooking Time Too Long")
            return
    
        while second < in_for:
            print(f"\rPreparing {order._food.__str__()}")
            time.sleep(0.33)
            os.system("cls")
            second += 1
            print(f"\rTime elapsed: {second} seconds\n")
        print(f"Done!\n{order._customer}'s Reaction: {order.cookingReaction(in_for)}\n")

    def addToppings(self, order):
        print("Toppings to add (Leave blank when finished):\n")
        still_adding = True
        while still_adding:
            new_topping = input("")
            if new_topping == "":
                still_adding = False
            else:
                new_topping = new_topping.title()
                if new_topping in order._toppings:
                    print("✅\n")
                    order._toppings.remove(new_topping)
                    order._customerSatisfaction += 10
                else:
                    print("❌\n")
                    order._customerSatisfaction -= 5
        if len(order._toppings) != 0:
            print(f"Forgot {', '.join(order._toppings)}\n")
            order._customerSatisfaction -= (3 * len(order._toppings))
        else:
            print("All toppings added!\n")

    def completeOrder(self, order):
        print("Order Completed!")
        print(f"Food Cost:\t€{order._food._cost:.2f}")
        if order._customerSatisfaction > 100:
            tips = 2 * (order._food._cost * ((order._customerSatisfaction - 100) / 100))
        else:
            tips = 0
        print(f"Tip Amount:\t€{tips:.2f}\n")
        order_income = order._food._cost + tips
        print(f"Order Total:\t€{order_income:.2f}\n")
        self._ordersCompleted.append(order)
        self._orderAmount += 1

        self._income += order_income
        print(f"Total Income:\t€{self._income:.2f}\n\n")

        self.order = None
        self.prompt()

    def badOrder(self, order, reason):
        print(f"Order Cancelled!\n{order._customer} stomped out of the restaurant.\nTheir reason: {reason}\n\n")
        print(f"Order Income:\t€{0:.2f}")
        print(f"Total Income:\t€{self._income:.2f}\n\n")

        self._orderAmount += 1
        self.order = None
        
        self.prompt()

    def end_of_day(self):
        import os

        os.system("cls")
        threshold = (.33 * self._expectedIncome)
        difference = self._income - self._expectedIncome
        if difference <= -1 * threshold:
            conclusion = "An absolutely terrible day for business! You're fired!"
        elif difference <= 0:
            conclusion = "A bad day for business! You must try harder!"
        elif difference <= threshold * 0.5:
            conclusion = "An alright day for business! We'll do better tomorrow!"
        elif difference >= threshold:
            conclusion = "An absolutely fantastic day for business! Promotion time!"
        elif difference >= threshold * 0.5:
            conclusion = "A really good day for business! Well Done!"

        print(f"Restaurant Closed!\n\nTotal Income:\t\t€{self._income:.2f}\nExpected Income:\t€{self._expectedIncome:.2f}\n\nOrders Completed: {len(self._ordersCompleted)}/{self._orderAmount}\n\nBoss' Words: {conclusion}")
        input("Press Enter to go home\n")

    def status(self):
        import os

        os.system("cls")
        print(f"""
              Restaurant Now Open!
              ---------------------
              Income: €{self._income:.2f}
              Orders Completed: {len(self._ordersCompleted)}
              ---------------------
              Current Order for {self.order._customer}
              """)
        
    def prompt(self):
        input("Press Enter to continue...\n")

    def __str__(self):
        self.status()

    order = property(getOrder, setOrder)
