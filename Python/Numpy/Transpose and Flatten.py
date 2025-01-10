import numpy as np

# Read the number of rows and columns for the array
rows, columns = list(map(int, input().split()))

# Initialize an empty list to store the rows of the array
rows_list = []

# Iterate over the input rows
for _ in range(rows):
    # Read each row as a list of integers and append it to rows_list
    row = list(map(int, input().split()))
    rows_list.append(row)

# Convert the list of rows into a NumPy array
array = np.array(rows_list)

# Print the transposed version of the array (rows become columns and vice versa)
print(np.transpose(array))

# Print the flattened (1D) version of the array (all elements in a single row)
print(array.flatten())
