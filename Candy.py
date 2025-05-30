from Product import Product
class Candy(Product):
    def __init__(self, name, price, flavor):
        super().__init__(name, price)
        self.__flavor = flavor

    def get_flavor(self):
        return self.__flavor

    def set_flavor(self, flavor):
        if not flavor:
            raise ValueError("Flavor cannot be empty")
        self.__flavor = flavor

    def display_info(self):
        product_info = super().display_info()
        return f"{product_info}Flavor: {self.__flavor}"