# 1. Create a list with the 10 integers
# list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(max(list))
# print(min(list))

# 2. Ask the user 5 numbers and store them in a list
# list = []
# for i in range(5):
#     list.append(int(input('Send a number: ')))
# print(list)
# print(sum(list))

# 3. From a list of numbers, remove the even numbers 
# num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# num_odd = [n for n in num if n % 2 != 0]
# print(num_odd)

# 4. Create a list with the 10 names and sort it in alphabetical order
# names = ['ygor', 'joao', 'philipe', 'ana', 'david', 'daniel', 'luca', 'jeniffer', 'rhuan', 'joseph']
# names.sort()
# print(names)

# 5. Create a list and find the second-largest number in the list
# num = [10, 45, 34, 87, 23, 56, 78, 12, 99]
# numUnics = list(set(num))
# numUnics.sort()
# print(numUnics[-2])

# 6. Ask the user a list words separed for comma and show the list with word inverted 
# word = input('Digit a words separed for comma: ').split(',')
# wordInverted = word[::-1]
# print('List with the word reversed:', wordInverted)

# 7. Given a list of numbers, create a new list that contains only the number larger }}than 10
# num = [1, 23, 56, 21, 8, 6, 10, 9]
# numLarger = [n for n in num if n > 10]
# print(numLarger)

# 8. Check if a list contains a value specific
# num = [1, 23, 56, 21, 8, 6, 10, 9]
# exists = int(input('Digit a value to check if it contains in a list specific: '))
# if exists in num:
#     print(f'This number "{exists}" exists in this list')
# else:
#     print('It do not exists in this list.')

# 9. Combine two lists of the numbers, remove duplicates and show it in a list 
# list1 = [1,2,3,4,5]
# list2 = [4,5,6,7,8]
# list_combine = list(set(list1 + list2))
# print(list_combine)

# 10. Ask to user 5 numbers and show it in a original list and order list without modify the original
# listOriginal = []
# for i in range(5):
#     i = int(input('Digit a number to put in a list: '))
#     listOriginal.append(i)
# listOrder = sorted(listOriginal)
# print(listOriginal)
# print(listOrder)

# 11. Create a list of the list containing the students names and their grade
# students = [['João', 8, 7, 9], ['Ana', 10, 9 ,6], ['Clara', 8, 9, 9]]
# for student in students:
#     media = sum(student[1:]) / len(student[1:])
#     student.append(media)
# listOrder = sorted(students, key=lambda x: x[4], reverse=True)
# for student in listOrder:
#     print(f'Student: {student[0]} - Media: {student[4]:.2f}')

# 12. Implement a function that get two lists and return a list containing just the elements that presents in both lists.
# list1 = [1,2,3,4,5]
# list2 = [4,5,6,3,6,8]
# def bothList(list1, list2):
#     return [item for item in list1 if item in list2]
# print(bothList(list1, list2))

# 13. Given a list of the integers, create a function that split the list in two new lists: one containing the positive numbers and other containing negative numbers. Show it in two lists and your size 
# def splitList(num):
#     positive = [n for n in num if n > 0]
#     negative = [n for n in num if n < 0]
#     return positive,  negative
# list1 = [10, -1, -7, 4, 8, -9, 3, -2, -5, 0]
# print(splitList(list1))

# 14. given a list of the words, create a function that agroup that words with your length. The function must return a dict where the keys are the length and your values are lists of the words with that one length 
# def agroupByLength(word):
#     agroup = {}
#     for word in words:
#         length = len(word)
#         if length not in agroup:
#             agroup[length] = []
#         agroup[length].append(word)
#     return agroup
# words = ['Cachorro', 'Gato', 'Elefante', 'Ave', 'Rato', 'Onça', 'Girafa']
# res = agroupByLength(words)
# for lengt, agroup in res.items():
#     print(f'Word with {lengt} letters: {agroup}')

# 15. Given a list of the integers, to write a function that return sum the elements that in indices pairs and sum the elements that in indices odd 
# def sumPairsOdd(num):
#     sumPairs = sum(num[i] for i in range(0, len(num), 2))
#     sumOdd = sum(num[i] for i in range(1, len(num), 2))
#     return sumPairs, sumOdd
# list = [10, 15, 20, 25, 30, 35, 40]
# sumPairs, sumOdd = sumPairsOdd(list)
# print(f'Sum pairs: {sumPairs}')
# print(f'Sum Odd: {sumOdd}')