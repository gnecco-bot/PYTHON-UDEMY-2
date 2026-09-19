# 1. Sum function 
# def sum(a, b):
#     return a + b
# print(sum(1, 5))

# 2. Function that checks if a number is even or odd
# def checkNumber(num):
#     if num % 2 == 0:
#         return 'Even'
#     elif num % 2 != 0:
#         return 'Odd'
#     else:
#         return 'number incorret'
# print(checkNumber(2))

# 3. Factorial function
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))