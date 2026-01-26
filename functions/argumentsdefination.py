# def function_name(arg1, arg2='default', *args, **kwargs):
#     """
#     This is an example function to demonstrate argument definitions in Python.
#
#     Parameters:
#     arg1 (int): The first positional argument.
#     arg2 (str): The second argument with a default value of 'default'.
#     *args: Additional positional arguments.
#     **kwargs: Additional keyword arguments.
#
#     Returns:
#     None
#     """
#     print(f"arg1: {arg1}")
#     print(f"arg2: {arg2}")
#     print(f"Additional positional arguments (args): {args}") -- positional arguments
#     print(f"Additional keyword arguments (kwargs): {kwargs}") -- variable number of arguments - yeh ek dict hota h


# chai = "ginger chai"
# def  prepare_chai(order):
#     print(f"Preparing {order}...")
#     print(f"{chai} is ready!")
#
# prepare_chai("Masala Chai with extra sugar")

# def function_name(arg1, arg2='default', *args, **kwargs):
#     """
#     This is an example function to demonstrate argument definitions in Python.
#
#     Parameters:
#     arg1 (int): The first positional argument.
#     arg2 (str): The second argument with a default value of 'default'.
#     *args: Additional positional arguments.
#     **kwargs: Additional keyword arguments.
#
#     Returns:
#     None
#     """
#     print(f"arg1: {arg1}")
#     print(f"arg2: {arg2}")
#     print(f"Additional positional arguments (args): {args}")  # positional arguments, tuple ki tarah hota h
#     print(f"Additional keyword arguments (kwargs): {kwargs}")  # key value arguments , variable number of arguments - yeh ek dict hota h

def special_chai(*ingridients, **extras):
    print("Preparing special chai with the following ingridients:")
    print("Ingridients: ", ingridients)
    print("Extras: ", extras)

special_chai("ginger", "cardamom", sugar=3, milk="full cream")





