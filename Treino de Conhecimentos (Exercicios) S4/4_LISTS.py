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
list1 = [1,2,3,4,5]
list2 = [4,5,6,7,8]

list_combine = list(set(list1 + list2))
print(list_combine)