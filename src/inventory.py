#!/usr/bin/python

# TODO
# methods
# create carts - done
# add items - done
# view items - done
# remove items - done
# clear cart - done
# check_valid - done
# replace item - done
# TODO
#
# Inventory - done
# Cart - done

# global variable 
cart_num = 0


class Inventory:
    ''' class to creat an inventory object to add items to carts , view  or remove items from carts '''

    def __init__(self, item=''):
        ''' initializes class object with an optional argument '''
        self.item = item
        self.cart = Cart()

    def add_items(self, cart_id):
        ''' method to add items with given inventory class id '''
        if self.cart.check_id(cart_id):
            cart_id = input("enter id: ")
            if self.cart.check_id(cart_id):
                self.item = input("enter your items: ")
                print("{0} with id ({1}) is being added to cart items".format(self.item, cart_id))
                if self.__check_valid(self.item):
                    self.cart.add_to_cart(self.item, cart_id)
                    print("items have been added.")
            else:
                print("cart id not found.")
        else:
            print("id not valid.")

    def __check_valid(self, item=None):
        ''' class method to check for items and verify them '''
        if str(item) == str(self.item):
            return True
        return False

    def view_items(self, cart=None):
        ''' displays items in a specified cart '''
        if not self.cart:
            cart = self.cart.item_list
            cout = 1
            if not cart:
                print("noting in your cart yet.")
            else:
                print("Your items are ")
                for item in cart:
                    print("{0}: {1}".format(cout, item))
                    cout += 1
        else:
            cout = 1
            if not self.cart.item_list:
                print("noting in your cart yet.")
            else:
                print("Your items are ")
                for item in self.cart.item_list:
                    print("{0}: {1}".format(cout, item))
                    cout += 1
    def replace_item(self, card_id):
        if not self.cart.cart_id:
            print("Invalid item cart id.")
        else:
            if self.cart.item_list:
                self.view_items()
                item = input("enter item number to replace: ")
                if int(item):
                    item = int(item)
                    if item >= 1 and item <= len(self.cart.item_list):
                        self.cart.item_list[item-1] = input("enter item to replace ({}): ".format(self.cart.item_list[item-1]))
                        print("item replaced.. check cart to review replacement.")
                else:
                    print("invalid number type.")
    def clear_carts(self, cart_id, cart=None):
        ''' method to empty out the cart with the specified cart id.'''
        if not cart:
            cart = self.cart
            if cart.check_id(cart_id):
                print("clearing items in cart......")
                cart.item_list.clear()
                print("cart is now empty..")
            else:
                print("specify valid cart's id.")

    def remove_items(self, cart_id):
        if self.cart.check_id(cart_id):
            if self.cart.item_list:
                print("Choose items you wish to remove")
                cout = 1
                for item in self.cart.item_list:
                    print("item({0}): {1}".format(cout, item))
                    cout += 1
                item_select = input("Enter item number to remove: ")
                
                try:
                    item_select = int(item_select)
                    print("removing..... item({0})".format(item_select))
                    print("{0} removed for shopping cart..".format(self.cart.item_list.pop(item_select - 1)))
                except:
                    print("item not valid.")
            else:
                print("nothing currectly in cart...")
        else:
            print("id not found for cart")


class Cart:
    ''' class creates a cart list to store items into shopping carts '''

    def __init__(self, ):
        self.item_list = []
        global cart_num
        cart_num += 1
        self.cart_id = cart_num

    def check_id(self, cart_id):
        if str(cart_id) == str(self.cart_id):
            return True
        return False

    def add_to_cart(self, item, cart_id):
        if self.check_id(cart_id):
            self.item_list.append(item)
