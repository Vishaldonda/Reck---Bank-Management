# Extract Words with More than Three Letters
 
# Problem Statement:

# Given a 2D list of words, flatten it into a single list while keeping only words with more than three letters. Convert them to uppercase.
# Example Input:
# pythonCopyEditwords = [
#     ["hi", "hello", "to"],
#     ["apple", "go", "code"],
#     ["yes", "python", "AI"]
# ]
 
# Expected Output:
# ["HELLO", "APPLE", "CODE", "PYTHON"]

pythonCopyEditwords = [
    ["hi", "hello", "to"],
    ["apple", "go", "code"],
    ["yes", "python", "AI"]
]
 

list = [pythonCopyEditwords[i][j].upper() for i in range(len(pythonCopyEditwords)) for j in range(len(pythonCopyEditwords[i])) if len(pythonCopyEditwords[i][j])>3 ]

print(list)