# 1. Count 1 to 10
# i = 0
# while i < 10:
#     i += 1
#     print(i)

# 2. Sums the numbers until the user enters 0.
# i = True
# sum = 0
# while i:
#     num = int(input('Digit a number (0 to exit):'))
#     sum += num 
#     if num == 0:
#         break
# print(sum)

# 3. Correct password 
# passwordCorrect = 'Python123'
# i = True
# while i:
#     password = str(input('Digit the correct password: '))
#     if password != passwordCorrect:
#         print('incorrect, try again.')
#     else: 
#         i = False
# print('Congratulations! You have sent the correct password!')

# 4. Numbers enter 1 to 10
# num = int(input('Digit a number enter 1 to 10: '))
# while num != 5:
#     print('A wrong value, try again')
#     num = int(input('Digit a number: '))
# print('Congratulations, you have sent a correct number!')

# 5. Countdown from 10 to 1
# count = 10
# while count >= 1:
#     print(f'CountDown: {count}')
#     count -= 1

# 6. Sum number pairs from 1 to 100
# sum = 0
# num = 2
# while num <= 100:
#     sum += num
#     num += 2
# print(f'Total sum: {sum}')

# 7. Count the digits of a number
# num = int(input('Digit a number: '))
# count = 0
# while num > 0:
#     num //= 10
#     count += 1
# print(f'Have {count} digit')

# 8. Successive multiplication
# num = int(input('Put a number: '))
# count = 10
# while count >= 1:
#     print(f'{num} x {count} = {num * count}')
#     count -= 1

# 9. Check the age input
age = int(input('Digit your age: '))

while age >= 0 and age <= 120:
    print('OK, valid age.')
    age = int(input('Digit your age: '))

print('Invalid age.')