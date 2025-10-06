msg = input ("Enter a number between 2 and 9")

userInput = int(msg)

if userInput >= 2 and userInput <= 9:
    print([[ 0 for i in range(userInput)] for j in range(userInput)]) 

else:
    print(f"{userInput} is out of bounds.") # Inform the user and exist
    