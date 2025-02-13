# Problem Statement:
# You are given a 2D list (matrix) containing integers. 
# Your task is to flatten the matrix into a single list 
# and retain only the even numbers, squaring them in the process.

# Constraints:
# The input is a list of lists containing integers.
# The output should be a single list of squared even numbers.


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

list = [matrix[i][j]**2 for i in range(len(matrix)) for j in range(len(matrix[i])) if matrix[i][j]%2==0 ]

print(list)