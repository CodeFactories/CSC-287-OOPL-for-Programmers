# initializing a two Dimensional List

#list = []

#for i in range (5):
#    list [i] = []
#    for j in range(5):
#        list [i][j] = 0 # will raise a error.


# Correct way
list = []
for i in range(5):
    row = []
    for j in range(5):
        row.append(0)
        list.append(row)
print(list)

# Using List Comprehension
rows, cols = (5, 5)
print([[0 for i in range(cols)] for j in range(rows)])