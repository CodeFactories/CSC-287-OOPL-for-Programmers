# This repeat input back to the user until the user enter 'quit'

userInput = input ("Tell me something, and I will repeat it back to you." \
                    " Enter 'quit' to end the program. ")

# while statement that exit when the user enter quit
while userInput != "quit":
    print( f" You type {userInput}")
    userInput = input ("Tell me something, and I will repeat it back to you." \
                        " Enter 'quit' to end the program. ")

print("Thank you for your visit!")
    