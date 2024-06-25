# Student Number: 122332721

#region| Food Class
class Food():
    def __init__(self):
        self._cost = 10.00
        
    def getToppings(self):      # inheritance example - All subclasses inside Food will have this method
        import random
        chosen_toppings = []
        
        for topping in range(random.randint(1, 5)):     # can have up to 5 toppings
            chosen_toppings.append(random.choice(self._availableToppings))      # chooses random toppings from the food's available toppings
            self._cost += (0.5 + (0.1 * len(chosen_toppings)))      # adds cost of each topping to the cost of the food, increasing as the amount of toppings increases

        return chosen_toppings

#region|     Pizza Class
class Pizza(Food):
    def __init__(self):
        super().__init__()
        self._availableToppings = ["Pepperoni", "Sausage", "Ham", "Bacon", "Chicken", "Beef", "Mushroom", "Onion", "Olive", "Pepper", "Pineapple"]

    def __str__(self):
        return "Pizza"

#endregion

#region|     Burger Class
class Burger(Food):
    def __init__(self):
        super().__init__()
        self._availableToppings = ["Cheese", "Lettuce", "Tomato", "Onion", "Pickle", "Bacon", "Egg", "Ketchup", "Mayo", "Mustard"]

    def __str__(self):
        return "Burger"

#endregion

#region|     Hotdog Class
class Hotdog(Food):
    def __init__(self):
        super().__init__()
        self._availableToppings = ["Ketchup", "Mustard", "Onion", "Pickle", "Bacon", "Cheese", "Chilli", "Jalapeno"]

    def __str__(self):
        return "Hotdog"

#endregion

#region|     Burrito Class
class Burrito(Food):
    def __init__(self):
        super().__init__()
        self._availableToppings = ["Beef", "Chicken", "Pork", "Rice", "Beans", "Cheese", "Sour Cream", "Guacamole", "Salsa"]

    def __str__(self):
        return "Burrito"
    
#endregion

#endregion
