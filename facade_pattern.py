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

    # TODO: Add index feature that locates item within the machine prior to dispensing.

class ProductInfo:
    '''Class representing product information for vendable products'''
    def __init__(self, name, price, stock_qty=0):
        self.name = name
        self.price = price
        self.stock = stock_qty

        # TODO: Add self.location attribute. Upon initialisation, next available location assigned.

    def __str__(self):
        return f"Name: {self.name.title()};  Price: £{self.price};  Stock QTY: {self.stock}"


class Engineer:
    '''Class representing the 'Engineer' for access to machine setting, maintenance and servicing'''
    def __init__(self, product_info_dict):
        self.product_info_dict = product_info_dict
    
    def diagnostic_check(self):
        print('\nRunning system diagnostic tests...')
        time.sleep(2)
        print('System check complete. No faults detected!')

    def add_product_info(self, name, price, stock_qty=0):
        '''Adds new product info to vending machine via ProductInfo'''
        self.product_info_dict[name] = ProductInfo(name, price, stock_qty)

    def delete_product_info(self, name):
        '''Adds new product info to vending machine via ProductInfo'''
        #self.product_info_dict[name] = ProductInfo(name, price, stock_qty)
        
    def modify_product_info(self, product_list):  
        product_choice = pyip.inputMenu(product_list, numbered=True, prompt="\nPlease select one of the following:\n")  
        product_attributes = ['Name', 'Price', 'Stock']

        prompt_1 = f"\nProduct selected: {product_choice.title()}\n"
        prompt_2 = "Please select the attribute to modify: \n"

        for product_key, product_info in self.product_info_dict.items():
            if product_key == product_choice.lower():
                attribute_choice = pyip.inputMenu(product_attributes, prompt=prompt_1 + prompt_2, numbered=True)  
                new_attribute_value = pyip.inputStr(f"\nEnter new {attribute_choice}: ")
                # product_info.attribute_choice = new_attribute_value # This isn't working. Wrong syntax.

    def modify_product_stock(self, product_list):     
        MAX_STOCK = 10
        product_choice = pyip.inputMenu(product_list, numbered=True)  

        for product_key, product_info in self.product_info_dict.items():
            if product_key == product_choice.lower():
                print(f"\nProduct: {product_key.title()}  --  Current stock: {product_info.stock}/{MAX_STOCK}")

                delta_stock = MAX_STOCK - product_info.stock
                restock_number = pyip.inputInt(min=0, max=delta_stock, prompt='Enter the quantity to add: ')
                product_info.stock += restock_number

                print(f"\n{restock_number} {product_key} successfully added to the vending machine...")
                print(f"New stock level: {product_info.stock}/{MAX_STOCK}")
        
        # Display existing stock level:   4/10 (10 max)
        # If user asked to add more than maximum stock - current stock: prompt to restock the difference
        # Display successful restock and confirm how many were added


