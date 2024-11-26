#"We'll burn that bridge when we get there" - LaRose
#"It's not because I'm avoiding it" - LaRose
#"Are you? " - LaRose
from dessert import(
    DessertItem,
    Candy,
    Cookie,
    IceCream,
    Sundae
)
from receipt import make_receipt

class Order:
    def __init__(self):
        self.order = []

    def __str__(self):
        string = ""
        for value in self.order:
            print(value.name)
            string += str(value) + ", "

        return string
    
    def __len__(self):
        return len(self.order)
    
    def add(self, DessertItem):
        self.order.append(DessertItem)
    
    def order_cost(self):
        total = 0
        for item in self.order:
            total += item.calculate_cost()
        return total
    
    def order_tax(self):
        tax = 0
        for item in self.order:
            tax += item.calculate_tax()
        return tax

class DessertShop:
    def __init__(self):
        pass

    def user_prompt_candy(self):
        while True: 
            try: 
                stored = Candy("Temp")
                stored.name = input("Enter the type of candy: ")
                stored.candy_weight = float(input("Enter the weight of candy: "))
                stored.price_per_pound = float(input("Enter the price per pound: "))
                return stored
            except:
                print("That input was invalid. ")

    def user_prompt_cookie(self):
        while True:
            try: 
                stored = Cookie("Temp")
                stored.name = input("Enter the type of cookie: ")
                stored.quantity = int(input("Enter the quantity purchased: "))
                stored.price_per_dozen = float(input("Enter the price per dozen: "))
                return stored
            except:
                print("That input was invalid. ")

    def user_prompt_icecream(self):
        while True:
            try: 
                stored = IceCream("Temp")
                stored.name = input("Enter the type of ice cream: ")
                stored.scoop_count = int(input("Enter the number of scoops: "))
                stored.price_per_scoop = float(input("Enter the price per scoop: "))
                return stored
            except:
                print("That input was invalid. ")

    def user_prompt_sundae(self):
        while True:
            try: 
                stored = Sundae("Temp")
                stored.name = input("Enter the type of ice cream: ")
                stored.scoop_count = int(input("Enter the number of scoops: "))
                stored.price_per_scoop = float(input("Enter the price per scoop: "))
                stored.topping_name = input("Enter the topping: ")
                stored.topping_price = float(input("Enter the price for the topping: "))
                return stored
            except:
                print("That input was invalid. ")



'''
Code to implement the main loop of terminal-based user interface for
Dessert Shop Part 4. Students should be able to paste this code into their own
main() method as-is and use it without change.
Author: George Rudolph
Date: 2 Jun 2023
'''
def main():
    shop = DessertShop()
    order = Order()
    listed = []
    sub_total = 0
    tax = 0
    # boolean done = false
    done: bool = False
    # build the prompt string once
    prompt = '\n'.join([ '\n',
    '1: Candy',
    '2: Cookie',
    '3: Ice Cream',
    '4: Sundae',
    '\nWhat would you like to add to the order? (1-4, Enter for done): '
    ])
    while not done:

        choice = input(prompt)
        match choice:
            case '':
                done = True
            case '1':
                item = shop.user_prompt_candy()
                order.add(item)
                print(f'{item.name} has been added to your order.')
            case '2':
                item = shop.user_prompt_cookie()
                order.add(item)
                print(f'{item.name} has been added to your order.')
            case '3':
                item = shop.user_prompt_icecream()
                order.add(item)
                print(f'{item.name} has been added to your order.')
            case '4':
                item = shop.user_prompt_sundae()
                order.add(item)
                print(f'{item.name} has been added to your order.')
            case _:
                print('Invalid response: Please enter a choice from the menu (1-4) or Enter')
        print()

    for item in order.order:
        listed.append([item.name, round(item.calculate_cost(), 2), round(item.calculate_tax(), 2)])
        sub_total += item.calculate_cost()
        tax += item.calculate_tax()

    total_cost = sub_total + tax
    total_number_of_items_in_the_order = len(order)

    listed.append(["Order Subtotals: ", "$" + str(round(sub_total, 2)), "$" + str(round(tax, 2))])
    listed.append(["Order Total:", "", "$" + str(round(total_cost, 2))])
    listed.append(["Total items in the order: ","", total_number_of_items_in_the_order])


    print(order)
    make_receipt(listed, "receipt")


#Old main
"""
def main():
    listed = []
    sub_total = 0
    tax = 0
    order = Order()
    order.add(Candy("Candy Corn", 1.5, .25))
    order.add(Candy("Gummy Bears", .25, .35))
    order.add(Cookie("Chocolate Chip", 6, 3.99))
    order.add(IceCream("Pistachio", 2, .79))
    order.add(Sundae("Vanilla", 3, .69, "Hot Fudge", 1.29))
    order.add(Cookie("Oatmeal Raisin", 2, 3.45))

    print(order, end = "")
    print("Total number of items in order:", len(order))

    for item in order.order:
        listed.append([item.name, round(item.calculate_cost(), 2), round(item.calculate_tax(), 2)])
        sub_total += item.calculate_cost()
        tax += item.calculate_tax()

    total_cost = sub_total + tax
    total_number_of_items_in_the_order = len(order)

    listed.append(["Order Subtotals: ", round(sub_total, 2), round(tax, 2)])
    listed.append(["Order Total:", "", round(total_cost, 2)])
    listed.append(["Total items in the order: ","", total_number_of_items_in_the_order])

    make_receipt(listed, "receipt")
"""

main()