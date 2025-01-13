# Import the NumPy library for numerical computations
import numpy as np

# Read the number of rows and columns for the array as integers
rows, columns = list(map(int, input().split()))

# Initialize an empty list to store the rows of the array
rows_list = []

# Loop through the input to read each row of integers
for _ in range(rows):
    # Read a row of integers, split by spaces, and append it to the rows_list
    row = list(map(int, input().split()))
    rows_list.append(row)

# Convert the list of rows into a NumPy array for efficient numerical operations
array = np.array(rows_list)

# Compute the sum of elements along axis 0 (column-wise sum)
axis0_sum = np.sum(array, axis=0)

# Compute the product of the column-wise sums and print the result
print(np.product(axis0_sum))
