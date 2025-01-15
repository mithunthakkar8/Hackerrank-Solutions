# Import the Fraction class to handle rational numbers precisely
from fractions import Fraction  

# Import the reduce function to apply a binary operation cumulatively
from functools import reduce    

# Define the function to compute the product of a list of fractions
def product(fracs):
    # Apply the multiplication operation cumulatively to all fractions in the list
    t = reduce(lambda x, y: x * y, fracs)  
    
    # Return the numerator and denominator of the resulting fraction
    return t.numerator, t.denominator      

# Main execution block
if __name__ == '__main__':
    # Initialize an empty list to store the fractions
    fracs = []  

    # Read the number of fractions to be input from the user
    for _ in range(int(input())):
        # Read each fraction, convert it to a Fraction object, and append to the list
        fracs.append(Fraction(*map(int, input().split())))

    # Compute the product of the fractions using the product function
    result = product(fracs)

    # Output the result as a tuple containing the numerator and denominator
    print(*result)