class VendingFacade:
    '''Facade class for vending machine sub processes'''    
    MAX_PRODUCT_CAPACITY = 12
    MACHINE_IDS = []

    MAINTENANCE_PROMPTS = [
                        'Perform system check --->',
                        'Display machine information --->',
                        'Add new product --->',     
                        'Delete existing product --->',        
                        'Modify product information --->',  
                        'Modify stock level --->',          
                        'Exit maintenance mode --->',        
                        ]

    def __init__(self, type, default_products=dict()):
        self.id = self.assign_machine_id()
        self.type = type
        self.product_info_dict = dict()
        self.stock = Stock(self.product_info_dict)
        self.engineer = Engineer(self.product_info_dict)
        self.dispenser = Dispenser()

        if default_products:
            for product_key, product_info in default_products.items():
                self.engineer.add_product_info(product_info['name'], product_info['price'], product_info['stock_qty'])

    def __str__(self):
        line_1 = "\n--- MACHINE INFORMATION ---\n"
        line_2 = f"ID number: {self.id}\n"
        line_3 = f"Vendor type: {self.type.title()}\n"
        line_4 = f"Assigned slots: {len(self.product_info_dict.keys())}/{VendingFacade.MAX_PRODUCT_CAPACITY}"
        
        return line_1 + line_2 + line_3 + line_4

    def assign_machine_id(self):    
        if not VendingFacade.MACHINE_IDS:
            initial_machine_id = '1'
            VendingFacade.MACHINE_IDS.append(initial_machine_id)
            return initial_machine_id
        else:
            previous_machine_id = VendingFacade.MACHINE_IDS[-1]
            new_machine_id = str(int(previous_machine_id)+1)
            VendingFacade.MACHINE_IDS.append(new_machine_id)
            return new_machine_id

    def dispense_product(self, product_choice):
        '''Checks current stock level before dispensing product'''

        if self.stock.check_stock_level(product_choice) > 0:
            self.dispenser.dispense(product_choice)
            self.stock.remove_stock(product_choice) # Is this correct still?
            print(f'Dispensing complete. Enjoy your {product_choice}!')
            return True
        else:
            print(f'\n{product_choice.title()} is out of stock!')
            return False

    def engineer_mode(self):
        '''Takes engineer requirements'''
        print('\n-- Maintenance mode activated --\n')
        maintenance_menu_choice = pyip.inputMenu(VendingFacade.MAINTENANCE_PROMPTS, numbered=True)

        if maintenance_menu_choice == VendingFacade.MAINTENANCE_PROMPTS[0]:
            self.engineer.diagnostic_check()             

        elif maintenance_menu_choice == VendingFacade.MAINTENANCE_PROMPTS[1]:
            print(self.__str__())

        elif maintenance_menu_choice == VendingFacade.MAINTENANCE_PROMPTS[2]:
            print('\n-- Entering new product --')
            name = pyip.inputStr('Assign product name: ')
            price = pyip.inputFloat(prompt='Assign product price: ')
            stock_qty = pyip.inputInt(min=0, max=10, prompt='Enter initial stock level: ')
                    
            self.engineer.add_product_info(name, price, stock_qty)
            print(f"\n{name.title()} successfully added to vending machine!")

        elif maintenance_menu_choice == VendingFacade.MAINTENANCE_PROMPTS[3]:
            print('\n-- Product deletion --')
            product_list = get_product_list(machine_choice)
            name = pyip.inputMenu(product_list, numbered=True, prompt='Select item to be deleted:\n')
            self.engineer.delete_product_info(name)

        elif maintenance_menu_choice == VendingFacade.MAINTENANCE_PROMPTS[4]:
            product_list = get_product_list(machine_choice)
            self.engineer.modify_product_info(product_list)

        elif maintenance_menu_choice == VendingFacade.MAINTENANCE_PROMPTS[5]:
            product_list = get_product_list(machine_choice)
            self.engineer.modify_product_stock(product_list)

        elif maintenance_menu_choice == VendingFacade.MAINTENANCE_PROMPTS[6]:
            print('\n-- Maintenance mode deactivated --')
            
        #if not repeat_maintenance_process():
         
        #    maintenance_mode = False
        #    print('\n-- Maintenance mode deactivated --')



if __name__ == '__main__':

    vending_machine_1 = VendingFacade('food', DEFAULT_PRODUCTS_1)
    vending_machine_2 = VendingFacade('drink', DEFAULT_PRODUCTS_2)

    def vending_machine_pointer(machine_id):
        '''Takes the machine_id and returns a pointer to the correct machine object'''
        if machine_id == '1':
            pointer = vending_machine_1
        elif machine_id == '2':
            pointer = vending_machine_2
        else:
            pointer = None
        return pointer

    def get_product_list(machine_id):           
        '''Retrieves the most recent product list associated with the machine_id'''
        vending_machine = vending_machine_pointer(machine_id)
        product_list = []

        for product_key, product_info in vending_machine.product_info_dict.items():   
            product_list.append(product_key.title())
        return product_list

    def vending_process(machine_id):
        vending_machine_object= vending_machine_pointer(machine_id)
        product_list = get_product_list(machine_id)
        product_list.append('(( Enter maintenance mode ))')
        product_list.append('(( Exit vending process ))')
                
        while True:
            product_choice = pyip.inputMenu(product_list, numbered=True, prompt="\nPlease select one of the following:\n")
            
            if product_choice == '(( Enter maintenance mode ))':
                return 'maintenance'
            if product_choice == '(( Exit vending process ))':
                return False
            else:
                vending_machine_object.dispense_product(product_choice.lower())
                
    def terminate_program():
        user_input = pyip.inputYesNo(prompt="\nReturn to the vending machines (yes/no): ")  
        return True if user_input == 'no' else False

    def select_vending_machine():
        machine_string = ''
        for i in range(len(VendingFacade.MACHINE_IDS)):
            if i+1 < len(VendingFacade.MACHINE_IDS):
                machine_string += VendingFacade.MACHINE_IDS[i] + ', '
            if i+1 == len(VendingFacade.MACHINE_IDS):
                machine_string = machine_string[0:-2]
                machine_string += f" or {VendingFacade.MACHINE_IDS[i]}"
                                  
        machine_choice = pyip.inputChoice(VendingFacade.MACHINE_IDS, prompt=f"\nWhich vending machine do you wish to use? ({machine_string}): ")
        return machine_choice

    def repeat_maintenance_process():
        user_input = pyip.inputYesNo(prompt="\nStay in maintenance mode and perform another action (yes/no): ")  
        return False if user_input == 'no' else True


    # ------------------------------ TEST CASE ----------------------------------- #
    
    program_terminate = False
    maintenance_mode = False
    
    while program_terminate != True:

        machine_choice = select_vending_machine()      
        vending = vending_process(machine_choice)

        if vending == 'maintenance':

            vending_machine_object = vending_machine_pointer(machine_choice)
            vending_machine_object.engineer_mode()
        
        program_terminate = terminate_program()
