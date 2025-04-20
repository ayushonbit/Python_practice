# 4. Polymorphism
# Definition: The ability to use a single interface for different data types (e.g., methods with the same name but different behaviors).

# Key Concepts:
# Method Overloading (not natively supported, but simulated).

# Duck Typing (if it walks like a duck, it’s a duck).

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

# Polymorphic function
def print_area(shape):
    print(f"Area: {shape.area()}")

# Usage
rectangle = Rectangle(4, 5)
circle = Circle(7)

print_area(rectangle)  # Output: Area: 20
print_area(circle)     # Output: Area: 153.86