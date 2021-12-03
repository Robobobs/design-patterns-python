'''Example script showcasing the Facade design pattern via a vending machine process'''

import time
import pyinputplus as pyip

DEFAULT_FOOD_PRODUCTS_1 = {
                    'bulgarian kozunak':{
                                        'name': 'bulgarian kozunak',
                                        'price': 1.90,
                                        'stock_qty': 2
                                        },
                    'dairy milk': {
                                        'name': 'dairy milk',
                                        'price': 1.20,
                                        'stock_qty': 4
                                        },
                    'freddo': {
                                        'name': 'freddo',
                                        'price': 0.10,
                                        'stock_qty': 3
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
                                        'stock_qty': 6
                                        },
                    'snickers': {
                                        'name': 'snickers',
                                        'price': 2.10,
                                        'stock_qty': 2
                                        },
                    }

DEFAULT_DRINK_PRODUCTS_1 = {
                    'mint tea': {
                                    'name': 'mint tea',
                                    'price': 1.70,
                                    'stock_qty': 3
                                    },
                    'americano': {
                                    'name': 'americano',
                                    'price': 3.05,
                                    'stock_qty': 1
                                    },
                    'macha tea': {
                                    'name': 'macha tea',
                                    'price': 3.60,
                                    'stock_qty': 2
                                    },
                    'peppermint tea': {
                                    'name': 'peppermint tea',
                                    'price': 3.70,
                                    'stock_qty': 5
                                    },
                    'green tea': {
                                    'name': 'green tea',
                                    'price': 2.60,
                                    'stock_qty': 3
                                    },
                    'latte': {
                                    'name': 'latte',
                                    'price': 3.55,
                                    'stock_qty': 2
                                    },
                    'hot water': {
                                    'name': 'hot water',
                                    'price': 0.20,
                                    'stock_qty': 5
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

        # TODO: Add self.index attribute. Upon initialisation, next available index assigned.

    def __str__(self):
        return f"Name: {self.name.title()};  Price: £{self.price};  Stock QTY: {self.stock}"

class Engineer:
    '''Class representing the 'Service Engineer' for access to machine setting, maintenance and servicing'''
    def __init__(self, product_info_dict):
        self.product_info_dict = product_info_dict
    
    def get_product_list(self):           
        '''Retrieves the most recent product list associated with the machine_id'''
        product_list = []

        for product_key, product_info in self.product_info_dict.items():   
            product_list.append(product_key.title())
        return product_list

    def diagnostic_check(self):
        print('\nRunning system diagnostic tests...')
        time.sleep(2)
        print('System check complete. No faults detected!')
        time.sleep(2)

    def add_product_info(self, name=str(), price=float(), stock_qty=int()):
        '''Adds new product info to vending machine as ProductInfo object'''
        if name != '':
            self.product_info_dict[name] = ProductInfo(name, price, stock_qty)
        else:
            print('\n||--- New Product ---||')
            name = pyip.inputStr('Assign product name: ')
            price = pyip.inputFloat(prompt='Assign product price: ')
            stock_qty = pyip.inputInt(min=0, max=10, prompt='Enter initial stock level: ')
            
            self.product_info_dict[name] = ProductInfo(name, price, stock_qty)
            print(f"\n{name.title()} successfully added to the vending machine!")

    def delete_product_info(self):
        '''Deletes product info from vending machine'''
        product_list = self.get_product_list()
        product_list.append('Exit deletion process --->') 
        
        print('\n||--- Delete Product ---||')
        prompt_1 = 'Select item to be deleted:\n'
        selected_product = pyip.inputMenu(product_list, numbered=True, prompt=prompt_1)
                
        if selected_product in product_list[0:-1]:
            prompt_2 = f"\nAre you sure you want to delete {selected_product.lower()} (yes/no): "
            deletion_check = pyip.inputYesNo(prompt=prompt_2)
            if deletion_check == 'yes':
                del self.product_info_dict[selected_product.lower()]
                print(f"\n{selected_product.title()} deleted!")
                time.sleep(1)
            else:
                print(f"\n{selected_product.title()} not deleted!")
                time.sleep(1)

    def modify_product_info(self):  
        print('\n||--- Product Modification ---||')
        
        product_list = self.get_product_list()
        product_list.append('Exit modify process --->')
        
        prompt_1 = "Select one of the following products to modify:\n"
        product_choice = pyip.inputMenu(product_list, numbered=True, prompt=prompt_1)  
        
        product_attributes = [
                            'Name',
                            'Price',
                            ]
        product_attributes.append('Display product info --->')
        product_attributes.append('Exit modify process --->')
        
        if product_choice != 'Exit modify process --->':           
            REPEAT_FLAG = True

            while REPEAT_FLAG:                                
                for product_key, product_info in self.product_info_dict.items():
                    if product_key == product_choice.lower():
                        prompt_2 = "\nPlease select the attribute to modify: \n"
                        attribute_choice = pyip.inputMenu(product_attributes, prompt=prompt_2, numbered=True)  
                        
                        if attribute_choice not in product_attributes[-2:]: 
                            new_attribute_value = pyip.inputStr(f"\nEnter new {attribute_choice.lower()}: ")
                            
                            if attribute_choice == product_attributes[0]:
                                name, price, stock = new_attribute_value.lower(), product_info.price, product_info.stock                              
                                del self.product_info_dict[product_key]
                                self.add_product_info(name, price, stock)
                                return
                            elif attribute_choice == product_attributes[1]:
                                product_info.price = float(new_attribute_value)
                                return
                            
                        elif attribute_choice == product_attributes[-2]:
                            print('\n||--- Product Information ---||')
                            print(product_info.__str__())
                        
                        elif attribute_choice == product_attributes[-1]:
                            REPEAT_FLAG = False
                            break
                   
    def modify_product_stock(self):     
        '''Modifies existing product stock level'''
        product_list = self.get_product_list()
        product_list.append('Exit stock modification process --->')
        
        prompt = "\nPlease select one of the following:\n"
        product_choice = pyip.inputMenu(product_list, numbered=True, prompt=prompt)  

        for product_key, product_info in self.product_info_dict.items():
            if product_key == product_choice.lower():
                print(f"\nProduct: {product_key.title()}  --  Current stock: {product_info.stock}/{VendingFacade.MAX_SLOT_CAPACITY}")

                delta_stock = VendingFacade.MAX_SLOT_CAPACITY - product_info.stock
                restock_number = pyip.inputInt(min=0, max=delta_stock, prompt='Enter the quantity to add: ')
                product_info.stock += restock_number

                print(f"\n{restock_number} {product_key} successfully added to the vending machine...")
                print(f"New stock level: {product_info.stock}/{VendingFacade.MAX_SLOT_CAPACITY}")
                time.sleep(2)
    
class VendingFacade:
    '''Facade class for vending machine sub processes'''    
    MAX_PRODUCT_CAPACITY = 12
    MAX_SLOT_CAPACITY = 10
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

    def __init__(self, vendor_type, default_products=dict()):
        self.id = self.assign_machine_id()
        self.type = vendor_type
        self.product_info_dict = dict()
        self.stock = Stock(self.product_info_dict)
        self.engineer = Engineer(self.product_info_dict)
        self.dispenser = Dispenser()

        if default_products:
            for product_key, product_info in default_products.items():
                self.engineer.add_product_info(product_info['name'], product_info['price'], product_info['stock_qty'])

    def __str__(self):
        '''Returns a string containing machine information specific to each instance'''
        line_1 = "\n||--- Machine Information ---||\n"
        line_2 = f"ID number: {self.id}\n"
        line_3 = f"Vendor type: {self.type.title()}\n"
        line_4 = f"Assigned slots: {len(self.product_info_dict.keys())}/{VendingFacade.MAX_PRODUCT_CAPACITY}"
        return line_1 + line_2 + line_3 + line_4

    def assign_machine_id(self):    
        '''Assigns a new, chronological machine ID for each instance of VendingFacade'''
        if not VendingFacade.MACHINE_IDS:
            initial_machine_id = '1'
            VendingFacade.MACHINE_IDS.append(initial_machine_id)
            return initial_machine_id
        else:
            previous_machine_id = VendingFacade.MACHINE_IDS[-1]
            new_machine_id = str(int(previous_machine_id)+1)
            VendingFacade.MACHINE_IDS.append(new_machine_id)
            return new_machine_id

    def initiate_vending_process(self):         
        while True:
            product_list = self.engineer.get_product_list()
            product_list.append('Enter maintenance mode --->')
            product_list.append('Exit vending process --->')
            
            prompt = "\nPlease select one of the following products/options:\n"
            user_choice = pyip.inputMenu(product_list, numbered=True, prompt=prompt)
            
            if user_choice == 'Enter maintenance mode --->':
                self.maintenance_access()
            elif user_choice == 'Exit vending process --->':
                return
            else:
                self.dispense_product(user_choice.lower())

                # TODO: If self.dispense_product returns 'None', add product to list for restocking and notify control
                #       Note: Utilise observer pattern for notification of Subject change.
                
            user_input = pyip.inputYesNo(prompt="\nWould you like another product (yes/no): ")  
            if user_input == 'no':
                return
    
    def dispense_product(self, product_choice):
        '''Checks current stock level before dispensing product'''
        if self.stock.check_stock_level(product_choice) > 0:
            self.dispenser.dispense(product_choice)
            self.stock.remove_stock(product_choice)
            print(f'Dispensing complete. Enjoy your {product_choice}!')
        else:
            print(f'\n{product_choice.title()} is out of stock!')
            return None

    def maintenance_access(self):
        '''Processes maintenance requirements and provides access to Engineer subprocesses'''
        print('\n||--- MAINTENANCE MODE ACTIVATED ---||')
        
        while True:
            prompt = "\nPlease select one of the following options:\n"
            maintenance_menu_choice = pyip.inputMenu(VendingFacade.MAINTENANCE_PROMPTS, numbered=True, prompt=prompt)

            if maintenance_menu_choice == VendingFacade.MAINTENANCE_PROMPTS[0]:
                self.engineer.diagnostic_check()             

            elif maintenance_menu_choice == VendingFacade.MAINTENANCE_PROMPTS[1]:
                print(self.__str__())

            elif maintenance_menu_choice == VendingFacade.MAINTENANCE_PROMPTS[2]:     
                self.engineer.add_product_info()
                
            elif maintenance_menu_choice == VendingFacade.MAINTENANCE_PROMPTS[3]:
                self.engineer.delete_product_info()
                
            elif maintenance_menu_choice == VendingFacade.MAINTENANCE_PROMPTS[4]:
                self.engineer.modify_product_info()

            elif maintenance_menu_choice == VendingFacade.MAINTENANCE_PROMPTS[5]:
                self.engineer.modify_product_stock()
                
            elif maintenance_menu_choice == VendingFacade.MAINTENANCE_PROMPTS[6]:
                break
        
        print('\n||--- MAINTENANCE MODE DEACTIVATED ---||')


if __name__ == '__main__':

    def select_vending_machine():
        '''Customises user prompt to include all instantiated vending machines as per their machine ID'''
        machine_string = ''
        for i in range(len(VendingFacade.MACHINE_IDS)):
            if i+1 < len(VendingFacade.MACHINE_IDS):
                machine_string += VendingFacade.MACHINE_IDS[i] + ', '
            if i+1 == len(VendingFacade.MACHINE_IDS):
                machine_string = machine_string[0:-2]
                machine_string += f" or {VendingFacade.MACHINE_IDS[i]}"

        prompt = f"\nWhich vending machine do you wish to use? ({machine_string}): "                          
        machine_choice = pyip.inputChoice(VendingFacade.MACHINE_IDS, prompt=prompt)
        return machine_choice

    def machine_pointer(machine_id):
        '''Takes the machine_id and returns a pointer to the correct machine object'''
        if machine_id == '1':
            pointer = vending_machine_1
        elif machine_id == '2':
            pointer = vending_machine_2
        else:
            pointer = None
        return pointer

    def terminate_program():
        user_input = pyip.inputYesNo(prompt="\nReturn to the vending machines (yes/no): ")  
        return True if user_input == 'no' else False

    # ------------------------------ TEST CASE ----------------------------------- #
    
    vending_machine_1 = VendingFacade('food', DEFAULT_FOOD_PRODUCTS_1)
    vending_machine_2 = VendingFacade('drink', DEFAULT_DRINK_PRODUCTS_1)

    PROGRAM_TERMINATE = False
    
    while PROGRAM_TERMINATE != True:

        machine_choice = select_vending_machine()      
        vending_machine_object = machine_pointer(machine_choice)
        vending_machine_object.initiate_vending_process()
        
        PROGRAM_TERMINATE = terminate_program()
