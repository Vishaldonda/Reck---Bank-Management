arr = [1,2,3,4,5]

# 1. list comprehensions are designed to build and return a new list
list = [i for i in arr]
print(list)

# 2. generic exp
print(*(i for i in arr))

# 3. map fucntion
map(print, arr)


import time

# Using nested loops
start_time = time.time()
nested_result = []
for i in range(1000):
    for j in range(1000):
        nested_result.append(i * j)
nested_time = time.time() - start_time
print(f"Nested loops execution time: {nested_time:.5f} seconds")

# Using list comprehension
start_time = time.time()
comprehension_result = [i * j for i in range(1000) for j in range(1000)]
comprehension_time = time.time() - start_time
print(f"List comprehension execution time: {comprehension_time:.5f} seconds")

# Compare performance
if nested_time < comprehension_time:
    print("Nested loops were faster")
else:
    print("List comprehension was faster")


