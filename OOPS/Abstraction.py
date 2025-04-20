# Definition: Hiding complex implementation details and exposing only essential features.

# Key Concepts:
# Abstract classes (from abc import ABC, abstractmethod).

# Interfaces (Python uses abstract classes for this).


# Abstract Base Classes (ABCs) - Python's Equivalent
# Key Properties:
# Requires abc module: Must import ABC and abstractmethod from abc module

# Partial abstraction: Can mix abstract and concrete methods

# Cannot be instantiated: Attempting to instantiate raises TypeError

# Subclass enforcement: Subclasses must implement all abstract methods

# Registration: Non-subclasses can be registered as virtual subclasses

# Multiple inheritance: Supports multiple abstract base classes

# Dynamic checking: isinstance() and issubclass() work with ABCs

# Abstract Methods in Python
# Key Properties:
# Decorator syntax: Marked with @abstractmethod decorator

# No implementation: Typically just contain pass or raise NotImplementedError

# Enforcement: Must be overridden in concrete subclasses

# Can have docstrings: Should include docstring explaining purpose

# Combined with other decorators: Can be used with @classmethod, @staticmethod, etc.



from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius

# Usage
circle = Circle(5)
print(circle.area())      # Output: 78.5
print(circle.perimeter()) # Output: 31.4

# shape = Shape()  # Error: Can't instantiate abstract class