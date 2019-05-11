#!/usr/bin/python3
import sys
from inventory import Inventory
class Menu:
    ''' class Menu function to display simple user interactive prompt to add, remove items from cart and other functions 
        i havnt added yet. '''
    def __init__(self, ):
        self.invent = Inventory()
        self.choices = {
                "1": self.add_to_cart,
                "2": self.view_cart,
                "3": self.remove_cartitems,
                "4": self.empty_cart,
                "5": self.replace_items,
                "6": self.quit        
                }

    def interface(self):
        print("""
        SHOPPING INVENTORY 

        1. add items to cart
        2. view items in cart 
        3. remove items from cart
        4. empty cart
        5. replace item in cart
        6. quit
        """)

 
    def add_to_cart(self):
        ''' function to add items into cart list '''
        self.invent.add_items(self.invent.cart.cart_id)
        
    


    def view_cart(self):
        ''' function to display items inside a cart list '''
        self.invent.view_items()
    
    def replace_items(self):
        ''' function to replace items inside a cart list '''
        try:
            self.invent.replace_item(self.invent.cart.cart_id)
        except Exception as Err:
            print('invalid option! ({})'.format(Err))
    
    def remove_cartitems(self):
        ''' function to remove individual items of a cart list '''
        self.invent.remove_items(self.invent.cart.cart_id)

    

    def empty_cart(self):
        ''' function to empty cart list '''
        self.invent.clear_carts(self.invent.cart.cart_id)
    
    def quit(self):
        ''' function to quit from runtime '''   
        print("Thanks for shopping with us.. See you next time.")
        sys.exit(0)

    def run(self):
        while True:
            self.interface()
            choice = input("enter an option: ")
            action = self.choices.get(str(choice))

            if action:
                action()
            else:
                print("({0}) not a valid option. ".format(choice))


if __name__ == "__main__":
    Menu().run()
