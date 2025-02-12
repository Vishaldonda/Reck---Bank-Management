funct = lambda a,b : a+b

def add(a,b):
    return a+b
    
print(type(add))
print(type(funct))
print(funct.__name__)  # lambda

print(funct(2,3))