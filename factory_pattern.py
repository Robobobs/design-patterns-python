'''Example script showcasing the factory design pattern for a generic Product'''

from abc import ABCMeta, abstractmethod
import pyinputplus as pyip

class IProduct(metaclass=ABCMeta):      # Abstract classes cannot be instantiated.
    '''Defines abstract Product class'''

    @staticmethod                       # Removes need for 'self' argument. Self not needed as method is not implemented.
    @abstractmethod                     # Ensures the inheriting class must override this method during instantiation.
    def product_method():               # Defined common interface method.
        '''Static interface method only'''


class ProductA(IProduct):
    '''Class for Product A'''
    def __init__(self):
        self.name = 'Product A'
        self.description = f'{self.name} is a small product'

    def product_method(self):
        return 'Generic method call for Product A'

class ProductB(IProduct):
    '''Class for Product B'''
    def __init__(self):
        self.name = 'Product B'
        self.description = f'{self.name} is a medium product'

    def product_method(self):
        return 'Generic method call for Product B'

class ProductC(IProduct):
    '''Class for Product C'''
    def __init__(self):
        self.name = 'Product C'
        self.description = f'{self.name} is a large product'

    def product_method(self):
        return 'Generic method call for Product C'


class ProductFactory:
    '''Product factory class'''
    
    def new_product(self, user_input):
        '''Defines a new product via argument(user_input)'''
        if user_input == 'A':
            return ProductA()
        elif user_input == 'B':
            return ProductB()
        elif user_input == 'C':
            return ProductC()
        else:
            print('\nERROR: Invalid product type!')
            return None
  

if __name__ == "__main__":
    
    products = ['A', 'B', 'C']
    user_input = pyip.inputChoice(products, prompt = 'Choose a product type (A, B or C): ')
    product1 = ProductFactory().new_product(user_input.upper())
    
    # ------------------------------ TEST CASE ----------------------------------- #
    try:
        print(f"\nName: {product1.name}")
        print(f"Description: {product1.description}")
        print(product1.product_method())

    except AttributeError:
        print('Product attribute or method not found...')
