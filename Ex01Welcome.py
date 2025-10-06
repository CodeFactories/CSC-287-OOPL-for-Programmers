
list = ["Bon-Fils", " Anush", "Kavin", "Gabriel", "Phat", " Matthew", "Jorge", "Celia", "Kenneth", "Anderson",
        "Jonathan", "Mario" ]

greet = " welcome to the class"

for name in list:
    print( f"  {greet},  {name}")


# Exercise #1: Iterating through a list

 # Sort list of name
list.sort()
print(list) # print sorted list

for name in list:
    print( f"{name}, welcome to the class!, Hope you learn some useful things in CSC-287, {name}")
