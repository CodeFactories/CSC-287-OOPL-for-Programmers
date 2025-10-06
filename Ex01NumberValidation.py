# This Validate Number

msg = input(" Enter a number between 1 and 9")

userInput = int(msg)

if (userInput >= 1 and userInput  <= 9):
    print(f" {userInput} is between 1 and 9")

else:
    print(f" {userInput} is not between 1 and 9")

# If a string  or a decimal is entered the program will crash.