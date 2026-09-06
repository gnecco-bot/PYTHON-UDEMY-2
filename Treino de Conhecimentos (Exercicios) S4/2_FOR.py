# 1. Print the numbers from 1 to 10
# for i in range(1, 11):
#     print(i)

# 2. Print the pairs from 1 to 20
# for i in range(2,21,2):
#     print(i)

# 3. Sum numbers from 1 to 100
# sum = 0
# for i in range(0, 101):
#     sum += i
#     print(sum)        

# 4. Print the elements of a list
# list = [5, 10, 15, 20, 25]
# for i in list:
#     print(i)

# 5. Count the letters of a word
# word = str(input('Digit a word: '))
# letters = 0
# for i in word:
#     letters += 1
# print(letters)

# 6. Multiplication each number by 3
# list = [1, 2, 3, 4, 5]
# for i in list:
#     print(i*3)

# 7. Print each letters by "python"
# python = 'python'
# for i in python:
#     print(i)

# 8. Count the number of pairs in a list 
# list = [2, 5, 6, 7, 8, 10, 12]
# count = 0
# for i in list:
#     if i % 2 == 0:
#         count += 1
#         print(f'Number of pairs "{i}" in list count: {count}')

# 9. Print odd numbers
# for i in range(21):
#     if i % 2 != 0:
#         print(i)

# 10. Calcute factorial number sended by user
# num = int(input('Digit a number: '))
# factorial = 1
# for i in range(1, num+1):
#     factorial *= i
# print(f'Factorial number {factorial}')

# 11. To check prime number 
# num = int(input('Send a number to check if it is prime: '))
# prime = True
# for i in range(2, num):
#     if num % i == 0:
#         prime = False
#         break
# if prime:
#     print(f'This number "{num}" is prime or not? {prime}')
# else:
#     print(f'This number "{num}" is prime or not? {prime}')

# 12. Multiple each element of the list by a provided value
# num = int(input('Send a value: '))
# list = [2, 4, 5, 8, 10]
# list2 = [i * num for i in list]
# print(list2)

# 13. Vowel count in a sentence
# phrase = str(input('Digit a phrase: '))
# vowel = 'aeiou'
# count = 0
# for i in phrase:
#     if i in vowel:
#         count += 1
# print(f'Have "{count}" vowel!')

# 14. Sort a list manually
# list = [29, 10, 14, 37, 13]
# for i in range(len(list)):
#     for j in range(i+1, len(list)):
#         if list[i] > list[j]:
#             list[i], list[j] = list[j], list[i]
# print(list)

# 15. Check for palindrome
# word = str(input('Digit a word: ')).lower()
# palindrome = True
# for i in range(len(word)):
#     if word[i] != word[-(i + 1)]:
#         palindrome = False
#         break
# if palindrome:
#     print('is palindrome')
# else:
#     print('isnt palindrome')
