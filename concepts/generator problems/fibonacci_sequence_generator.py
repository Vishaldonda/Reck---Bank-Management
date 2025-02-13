# fibonacci sequence generator
def infinite_generator():
    a = 0 
    b = 1    
    while True:
        yield a
        b = a+b
        a = b-a 
    
    
gen = infinite_generator()

n =  int(input("Enter the number of fibonacci terms to generate : ")) 
for i in range(n):
    print(next(gen))  # Output: 1

# This will never raise StopIteration, as the generator keeps yielding values.
