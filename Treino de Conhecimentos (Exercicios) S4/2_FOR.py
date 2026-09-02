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
list = [2, 5, 6, 7, 8, 10, 12]
count = 0
for i in list:
    if i % 2 == 0:
        count += 1
        print(f'Number of pairs "{i}" in list count: {count}')
