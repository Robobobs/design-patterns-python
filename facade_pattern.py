'''Example script showcasing the Facade design pattern via a vending machine process'''

import time

class ChoiceValidator:
    '''Checks if the users product selection is available'''
    def check_drink_choice(self, product_choice, product_info_dict):
        return True if product_choice in product_info_dict.keys() else False
            

class Stock:
    '''Checks if the users product selection is in stock'''
    def check_stock_level(self, product_choice, product_info_dict):     
        for product_key, product_dict in product_info_dict.items():
            if product_key == product_choice:
                return product_dict[self.stock]
        return False

    
class Dispenser:
    '''Initiates physical vending (activates dispensing pump)'''    
    def dispense(self):
        print('Dispensing drink...')
        time.sleep(3)
        

class ProductInfo:
    '''Product class for storing product information'''
    def __init__(self, name, price, stock_qty=0):
        self.name = name
        self.price = price
        self.stock = stock_qty


class VendingFacade:
    '''Facade for vending machine sub processes'''    
    
    product_info_dict = {}

    def add_product_info(self, name, price, stock_qty=0):
        self.product_info_dict[name] = ProductInfo(name, price, stock_qty)


    def __init__(self):
        self.add_product_info('peppermint tea', 3.70, 5)
        self.add_product_info('bulgarian fruit cake', 1.90, 0)
        self.add_product_info('dairy milk', 1.20, 8)
        self.add_product_info('freddo', 0.10, 10)
        self.add_product_info('coffee', 3.20, 2)
        self.add_product_info('green tea', 2.60, 9)
        
        self.choice = ChoiceValidator()
        self.stock = Stock()
        self.dispenser = Dispenser()


    def add_stock(self, name, add_qty):
        for product_key, product_dict in self.product_info.items():
            if product_key == name:
                product_dict[self.stock] += add_qty

        print(f'{add_qty} added to {product_key}')


    def dispense_drink(self, product_choice):
        choice = self.choice.check_drink_choice(product_choice, product_info_dict)
        stock = self.stock.check_stock_level(product_choice, product_info_dict)

        if choice == True and stock > 0:
            self.dispenser.dispense()
            print('Dispensing complete. Enjoy your drink!')
            return True
        else:
            print(f'{product_choice.title()} is not available or out of stock...')
            return False

    

if __name__ == '__main__':
    
    #   User input and vending process
    
    product_choice = input('Please select your food or drink: ')
    vend = VendingFacade()
    vend.dispense_drink(product_choice.lower())

