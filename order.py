# Student Number: 122332721
from food import Pizza, Burger, Hotdog, Burrito

#region| Order Class
class Order():
    def __init__(self):
        import random
        self._customer = self.retrieveCustomerName()
        self._food = random.choice([Pizza(), Burger(), Hotdog(), Burrito()])
        self._toppings = self._food.getToppings()
        self._cookingTime = random.randint(1, 15)
        self._customerSatisfaction = 100

    def retrieveCustomerName(self):
         # import names from a file
        import random
        Port = open("names.txt", "r")
        people = Port.read().split("\n")
        return random.choice(people)
    
    def cookingReaction(self, timeElapsed):
        if abs(self._cookingTime - timeElapsed) >= 4:
            self._customerSatisfaction -= 20
            return f"😠\t\t\tIT WAS TO BE IN FOR {self._cookingTime} SECONDS!!!"
        elif abs(self._cookingTime - timeElapsed) == 3:
            self._customerSatisfaction -= 15
            return f"😐\t\t\tIt was supposed to be in for {self._cookingTime} seconds"
        elif abs(self._cookingTime - timeElapsed) == 2:
            self._customerSatisfaction -= 8
            return f"🙂\t\t\t2 seconds out but it's alright."
        elif abs(self._cookingTime - timeElapsed) == 1:
            self._customerSatisfaction -= 5
            return "😋\t\t\t1 second more and it would have been perfect!"
        else:
            return "🤩\t\t\tPERFECT!"

    def __str__(self):
        return f"""
                        New Order:\n\n
        
                        Customer:\t\t{self._customer}\n
                        Food:\t\t\t{self._food.__str__()}\n
                        Toppings:\t\t{", ".join(self._toppings)}\n
                        Cooking Time:\t\t{self._cookingTime} seconds\n
                    """
    
    
#endregion
