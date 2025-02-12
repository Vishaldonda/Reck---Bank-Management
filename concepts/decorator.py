# function that modifies another function without changing its actual code. 
# It is often used to add functionality

# decorator function always expects an function argument
def print_function2(org_func):
    def wrapper():        
        print("function 2")
        org_func()
    return wrapper

def print_function1(org_func):
    def wrapper():        
        print("function 1")
        org_func()
    return wrapper

# add = print_function2(print_function1(add))
@print_function2
@print_function1
def add():
    print("function main")
    # return a+b

add()

# equivalent to 
# add = print_function2(print_function1(add))
# To work as a proper decorator, each function must return a function (usually a wrapper).

