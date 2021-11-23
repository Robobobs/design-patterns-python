'''Example script showcasing the Facade design pattern via a vending machine process'''

import time
import pyinputplus as pyip

DEFAULT_PRODUCTS_1 = {
                    'peppermint tea': {
                                        'name': 'peppermint tea',
                                        'price': 3.70,
                                        'stock_qty': 5
                                        },
                    'bulgarian kozunak':{
                                        'name': 'bulgarian kozunak',
                                        'price': 1.90,
                                        'stock_qty': 0
                                        },
                    'dairy milk': {
                                        'name': 'dairy milk',
                                        'price': 1.20,
                                        'stock_qty': 8
                                        },
                    'freddo': {
                                        'name': 'freddo',
                                        'price': 0.10,
                                        'stock_qty': 10
                                        },
                    'coffee': {
                                        'name': 'coffee',
                                        'price': 3.20,
                                        'stock_qty': 2
                                        },
                    'green tea': {
                                        'name': 'green tea',
                                        'price': 2.60,
                                        'stock_qty': 9},
                    }

DEFAULT_PRODUCTS_2 = {
                    'mint tea': {
                                    'name': 'mint tea',
                                    'price': 1.70,
                                    'stock_qty': 8
                                    },
                    'big bulgarian lukanka':{
                                    'name': 'big bulgarian lukanka',
                                    'price': 9.90,
                                    'stock_qty': 1
                                    },
                    'fruit pastels': {
                                    'name': 'fruit pastels',
                                    'price': 2.20,
                                    'stock_qty': 4
                                    },
                    'trebor mints': {
                                    'name': 'trebor mints',
                                    'price': 1.10,
                                    'stock_qty': 3
                                    },
                    'coffee': {
                                    'name': 'latte',
                                    'price': 3.05,
                                    'stock_qty': 1
                                    },
                    'macha tea': {
                                    'name': 'macha tea',
                                    'price': 3.60,
                                    'stock_qty': 2
                                    },
                    }

class Stock:
    '''Class representing Stock levels for vendable products'''
    def __init__(self, product_info_dict):
        self.product_info_dict = product_info_dict
    
    def check_stock_level(self, product_choice):     
        '''Checks current stock quantity of specific product'''
        for product_key, product_info in self.product_info_dict.items():
            if product_key == product_choice:
                return product_info.stock
        return False

    def add_stock(self, product_choice, add_qty):
        '''Adds quantity to existing product stock'''
        for product_key, product_info in self.product_info_dict.items():
            if product_key == product_choice:
                product_info.stock += add_qty

    def remove_stock(self, product_choice, remove_qty=1):
        '''Removes quantity from existing product stock'''
        for product_key, product_info in self.product_info_dict.items():
            if product_key == product_choice:
                product_info.stock -= remove_qty


class Dispenser:
    '''Initiates physical vending (activates dispensing process)'''    
    def dispense(self, product_choice):
        print(f"\nDispensing {product_choice}...")
        time.sleep(2)


class ProductInfo:
    '''Class representing product information for vendable products'''
    def __init__(self, name, price, stock_qty=0):
        self.name = name
        self.price = price
        self.stock = stock_qty

    def __str__(self):
        return f"Name: {self.name.title()};  Price: £{self.price};  Stock QTY: {self.stock}"


class Engineer:
    '''Class representing 'Engineer Mode' for machine maintenance'''
    def __init__(self, product_info_dict):
        self.product_info_dict = product_info_dict
    
    def system_check(self):
        print('\nRunning system check...')
        time.sleep(2)
        print('System check complete. No faults detected!\n')

    def add_product_info(self, name, price, stock_qty=0):
        '''Adds new product info to vending machine via ProductInfo'''
        self.product_info_dict[name] = ProductInfo(name, price, stock_qty)
        
    def modify_product_info(self, product_list):  
        product_choice = pyip.inputMenu(product_list, numbered=True)  
        product_attributes = ['name', 'price', 'stock']

        for product_key, product_info in self.product_info_dict.items():
            if product_key == product_choice.lower():
                attribute_choice = pyip.inputMenu(product_attributes, prompt="Please select the attribute to modify: \n", numbered=True)  
                new_attribute_value = input(f"Enter new {attribute_choice}: ")
                product_info.attribute_choice = new_attribute_value

    def modify_product_stock(self, product_list):     
        MAX_STOCK = 10
        product_choice = pyip.inputMenu(product_list, numbered=True)  

        for product_key, product_info in self.product_info_dict.items():
            if product_key == product_choice.lower():
                print(f"\nProduct: {product_key.title()}  --  Current stock: {product_info.stock}/{MAX_STOCK}")

                delta_stock = MAX_STOCK - product_info.stock
                restock_number = pyip.inputInt(min=0, max=delta_stock, prompt = 'Enter the quantity to add: ')
                product_info.stock += restock_number

                print(f"\n{restock_number} {product_key} successfully added to the vending machine...")
                print(f"New stock level: {product_info.stock}/{MAX_STOCK}")
        
        # Display existing stock level:   4/10 (10 max)
        # If user asked to add more than maximum stock - current stock: prompt to restock the difference
        # Display successful restock and confirm how many were added


