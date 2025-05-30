from Product import Product

class Drink(Product):
    def __init__(self, name, price, volume):
        super().__init__(name, price)
        self.__volume = volume

    def get_volume(self):
        return self.__volume

    def set_volume(self, volume):
        if volume <= 0:
            raise ValueError("Volume must be positive")
        self.__volume = volume

    def display_info(self):
        product_info = super().display_info()
        return f"{product_info}Volume: {self.__volume}ml"
