import math  # Import the math module for mathematical operations

class Complex(object):
    def __init__(self, real, imaginary):
        # Initialize a complex number with real and imaginary parts
        self.real = real
        self.imaginary = imaginary
        
    def __add__(self, no):
        # Define addition for complex numbers
        real_part = self.real + no.real
        imaginary_part = self.imaginary + no.imaginary
        sign = "+" if imaginary_part >= 0 else ""
        return f"{real_part:.2f}{sign}{imaginary_part:.2f}i"
        
    def __sub__(self, no):
        # Define subtraction for complex numbers
        real_part = self.real - no.real
        imaginary_part = self.imaginary - no.imaginary
        sign = "+" if imaginary_part >= 0 else ""
        return f"{real_part:.2f}{sign}{imaginary_part:.2f}i"
        
    def __mul__(self, no):
        # Define multiplication for complex numbers
        real_part = self.real * no.real - self.imaginary * no.imaginary
        imaginary_part = self.real * no.imaginary + no.real * self.imaginary
        sign = "+" if imaginary_part >= 0 else ""
        return f"{real_part:.2f}{sign}{imaginary_part:.2f}i"

    def __truediv__(self, no):
        # Define division for complex numbers
        denominator = no.real**2 + no.imaginary**2
        real_part = (self.real * no.real + self.imaginary * no.imaginary) / denominator
        imaginary_part = (self.imaginary * no.real - self.real * no.imaginary) / denominator
        sign = "+" if imaginary_part >= 0 else ""
        return f"{real_part:.2f}{sign}{imaginary_part:.2f}i"

    def mod(self):
        # Calculate the modulus of a complex number
        modulus = math.sqrt(self.real**2 + self.imaginary**2)
        return f"{modulus:.2f}+0.00i"

    def __str__(self):
        # Return the string representation of a complex number
        if self.imaginary == 0:
            return "%.2f+0.00i" % (self.real)
        if self.real == 0:
            sign = "+" if self.imaginary >= 0 else "-"
            return f"0.00{sign}{abs(self.imaginary):.2f}i"
        sign = "+" if self.imaginary >= 0 else "-"
        return f"{self.real:.2f}{sign}{abs(self.imaginary):.2f}i"

if __name__ == '__main__':
    # Parse input for the first complex number
    c = map(float, input().split())
    # Parse input for the second complex number
    d = map(float, input().split())
    # Create Complex number instances for input values
    x = Complex(*c)
    y = Complex(*d)
    # Perform operations and print results
    print(*map(str, [x + y, x - y, x * y, x / y, x.mod(), y.mod()]), sep='\n')
