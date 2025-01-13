# Import the NumPy library for numerical computations
import numpy as np

# Set the print options for NumPy to ensure legacy floating-point formatting (for compatibility with older versions)
np.set_printoptions(legacy='1.13')

# Read a space-separated input of floating-point numbers, convert to a list of floats
A = list(map(float, input().split()))

# Print the floor values of the input array (rounds down to the nearest integer for each element)
print(np.floor(A))

# Print the ceiling values of the input array (rounds up to the nearest integer for each element)
print(np.ceil(A))

# Print the rounded values of the input array (rounds to the nearest integer; ties are rounded to the nearest even integer)
print(np.rint(A))
