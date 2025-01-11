import numpy as np

# Configure NumPy to use legacy printing style (for compatibility with older NumPy versions)
np.set_printoptions(legacy='1.13')

# Read the dimensions of the identity-like array
N, M = input().split()
N, M = int(N), int(M)  # Convert input strings to integers

# Create a 2D array with ones on the main diagonal and zeros elsewhere (identity-like matrix)
# The `k=0` argument specifies the diagonal to be filled with ones (main diagonal by default)
print(np.eye(N, M, k=0))
