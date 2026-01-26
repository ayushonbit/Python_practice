#Pure and impure functions are two fundamental concepts in functional programming that describe different types of functions based on their behavior and side effects.
# Recursive functions are functions that call themselves in order to solve a problem. They typically have a base case to terminate the recursion and a recursive case that breaks the problem down into smaller subproblems.
#Lambdas, also known as anonymous functions, are small, unnamed functions defined using the `lambda` keyword in Python. They are typically used for short, simple operations that can be expressed in a single line of code.

# Examples of each are provided below:

# Pure Function
def pure_function(x, y):
    return x + y
print("Pure Function Output:", pure_function(2, 3))

# Impure Function
total = 0
def impure_function(x):
    global total
    total += x
    return total
print("Impure Function Output:", impure_function(5))
print("Impure Function Output:", impure_function(10))

# Recursive Function
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
print("Recursive Function Output (Factorial of 5):", factorial(5))


# Lambda Function
square = lambda x: x * x
print("Lambda Function Output (Square of 4):", square(4))

