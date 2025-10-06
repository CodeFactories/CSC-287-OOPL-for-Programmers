# This create a list and Square elements of the list.

#initializing a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for item in numbers:
    print(item*item, end=" ") # or print(item**2, end=" ")

# Create a list of 100 numbers
num_range = list(range(1, 101))
# print(num_range)

squared_num = [num*num for num in num_range]
# print the square of the first 100 numbers in num_range
print(f" Print the square of 1 to 100, {squared_num}")

# Get the first 20 numbers using list slicing
num_range = list(range(1, 101))[0:20]

# Square of squares
squared_of_squares = [num**2 * num**2 for num in num_range]

# Print the square of squares of the first 20 numbers
print( f" Print the square of squares {squared_of_squares}" )


# Exercise #3.5: List Comprehension