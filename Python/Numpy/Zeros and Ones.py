import numpy as np

# Read input values for the shape of the array and convert them into a tuple of integers
dimensions = tuple(map(int, input().split()))

# Create a NumPy array filled with zeros, having the shape 'l', and with integer data type
print(np.zeros(dimensions, dtype=np.int))

# Create a NumPy array filled with ones, having the shape 'l', and with integer data type
print(np.ones(dimensions, dtype=np.int))
