# Abstract Base Class
from abc import ABC, abstractmethod

class Product(ABC):
    def __init__(self, product_name):
        self.product_name = product_name

    @abstractmethod
    def consume(self):
        pass

# Create the subclass Drink
class Drink(Product):
    def consume(self):
        print(f"Yum, you drink the {self.product_name}.")

# Create the subclass Snack
class Snack(Product):
    def consume(self):
        print(f"Yum, you eat the {self.product_name}.")

# Create a subclass called EmptyProduct
class EmptyProduct(Product):
    def consume(self):
        print("Sorry, this product is empty.")

class Slot:
    def __init__(self, location, product_type, unit_price, stock):
        self.location = location
        self.product_type = product_type  # Drink, Snack, EmptyProduct ect.
        self.unit_price = unit_price
        self.stock = stock  # The number of products in the slot

    def sell(self):
        if self.stock > 0:
            product = self.product_type(self.product_type.__name__)  # Create a product of the given type
            print(f"Selling product from {self.location}...")
            product.consume()
            self.stock -= 1
            print(f"Remaining stock in {self.location}: {self.stock}")
        else:
            print(f"Sorry, no products left in slot {self.location}.")

class VendingMachine:
    def __init__(self):
        self.slots = {}  # Create a dictionary to store slots by their location

    def stock_item(self, location, product_type, unit_price, quantity):
        """Stock a product type in the given slot with price and quantity."""
        if location not in self.slots:
            self.slots[location] = Slot(location, product_type, unit_price, quantity)
        else:
            # If slot already exists, just increase stock
            self.slots[location].stock += quantity

    def print_inventory(self):
        """Print all slots with product type, quantity, and price."""
        print("Vending Machine Inventory:")
        for location, slot in self.slots.items():
            print(f"Slot {location}: {slot.stock} items of {slot.product_type.__name__} at ${slot.unit_price} each")

    def purchase(self, location, money):
        """Handle the purchase: return product and change or an empty product if unavailable."""
        if location not in self.slots:
            print(f"Slot {location} does not exist.")
            return EmptyProduct("Invalid Slot"), money  # Invalid location

        slot = self.slots[location]
        
        if slot.stock == 0:
            print(f"Sorry, no products left in slot {location}.")
            return EmptyProduct("Empty Slot"), money  # stock available

        if money < slot.unit_price:
            print(f"Sorry, you don't have enough money for {slot.product_type.__name__}.")
            return EmptyProduct("Insufficient Funds"), money  # Inform the user

        # processing the purchase and calculate change
        product = slot.product_type(slot.product_type.__name__)  # create the product
        change = money - slot.unit_price
        slot.stock -= 1
        print(f"Dispensing {product.product_name}... Change: ${change:.2f}")
        return product, change

# ===============main==============

machine = VendingMachine()

# Stocking items
machine.stock_item("A1", Drink, 1.50, 2)  # Get 2 Cokes in A1
machine.stock_item("B1", Snack, 2.00, 2)  # Get 2 Bags of Chips in B1

# Print inventory
machine.print_inventory()

# Buying something
product, change = machine.purchase("A1", 2.00)
print(f"Got {product.product_name}, change: ${change}")
product.consume()
