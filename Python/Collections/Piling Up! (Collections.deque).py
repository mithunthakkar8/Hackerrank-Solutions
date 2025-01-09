# Import deque for efficient queue operations
from collections import deque  

# Read the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Read the number of side lengths (not used directly in the logic)
    _ = int(input())
    
    # Initialize a deque to hold the side lengths and a set to store used side lengths
    d = deque() 
    s = set()
    
    # Initially set the result to 'Yes', assuming the sequence is valid
    Result = 'Yes'
    
    # Read the side lengths as a list of integers
    sideLengths = list(map(int, input().split()))
    
    # Add all the side lengths to the deque for further processing
    d.extend(sideLengths)
    
    # While the deque is not empty, continue processing
    while d:
        # If the first element of deque is greater than or equal to the last element
        if d[0] == max(d[0], d[-1]):
            # Check if the set is empty or if the current element (d[0]) is less than or equal to the max value in the set
            if (not s) or (d[0] <= max(s)):
                # Add the current element (d[0]) to the set
                s.add(d[0])
                # Remove the element from the front of the deque
                d.popleft()
            else:
                # If the condition fails, set the result to 'No' and exit the loop
                Result = 'No'
                break
        else:
            # If the last element of deque is greater than or equal to the first element
            if (not s) or (d[-1] <= max(s)):
                # Add the current element (d[-1]) to the set
                s.add(d[-1])
                # Remove the element from the back of the deque
                d.pop()
            else:
                # If the condition fails, set the result to 'No' and exit the loop
                Result = 'No'
                break 
    
    # Output the result for the current test case
    print(Result)
