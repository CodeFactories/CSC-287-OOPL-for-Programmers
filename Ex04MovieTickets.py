# This practice 
# write a loop in which you ask users their age, and then tell them 
# the cost of their movie ticket. Typing quit should exit the program.
# Also try using a flag or the break statement to implement the above.

flag = True
while flag:
    userInput = input("Enter the or type 'quit' to exit the program: ") # Prompt the user
    if (userInput == 'quit'):
        flag = False # Set flag to false to exit the loop
        
    else:
        age = int(userInput) # Convert input to digit
        if (age < 3):
            print("Print the ticket is free. ") # Display price to the user
        
        elif(age >= 3 and age <= 12):
            print("The ticket is $ 10. ")

        else:
            print("The ticket is $ 15.")
        
