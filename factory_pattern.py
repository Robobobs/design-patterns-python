'''example script showcasing the factory design pattern'''

from abc import ABCMeta, abstractmethod


# TODO: create client code to call factory method (if __name__ == __main__ implementation?)

# TODO: create IClass that inherets from abstract class

class IProduct(Metaclass=ABCMeta):
    '''abstract product class'''

    @staticmethod
    @abstractmethod
    def

# TODO: create factory creator class that takes identifiers, and whose method determines 
#       which concrete product class to return

class ProductFactory:
    '''product factory class'''

    def new_product(self, id_1, id_2):


# TODO: create concrete product classes that inheret from IClass and return class object

class ProductA(IProduct):


Maybe:
Create a factory for scaling existing object (product). Product attributes can include scale ratio 2:1, name, dimensions etc.