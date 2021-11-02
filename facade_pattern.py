'''Example script showcasing the Facade design pattern via a vending machine process'''

import time

class CheckDrinkChoice:
    '''Checks if drink selection is available'''
    def check_drink_choice(self, drink_choice, drinks):
        if drink_choice in drinks.keys():
            return True
        else:
            False 
   

class CheckStock:
    '''Checks if drink selection is in stock'''
    def check_stock_level(self, drink_choice, drinks):     
        for drink, stock_num in drinks.items():
            if drink == drink_choice:
                return stock_num
        return False            

    
class Dispense:
    '''Initiates physical vending (activates dispensing pump)'''    
    def dispense(self):
        print('Dispensing drink...')
        time.sleep(3)
        

class VendingFacade:
    '''Facade for vending machine sub processes'''    
    def __init__(self):
        self.choice = CheckDrinkChoice()
        self.stock = CheckStock()
        self.dispense = Dispense()

    def dispense_drink(self, drink_choice, drinks):
        choice = self.choice.check_drink_choice(drink_choice, drinks)
        stock = self.stock.check_stock_level(drink_choice, drinks)

        if choice == True and stock > 0:
            self.dispense.dispense()
            print('Dispensing complete. Enjoy your drink!')
        else:
            print(f'{drink_choice.title()} is not available or out of stock...')
            return None


if __name__ == '__main__':
    
    #   Client specific drinks incl. stock values
    drinks = {
            'peppermint tea': 5,
            'coffee': 2,
            'black tea': 10,
            'green tea': 0,
            'macha': 7,
            }

    #   User input and vending process
    drink_choice = input('Select your drink: ')
    vend = VendingFacade()
    vend.dispense_drink(drink_choice.lower(), drinks)
    
