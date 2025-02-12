1. `- list comprehension (increse complexity) - Yes
how much time it takes` - lesser than traditioanl loop; fewer function calls like `append`

2. - `swap 2 variables different ways` - Done

3. - lambda fucntion  `(explore)`
    - anonymous , single line funciton
    - lambda arg: expression

4. - decorator :
    - decorator in Python is a function that takes another function as input, adds some functionality to it, and returns the modified function

    - It’s useful when you want to modify a function without changing its original code.

    - used for logging, authentication, caching

```
    Exercide: Create two decorators and check which one will it call first
```

5. genarators:
- generator in Python is a special type of function that produces values one at a time using the yield keyword, instead of returning them all at once like a regular function.
- generators memory-efficient and useful for handling large datasets or infinite sequences.

```
def infinite_generator():
    i = 1
    while True:  # Infinite loop
        yield i
        i += 1

gen = infinite_generator()

print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
print(next(gen))  # Output: 3
# This will never raise StopIteration, as the generator keeps yielding values.
```


## Future concepts
```
- iterator
- context manager
```