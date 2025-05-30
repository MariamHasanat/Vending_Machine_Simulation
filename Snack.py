from Product import Product
class Snack(Product):
    def __init__(self, name, price, calories):
        super().__init__(name, price)
        self.__calories = calories

    def get_calories(self):
        return self.__calories

    def set_calories(self, calories):
        if calories <= 0:
            raise ValueError("Calories must be positive")
        self.__calories = calories

    def display_info(self):
        product_info = super().display_info()
        return f"{product_info}, Calories: {self.__calories}kcal"