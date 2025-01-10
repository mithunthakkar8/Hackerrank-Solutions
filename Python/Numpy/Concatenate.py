import numpy as np

# Read the dimensions N, M, and P from input where:
# N = number of rows in the first array
# M = number of rows in the second array
# P = number of columns in each array
N, M, P = list(map(int, input().split()))

# Initialize an empty list to store the rows of the first array
rows_list = []

# Iterate over the input rows for the first array
for _ in range(N):
    # Read each row as a list of integers and append it to rows_list
    row = list(map(int, input().split()))
    rows_list.append(row)

# Convert the list of rows into a NumPy array for the first array
array_1 = np.array(rows_list)
    
# Re-initialize the list to store the rows of the second array
rows_list = []    

# Iterate over the input rows for the second array
for _ in range(M):
    # Read each row as a list of integers and append it to rows_list
    row = list(map(int, input().split()))
    rows_list.append(row)

# Convert the list of rows into a NumPy array for the second array
array_2 = np.array(rows_list)

# Concatenate the two arrays along the first axis (rows) and print the result
print(np.concatenate((array_1, array_2), axis=0))
