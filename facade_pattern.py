'''Example script showcasing the Facade design pattern via a vending machine process'''

import time

class ChoiceValidator:
    '''Checks if the users product selection is available'''
    def __init__(self, product_info_dict):
        self.product_info_dict = product_info_dict
    
    def check_product_choice(self, product_choice):
        return True if product_choice in self.product_info_dict.keys() else False
            

class Stock:
    '''Checks if the users product selection is in stock'''
    def __init__(self, product_info_dict):
        self.product_info_dict = product_info_dict
    
    def check_stock_level(self, product_choice):     
        for product_key, product_info in self.product_info_dict.items():
            if product_key == product_choice:
                return product_info.stock
        return False

    
class Dispenser:
    '''Initiates physical vending (activates dispensing process)'''    
    def dispense(self):
        print('Dispensing product...')
        time.sleep(3)
        

class ProductInfo:
    '''Product class for storing product information'''
    def __init__(self, name, price, stock_qty=0):
        self.name = name
        self.price = price
        self.stock = stock_qty

    def __str__(self):
        return f"Name: {self.name.title()};  Price: £{self.price};  Stock QTY: {self.stock}"


class VendingFacade:
    '''Facade for vending machine sub processes'''    
    
    #   Product dictionary to store information relating to each product
    product_info_dict = {}

    def add_product_info(self, name, price, stock_qty=0):
        '''Adds new product info to vending machine via ProductInfo'''
        self.product_info_dict[name] = ProductInfo(name, price, stock_qty)

    def __init__(self):
        self.add_product_info('peppermint tea', 3.70, 5)
        self.add_product_info('bulgarian fruit loaf', 1.90, 0)
        self.add_product_info('dairy milk', 1.20, 8)
        self.add_product_info('freddo', 0.10, 10)
        self.add_product_info('coffee', 3.20, 2)
        self.add_product_info('green tea', 2.60, 9)
        
        self.choice = ChoiceValidator(self.product_info_dict)
        self.stock = Stock(self.product_info_dict)
        self.dispenser = Dispenser()

    def add_stock(self, name, add_qty):
        '''Adds stock to an existing product'''
        for product_key, product_info in self.product_info_dict.items():
            if name == product_key:
                product_info.stock += add_qty

    def dispense_product(self, product_choice):
        '''Checks user choice and stock level before dispensing product'''
        choice = self.choice.check_product_choice(product_choice)
        stock = self.stock.check_stock_level(product_choice)

        if choice == True and stock > 0:
            self.dispenser.dispense()
            print(f'Dispensing complete. Enjoy your {product_choice}!')
            return True
        else:
            print(f'{product_choice.title()} is not available or out of stock...')
            return False


if __name__ == '__main__':

    vend = VendingFacade()

    # ------------------------------ TEST CASE ----------------------------------- #
    #   User input and initiation of vending process
    product_choice = input('Please select your food or drink: ')
    vend.dispense_product(product_choice.lower())

    #   Adding new product to vending machine and printing all product information
    vend.add_product_info('snickers', 2.30, 9)
    print('\n--- Product Information ---')
    for product_name, product_info in vend.product_info_dict.items():
        print(product_info.__str__()) # Note: Last product now 'Snickers'
    
    #   Updating existing product stock and printing all product information
    vend.add_stock('bulgarian fruit loaf', 5)
    print('\n--- Product Information ---')
    for product_name, product_info in vend.product_info_dict.items():
        print(product_info.__str__()) # Note: 'Stock QTY' increased from 0 to 5