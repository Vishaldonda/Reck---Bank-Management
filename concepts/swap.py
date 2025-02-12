# 1. Using a Temporary Variable (Traditional Method)

a = 5 
b = 10 
print(f"a: {a}, b: {b}")

temp = a
a = b
b = temp 
print(f"a: {a}, b: {b}")
# uses extra memory

# 2. Tuple Unpacking

a, b = 5, 10
a, b = b, a

print(a, b)
# No extra memory needed
# uses tuple unpacking

# 3. Arithmetic Operations (Without Extra Variable) 
    # 3.1 using only (+) and (-)

a = 5 
b = 10 

a = a + b # 15
b = a - b # 5
a = a - b  

print(a, b)
#  Works without extra space
    # 3.2 using only (*) and (//)

a = 5 
b = 10 

a = a*b #50
b = a//b # 5
a = a //b
print(a, b) 

# 4. Using XOR Bitwise Operator (Best for Performance)
# XOR (Exclusive OR)  : operator (^) is a bitwise operator in Python that operates on binary numbers
# 0 ^ 0 = 0
# 1 ^ 1 = 0
# 0 ^ 1 = 1
# 1 ^ 0 = 1
# Result is 1 only if the bits are different.

# 4.1 XOR operator works on the binary representation of integers
# 1. XOR with Integers
a = 5
b = 10

result = a ^ b  # XOR
print(result)   # Output: 6

# Explanation:
#   0101  (5)
# ^ 0011  (3)
# --------
#   0110  (6)

# 4.2  XOR for Swapping Two Variables (Without Temp Variable)
a = 5
b = 10

a = a ^ b # 5 ^ 10
b = a ^ b # (5 ^ 10) ^ 10
a = a ^ b # (5 ^ 10) ^ 5

print(a, b)  # Output: 10 5

# No extra space used
# Faster than arithmetic methods
# No overflow risk like in arithmetic swap

# Toggle : applying XOR with 1 acts as a toggle switch, flipping 0 to 1 and 1 to 0
#          applying XOR with 0 does nothing (keeps bits the same)

# Practical Uses of XOR for Bit Flipping
    # Ex1: Toggling a bit: x ^ 1 can be used to switch a binary state (like a light switch).
    # Ex2: Checking if a number is odd or even:
        # x ^ 1 flips the last bit, changing even ↔ odd.
        # x & 1 checks if the last bit is 1 (odd) or 0 (even).
# Used for: Swapping numbers, finding unique elements, bit manipulation, and toggling bits.
#   - Super useful in competitive programming & cryptography
    
# 5. Using a List
a, b = [5, 10]
a, b = [b, a]

print(a, b)
# less efficient


# Conclusion : Tuple swap (unpacking), XOR(very fast), Arithmetic are fast performing