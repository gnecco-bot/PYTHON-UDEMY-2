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
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
# print(factorial(5))

# 4. Function to count letters in a string
# def countLetters(word):
#     return len(word.replace(" ", ""))
# print(countLetters('test and test'))

# 5. Invert string function
# def invertString(word):
#     return word[::-1]
# print(invertString('teste'))

# 6. Calculate average function
# def average(a, b, c):
#     return (a + b + c) / 3
# print(average(5, 8, 9))

# 7. Converte temperature function (celsius to fahrenheit)
# def convertToFahrenheit(c):
#     return (c * 9/5) + 32
# print(convertToFahrenheit(20))

# 8. Fuction to check if a number is prime
# def numberPrime(n):
#     if n < 2:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True
# print(numberPrime(19))

# 9. Function to generate a multiplication table
# def table(n):
#     for i in range(1, 11):
#         print(f'{n} X {i} = {n*i}')
# print(table(10)) 

# 10. Palindrome check function
# def palindrome(word):
#     word = word.replace(" ", "").lower()
#     return word == word[::-1]
# print(palindrome('ava'))
        
# 11. Calcule power function
# def power(a, b):
#     return a ** b
# print(power(10, 2))

# 12. Function to convert seconds to hours, minutos and seconds
# def convertSeconds(seconds):
#     hours = seconds // 3600
#     minutes = (seconds % 3600) // 60
#     seconds_remain = seconds % 60
#     return hours, minutes, seconds_remain
# hours, minutes, seconds = convertSeconds(8650)
# print(f'{hours} hours, {minutes} minutes and {seconds} seconds')

# 13. Function to count vowels
# def vowels(word):
#     vowels = 'aeiouAEIOU'
#     return sum([1 for letters in word if letters in vowels])
# print(vowels('testeasdasdu123hpeoinmviejr'))

# 14. Function to count words in a string
# def wordCount(text):
#     return len(text.split())
# print(wordCount('teste alo tetetest'))

# 15. Function to order a list
# def listNumbers(listNum):
#     return sorted(listNum)
# print(listNumbers([5, 4, 2, 1, 6, 8, 2]))

# 16. Function to find a largest number or smallest number in a list
# def largerOrSmall(list):
#     return max(list), min(list)
# print(largerOrSmall([1,2,7,4,2,7,89,23,0,51]))