import math

class Points(object):
    def __init__(self, x=0, y=0, z=0):
        # Initialize a point in 3D space with default values of 0 for x, y, and z
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, no):
        # Overload the subtraction operator to compute the vector difference between two points
        return Points(self.x - no.x, self.y - no.y, self.z - no.z)

    def dot(self, no):
        # Compute the dot product of the current vector with another vector
        a = [self.x, self.y, self.z]
        b = [no.x, no.y, no.z]
        dot_product = a[0] * b[0] + a[1] * b[1] + a[2] * b[2]
        return dot_product

    def cross(self, no):
        # Compute the cross product of the current vector with another vector
        a = [self.x, self.y, self.z]
        b = [no.x, no.y, no.z]
        cross_product = [a[1] * b[2] - a[2] * b[1],
                         a[2] * b[0] - a[0] * b[2],
                         a[0] * b[1] - a[1] * b[0]]
        return Points(*cross_product)

    def absolute(self):
        # Compute the magnitude (absolute value) of the vector
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)

if __name__ == '__main__':
    points = list()

    # Read coordinates for four points in 3D space
    for i in range(4):
        a = list(map(float, input().split()))
        points.append(a)

    # Create Points instances for the four input points
    a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])

    # Calculate the cross product of vectors (b - a) and (c - b)
    x = (b - a).cross(c - b)

    # Calculate the cross product of vectors (c - b) and (d - c)
    y = (c - b).cross(d - c)

    # Compute the angle between the two vectors using the dot product and magnitudes
    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))

    # Convert the angle from radians to degrees and print it with two decimal precision
    print("%.2f" % math.degrees(angle))
