
sequence = [1,1]

for num in range (1, 11):
    print(num," ", end="")

sequence.append(sequence[-2]+sequence[-1])

print(sequence)