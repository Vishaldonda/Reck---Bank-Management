# -----------------------------
# *args and **kwargs are used to handle variable numbers of arguments in a function.

# *args (Positional Arguments)
# *args allows a function to accept any number of positional arguments.
# Inside the function, args is a tuple containing all arguments.

# **kwargs (Keyword Arguments)
# **kwargs allows a function to accept any number of keyword arguments.
# Inside the function, kwargs is a dictionary.

def add_numbers(*args):
    print(args)  # args is a tuple
    return sum(args)

print(add_numbers(1, 2, 3, 4, 5))  

def print_details(**kwargs):
    print(kwargs)  # kwargs is a dictionary
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_details(name="Alice", age=25, city="New York")


def show_info(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

show_info(1, 2, 3, name="Bob", age=30)
# Output :
# Positional arguments: (1, 2, 3)
# Keyword arguments: {'name': 'Bob', 'age': 30}
