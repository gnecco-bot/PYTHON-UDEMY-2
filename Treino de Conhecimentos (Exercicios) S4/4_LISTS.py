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
num = [10, 45, 34, 87, 23, 56, 78, 12, 99]
numUnics = list(set(num))
numUnics.sort()
print(numUnics[-2])