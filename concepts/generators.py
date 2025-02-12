# generator in Python is a special type of function that produces values one at a time
# generators memory-efficient and useful for handling large datasets or infinite sequences

def infinite_generator():
    i = 1
    while True:  # Infinite loop
        yield i
        i += 1

gen = infinite_generator()

# print(next(gen))  # Output: 1
# print(next(gen))  # Output: 2
# print(next(gen))  # Output: 3
# This will never raise StopIteration, as the generator keeps yielding values.


# 2. generic exp
arr = [1,2,3,4,5]
gen = (i for i in range(len(arr)))
print(type(gen)) # <class 'generator'>