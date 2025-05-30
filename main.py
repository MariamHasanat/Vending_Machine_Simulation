from Product import Product
from Snack import Snack
from Drink import Drink
from Candy import Candy

if __name__ == "__main__":
    # create a list of products 
    products = []
    # open the file in read mode 
    with open("products.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            data = line.strip().split(",")
            if data[0] == "Snack":
                product = Snack(data[1], float(data[2]), float(data[3]))
                products.append(product)
            elif data[0] == "Drink":
                product = Drink(data[1], float(data[2]), float(data[3]))
                products.append(product)
            elif data[0] == "Candy":
                product = Candy(data[1], float(data[2]), data[3])
                products.append(product)

# show a menu based on the loaded products 
    print("Welcome to the Python Vending Machine!\n\nPlease select what you want:")
    for i, product in enumerate(products, start=1):
        print(f"{i}. {type(product).__name__} - {product.get_name()}")
    
    choice = int(input("\n> "))
    if 1 <= choice <= len(products):
        selected_product = products[choice - 1]
        print(f"Product Information:\n{selected_product.display_info()}")
    else:
        print("Invalid choice. Please try again.")