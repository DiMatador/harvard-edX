class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2

    @property
    def area(self):
        return 3.14 * self.radius * self.radius

# Create an instance of the Circle class
my_circle = Circle(5)

# Access the diameter property
print(my_circle.diameter)  # Output: 10

# Modify the diameter property
my_circle.diameter = 14
print(my_circle.radius)  # Output: 7
print(my_circle.diameter)  # Output: 14

# Access the area property
print(my_circle.area)  # Output: 153.86
