# we are here learning about scopes in python (nonlocal variables and global variables)
# we have four types of scopes in python
# 1. Local Scope
# 2. Enclosing Scope
# 3. Global Scope
# 4. Built-in Scope


# Local Scope
def outer_function():
    x = "local x"

    def inner_function():
        y = "inner local y"
        print(x)  # Accessing variable from the enclosing scope
        print(y)  # Accessing local variable

    inner_function()
    # print(y)  # This would raise an error because y is not in the outer_function's scope
outer_function()

# Enclosing Scope
def outer_function_enclosing():
    x = "enclosing x"

    def inner_function_enclosing():
        print(x)  # Accessing variable from the enclosing scope

    inner_function_enclosing()
outer_function_enclosing()

# Global Scope
x_global = "global x"
def function_global():
    print(x_global)  # Accessing global variable
function_global()
print(x_global)  # Accessing global variable outside the function

# Built-in Scope
print(len("Hello, World!"))  # Using built-in function len()
print(abs(-10))  # Using built-in function abs()
print(max(1, 5, 3))  # Using built-in function max()
print(min(1, 5, 3))  # Using built-in function min()
print(sum([1, 2, 3, 4, 5]))  # Using built-in function sum()
print(round(3.14159, 2))  # Using built-in function round()
print(sorted([5, 2, 9, 1]))  # Using built-in function sorted()
print(type(42))  # Using built-in function type()
print(isinstance(42, int))  # Using built-in function isinstance()
print(dir([]))  # Using built-in function dir() on a list
print(help(str))  # Using built-in function help() on str class
print(chr(65))  # Using built-in function chr() to get character from ASCII value
print(ord('A'))  # Using built-in function ord() to get ASCII value from character
print(bin(10))  # Using built-in function bin() to get binary representation
print(hex(255))  # Using built-in function hex() to get hexadecimal representation
print(oct(8))  # Using built-in function oct() to get octal representation
print(eval("2 + 2"))  # Using built-in function eval() to evaluate an expression
print(int("42"))  # Using built-in function int() to convert string to integer
print(float("3.14"))  # Using built-in function float() to convert string to
print(str(100))  # Using built-in function str() to convert integer to string
print(list((1, 2, 3)))  # Using built-in function list() to convert tuple to list
print(tuple([1, 2, 3]))  # Using built-in function tuple()
print(set([1, 2, 2, 3]))  # Using built-in function set() to create a set
print(dict(a=1, b=2))  # Using built-in function dict() to create a dictionary
print(zip([1, 2, 3], ['a', 'b', 'c']))  # Using built-in function zip() to combine iterables
print(enumerate(['a', 'b', 'c']))  # Using built-in function enumerate() to get index and value
print(repr("Hello"))  # Using built-in function repr() to get string representation
print(format(3.14159, ".2f"))  # Using built-in function format
print(all([True, True, False]))  # Using built-in function all()
print(any([False, False, True]))  # Using built-in function any()
print(hash("Hello"))  # Using built-in function hash() to get hash value
print(id("Hello"))  # Using built-in function id() to get memory address
print(callable(len))  # Using built-in function callable() to check if len is callable
print(memoryview(b"Hello"))  # Using built-in function memoryview()
print(reversed([1, 2, 3]))  # Using built-in function reversed() to reverse an iterable
print(slice(1, 5, 2))  # Using built-in function slice()
print(staticmethod(function_global))  # Using built-in function staticmethod()
print(classmethod(outer_function))  # Using built-in function classmethod()
print(globals())  # Using built-in function globals() to get global symbol table
print(locals())  # Using built-in function locals() to get local symbol table
print(__import__('math'))  # Using built-in function __import__() to import a module
print(pow(2, 3))  # Using built-in function pow() to calculate power
print(complex(2, 3))  # Using built-in function complex() to create a complex number
print(bin(42))  # Using built-in function bin() to get binary representation
print(help(len))  # Using built-in function help() on len function
print(dir(str))  # Using built-in function dir() on str class
print(isinstance("Hello", str))  # Using built-in function isinstance()
print(issubclass(bool, int))  # Using built-in function issubclass()
print(memoryview(b"World"))  # Using built-in function memoryview()
print(bytearray(b"Hello"))  # Using built-in function bytearray()
print(bytes("Hello", 'utf-8'))  # Using built-in function bytes()
print(frozenset([1, 2, 3, 2]))  # Using built-in function frozenset()
print(property())  # Using built-in function property()
print(super())  # Using built-in function super()
print(type([]))  # Using built-in function type() on a list
print(vars())  # Using built-in function vars()
print(__build_class__)  # Using built-in function __build_class__()
print(__debug__)  # Using built-in constant __debug__
print(__name__)  # Using built-in constant __name__
print(__doc__)  # Using built-in constant __doc__
print(__package__)  # Using built-in constant __package__
print(__loader__)  # Using built-in constant __loader__
print(__spec__)  # Using built-in constant __spec__
print(__file__)  # Using built-in constant __file__
print(__cached__)  # Using built-in constant __cached__


