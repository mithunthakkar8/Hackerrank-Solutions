import numpy as np  # Import the NumPy library for numerical operations

# Read the number of rows and columns for the array from user input
# Example input format: "3 4" (3 rows, 4 columns)
rows, columns = list(map(int, input().split()))

# Initialize an empty list to store the rows of the array
rows_list = []

# Iterate over the input rows
for _ in range(rows):
    # Read each row as a list of integers from user input
    # Example: If input is "1 2 3 4", the row will be [1, 2, 3, 4]
    row = list(map(int, input().split()))
    # Append the row to the rows_list
    rows_list.append(row)

# Convert the list of rows (rows_list) into a NumPy array
array = np.array(rows_list)

# Compute the minimum value of each row using np.min with axis=1 (row-wise operation)
# Then find the maximum value among these minimum values using np.max
result = np.max(np.min(array, axis=1))

# Print the result
print(result)