class VendingFacade:
    '''Facade class for vending machine sub processes'''    
    def __init__(self, default_products=dict()):
        self.product_info_dict = dict() #   Dictionary of vendable products
        self.stock = Stock(self.product_info_dict)
        self.dispenser = Dispenser()
        self.engineer = Engineer(self.product_info_dict)

        if default_products:
            for product_key, product_info in default_products.items():
                self.engineer.add_product_info(product_info['name'], product_info['price'], product_info['stock_qty'])
    
    def dispense_product(self, product_choice):
        '''Checks current stock level before dispensing product'''

        if self.stock.check_stock_level(product_choice) > 0:
            self.dispenser.dispense(product_choice)
            self.stock.remove_stock(product_choice)
            print(f'Dispensing complete. Enjoy your {product_choice}!')
            return True
        else:
            print(f'\n{product_choice.title()} is out of stock...')
            return False


if __name__ == '__main__':

    vending_machine_1 = VendingFacade(DEFAULT_PRODUCTS_1)
    vending_machine_2 = VendingFacade(DEFAULT_PRODUCTS_2)
   
    machine_list = [
                    '1',    # vending_machine_1
                    '2',    # vending_machine_2
                    'm'     # maintenance mode placeholder
                    ]

    maintenance_prompt = [
                        'Perform system check --->',
                        'Add new product --->',             
                        'Modify product information --->',  
                        'Modify stock level --->',          
                        'Exit maintenance mode --->',        
                        ]
    
    def machine_pointer(vending_machine_id):
        if vending_machine_id == '1':
            pointer = vending_machine_1
        elif vending_machine_id == '2':
            pointer = vending_machine_2
        return pointer

    def get_product_list(vending_machine_id):           
        product_list = []
        vending_machine = machine_pointer(vending_machine_id)

        for product_key, product_info in vending_machine.product_info_dict.items():   
            product_list.append(product_key.title())
        return product_list

    def vending_process(vending_machine_id):
        product_list = get_product_list(vending_machine_id)
        vending_machine = machine_pointer(vending_machine_id)
        product_choice = pyip.inputMenu(product_list, numbered=True)
        vending_machine.dispense_product(product_choice.lower())

    def repeat_vending_process():
        user_input = pyip.inputYesNo(prompt = "\nReturn to the vending machines (yes or no): ")  
        return False if user_input == 'no' else True

    def repeat_maintenance_process():
        user_input = pyip.inputYesNo(prompt = "\nStay in maintenance mode and perform another action (yes or no): ")  
        return False if user_input == 'no' else True


    # ------------------------------ TEST CASE ----------------------------------- #
    #   Vending loop: including user input, initiation of vending process and maintenance access
    maintenance_mode = False
    repeat_flag = True

    while repeat_flag == True:

        prompt_1 = "\nWhich vending machine do you wish to use? (1 or 2)"
        prompt_2 = "\nEnter 'm' to access maintenance mode: "
        machine_choice = pyip.inputChoice(machine_list, prompt = prompt_1 + prompt_2)
            
        if machine_choice != 'm':
            vending_process(machine_choice) 
        else:
            maintenance_mode = True
            print('\n-- Maintenance mode activated --\n')
            
            while maintenance_mode == True:
                maintenance_menu_choice = pyip.inputMenu(maintenance_prompt, numbered=True)

                if maintenance_menu_choice == maintenance_prompt[4]:
                    print('\n-- Maintenance mode deactivated --')
                    break
                
                elif maintenance_menu_choice == maintenance_prompt[0]:
                    vending_machine_1.engineer.system_check()             

                elif maintenance_menu_choice == maintenance_prompt[1]:
                    name = input('Enter new product name: ')
                    price = pyip.inputFloat(prompt='Price: ')
                    stock_qty = pyip.inputInt(prompt='Initial stock level: ', min=0, max=10)
                    
                    vending_machine_1.engineer.add_product_info(name, price, stock_qty)
                    print(f"\n{name.title()} successfully added to vending machine...")

                elif maintenance_menu_choice == maintenance_prompt[2]:
                    product_list = get_product_list(machine_choice)
                    vending_machine_1.engineer.modify_product_info(product_list)

                elif maintenance_menu_choice == maintenance_prompt[3]:
                    product_list = get_product_list(machine_choice)
                    vending_machine_1.engineer.modify_product_stock(product_list)

                if not repeat_maintenance_process():
                    maintenance_mode = False
                    print('\n-- Maintenance mode deactivated --')

        if not repeat_vending_process():
            repeat_flag = False





    #vending_machine_1.maintenance.system_check():
    #print('Reboot required - system rebooting...')

    #   Adding new product to vending machine and printing all product information
    #vending_machine_1.add_product_info('snickers', 2.30, 9)
    #print('\n--- Product Information ---')
    #for product_name, product_info in vending_machine_1.product_info_dict.items():
    #    print(product_info.__str__()) # Note: Last product now 'Snickers'
    
    #   Updating existing product stock and printing all product information
    #vending_machine_1.add_stock('bulgarian kozunak', 5)
    #print('\n--- Product Information ---')
    #for product_name, product_info in vending_machine_1.product_info_dict.items():
    #    print(product_info.__str__()) # Note: 'Stock QTY' increased from 0 to 5