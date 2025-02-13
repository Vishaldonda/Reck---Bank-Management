# Custom Range Generator: 
# for example input 5. Output will be 1,2,3,4,5

def infinite_generator():
    i = 1
    while True:  # Infinite loop
        # next(gen), execution resumes immediately after the yield statement and continues until the next yield
        yield i
        i += 1

gen = infinite_generator()

n =  int(input("Enter the number n upto you wanted to generate : ")) 
for i in range(n):
    print(next(gen))