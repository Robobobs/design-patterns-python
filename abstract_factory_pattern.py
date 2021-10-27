'''Example script showcasing the abstract factory design pattern for a generic Product'''

from abc import ABCMeta, abstractmethod
import pyinputplus as pyip

#   Abstract factory class interface
class IProductFactory(metaclass=ABCMeta):
    '''Defines abstract Product Factory class'''

    @staticmethod
    @abstractmethod
    def get_product_factory():
        '''Static interface method only'''


#   Factory creator classes
class NewProductFactory(IProductFactory):
    '''Product factory class for choosing product type'''

    def get_product_factory(self, catagory, product_type):
        '''Defines a new product from product catagory and type'''
        if catagory == 'A':
            return ProductFactoryA().get_type(product_type)
        elif catagory == 'B':
            return ProductFactoryB().get_type(product_type)
        elif catagory == 'C':
            return ProductFactoryC().get_type(product_type)
        else:
            print('\nERROR: Invalid product type!')
            return None


#   Abstract product class interface
class IProduct(metaclass=ABCMeta):
    '''Defines abstract class for Product Factories'''

    @staticmethod
    @abstractmethod
    def get_type():
        '''Static interface method only'''


#   Factory creator classes for Products
class ProductFactoryA(IProduct):
    '''Product factory class for Product A'''

    def get_type(self, product_type):
        '''Product type selector'''
        if product_type == '1':
            return ProductA1()
        elif product_type == '2':
            return ProductA2()
        elif product_type == '3':
            return ProductA3()
        else:
            print('\nERROR: Product type not valid for Product A!')


class ProductFactoryB(IProduct):
    '''Product factory class for Product B'''

    def get_type(self, product_type):
        '''Product type selector'''
        if product_type == '1':
            return ProductB1()
        elif product_type == '2':
            return ProductB2()
        elif product_type == '3':
            return ProductB3()
        else:
            print('\nERROR: Product type not valid for Product B!')


class ProductFactoryC(IProduct):
    '''Product factory class for Product C'''

    def get_type(self, product_type):
        '''Product type selector'''
        if product_type == '1':
            return ProductC1()
        elif product_type == '2':
            return ProductC2()
        elif product_type == '3':
            return ProductC3()
        else:
            print('\nERROR: Product type not valid for Product C!')


#   Individual product classes: A1 - C3
class ProductA1:
    '''Class for Product A'''
    def __init__(self):
        self.name = 'Product A'
        self.description = f"{self.name} is a small product"

    def product_method(self):
        return 'Generic method call for Product A1'

class ProductA2:
    '''Class for Product A'''
    def __init__(self):
        self.name = 'Product A2'
        self.description = f"{self.name} is a medium product"

    def product_method(self):
        return 'Generic method call for Product A2'

class ProductA3:
    '''Class for Product A'''
    def __init__(self):
        self.name = 'Product A3'
        self.description = f"{self.name} is a large product"

    def product_method(self):
        return 'Generic method call for Product A3'


class ProductB1:
    '''Class for Product B'''
    def __init__(self):
        self.name = 'Product B'
        self.description = f"{self.name} is a small product"
        
    def product_method(self):
        return 'Generic method call for Product B1'

class ProductB2:
    '''Class for Product B'''
    def __init__(self):
        self.name = 'Product B2'
        self.description = f"{self.name} is a medium product"

    def product_method(self):
        return 'Generic method call for Product B2'

class ProductB3:
    '''Class for Product B'''
    def __init__(self):
        self.name = 'Product B3'
        self.description = f"{self.name} is a large product"

    def product_method(self):
        return 'Generic method call for Product B3'


class ProductC1:
    '''Class for Product C'''
    def __init__(self):
        self.name = 'Product C'
        self.description = f"{self.name} is a small product"

    def product_method(self):
        return 'Generic method call for Product C1'

class ProductC2:
    '''Class for Product C'''
    def __init__(self):
        self.name = 'Product C2'
        self.description = f"{self.name} is a medium product"

    def product_method(self):
        return 'Generic method call for Product C2'

class ProductC3:
    '''Class for Product C'''
    def __init__(self):
        self.name = 'Product C3'
        self.description = f"{self.name} is a large product"

    def product_method(self):
        return 'Generic method call for Product C3'



if __name__ == "__main__":
    
    product_catagories = ['A', 'B', 'C']
    product_types = ['1', '2', '3']
    
    #    Prompt for user inputs
    catagory = pyip.inputChoice(product_catagories, prompt = 'Choose a product catagory (A, B or C): ')
    product_type = pyip.inputChoice(product_types, prompt = 'Choose a product type (1, 2 or 3): ')

    product1 = NewProductFactory().get_product_factory(catagory.upper(), product_type)
    
   
    # ------------------------------ TEST CASE ----------------------------------- #
    try:
        print(f"\nName: {product1.name}")
        print(f"Description: {product1.description}")
        print(f"Class: {product1.__class__}")
        print(product1.product_method())

    except AttributeError:
        print('Product attribute or method not found...')


