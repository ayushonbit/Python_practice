# if you return Nothing then the function will return None by default.
# one value can be returned using return statement.
# multiple values can be returned using return statement separated by commas.
# Early return can be done using return statement.
"""
Below are examples demonstrating these concepts.
"""

def return_nothing():
    print("This function returns nothing explicitly.")
    # No return statement here

def return_one_value():
    print("This function returns one value.")
    return 42

def return_multiple_values():
    print("This function returns multiple values.")
    return 1, 2, 3

def early_return_example(n):
    print("This function demonstrates early return.")
    if n < 0:
        return "Negative number"
    return "Non-negative number"

