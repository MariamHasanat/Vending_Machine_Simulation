class Product:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price  
    
    def get_name(self):
        return self.__name
    
    def display_info(self):
        return f"Product Name: {self.__name}, Price: ${self.__price:.2f}\n"