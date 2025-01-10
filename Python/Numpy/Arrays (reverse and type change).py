# Importing the NumPy library for efficient numerical operations
import numpy

# Function to process the input array
def arrays(arr):
    # Reverse the order of elements in the array using NumPy's flip function
    arr = numpy.flip(arr)
    # Convert the array elements to 64-bit floating-point numbers for consistent precision
    arr = arr.astype('float64')
    return arr

# Read input from the user as a space-separated string and split it into a list of strings
arr = input("Enter space-separated values: ").strip().split(' ')

# Process the input list using the arrays function
result = arrays(arr)

# Print the resulting NumPy array after processing
print(result)
