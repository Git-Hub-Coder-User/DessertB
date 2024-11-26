"""
'A Dessert Shop sells candy by the pound, cookies by the dozen, ice cream by the scoop, and sundaes (ice cream with a topping).
For this part of the project, you will create the structure for a Dessert Shop program. There will be no user interface nor input/output at this time, but there will be later. Your code will be tested using automated test cases.
Test code can be simple asserts, unittest code, pytest code, or doctests as long as your set of test cases meets the requirements specified for the project. Whichever you choose, be consistent. unittest is built-in with Python, as are doctests and asserts. pytest is a 3rd-party module but is simpler to write code for than unittest, and it will run unittest code. Whichever you choose, be consistent.
To create this framework, you will implement an inheritance hierarchy of classes derived from a DessertItem superclass. Candy, Cookie, and IceCream classes will derive from the DessertItem class. The Sundae class will derive from the IceCream class. The classes will be structured as below.' - Instructions

"""
from abc import ABC, abstractmethod

class DessertItem(ABC):
    def __init__(self, name = ""):
        self.name = name
        self.tax_percent = 7.25
    
    def get_list(self):
        return []
    
    @abstractmethod
    def calculate_cost(self):
        return 0 
    
    def calculate_tax(self):
        returned = self.calculate_cost() * self.tax_percent * .01
        return returned


class Candy(DessertItem):
    def __init__(self, name, candy_weight = 0.0, price_per_pound = 0.0):
        super().__init__(name)
        self.candy_weight = candy_weight
        self.price_per_pound = price_per_pound
    
    def __str__(self):
        return f"{self.name}, {self.candy_weight}lbs, ${self.price_per_pound}/lb, {self.calculate_cost():.2f}, {self.calculate_tax():.2f}"
    
    def get_list(self):
        # print("CALLED")
        return [self.name, self.candy_weight, self.price_per_pound]
    
    def calculate_cost(self):
        cost = self.candy_weight * self.price_per_pound
        return cost
    

class Cookie(DessertItem):
    def __init__(self, name, quantity = 0, price_per_dozen = 0.0):
        super().__init__(name)
        self.quantity = quantity
        self.price_per_dozen = price_per_dozen
            
    def __str__(self):
        return f"{self.name}, {self.quantity} cookies, ${self.price_per_dozen}/dozen, {self.calculate_cost():.2f}, {self.calculate_tax():.2f}"

    def get_list(self):
        return [self.name, self.quantity, self.price_per_dozen]
    
    def calculate_cost(self):
        cost = self.quantity * self.price_per_dozen / 12
        return cost
    
class IceCream(DessertItem):
    def __init__(self, name, scoop_count = 0, price_per_scoop = 0.0):
        super().__init__(name)
        self.scoop_count = scoop_count
        self.price_per_scoop = price_per_scoop
            
    def __str__(self):
        return f"{self.name}, {self.scoop_count} scoops, ${self.price_per_scoop}/scoop, {self.calculate_cost():.2f}, {self.calculate_tax():.2f}"
        
    def get_list(self):
        return [self.name, self.scoop_count, self.price_per_scoop]
    
    def calculate_cost(self):
        cost = self.scoop_count * self.price_per_scoop
        return cost

class Sundae(IceCream):
    def __init__(self, name, scoop_count = 0, price_per_scoop = 0.0, topping_name = "", topping_price = 0.0):
        super().__init__(name, scoop_count, price_per_scoop)
        self.topping_name = topping_name
        self.topping_price = topping_price
    
    def __str__(self):
        return f"{self.topping_name} {self.name}, {self.scoop_count} scoops, {self.price_per_scoop}/scoop, {self.calculate_cost():.2f}, {self.calculate_tax():.2f}, {self.topping_name} topping, {self.topping_price}"

    def calculate_cost(self):
        cost = self.scoop_count * self.price_per_scoop + self.topping_price * self.price_per_scoop
        return cost

# test = Candy("Candy", 3.5, 2.4)
# print(test.get_list())
