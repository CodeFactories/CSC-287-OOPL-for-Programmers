# Create a dictionary for storing attributes of a book, author, title, and price.
book1 = { "Autor: ", "Date: "
}

book2 = { "Autor: ", "Date: "
}

# Create a list of book
books = [book1, book2]

# function to calculate_total()
def calculate_total(books):
    total = sum(book["price"] for book in books)
    return total

# function to calculate_shipping()
def calculate_shipping(books, shipping_rate=5):
    """Calculate the total shipping cost based on weight."""
    total_weight = sum(book["weight"] for book in books)
    shipping_cost = total_weight * shipping_rate  # Assume $5 per kg
    return shipping_cost

# Prompt the user if they want to checkout. If they say yes,

# print out the total number of books and the final total price.

# Otherwise, print out “Come back soon!”


#////////////////////////////////////////////////
#///////////////////////////////////////////////

# Book dictionaries
book1 = {
    "author": "George Orwell",
    "title": "1984",
    "price": 12.99,
    "weight": 0.5
}

book2 = {
    "author": "Jane Austen",
    "title": "Pride and Prejudice",
    "price": 9.99,
    "weight": 0.4
}

# List of books
books = [book1, book2]

# Function to calculate total price
def calculate_total(books):
    return sum(book["price"] for book in books)

# Function to calculate shipping
def calculate_shipping(books, shipping_rate=5):
    total_weight = sum(book["weight"] for book in books)
    return total_weight * shipping_rate

# Prompt user
checkout = input("Do you want to checkout? (yes/no): ").lower()

if checkout == 'yes':
    total_books = len(books)
    total_price = calculate_total(books)
    shipping = calculate_shipping(books)
    final_price = total_price + shipping

    print(f"\nYou have {total_books} books.")
    print(f"Books total: ${total_price:.2f}")
    print(f"Shipping: ${shipping:.2f}")
    print(f"Final total: ${final_price:.2f}")
else:
    print("Come back soon!")
