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
# age = int(input('Digit your age: '))
# while age >= 0 and age <= 120:
#     print('OK, valid age.')
#     age = int(input('Digit your age: '))
# print('Invalid age.')

# 10. Guess the secret number
# num = int(input('Digit a number to check secret number: '))
# secretNumber = 8
# while num != secretNumber:
#     print('Invalid number...')
#     num = int(input('Send other number: '))
# print('Very nice! You have sent a success valid number ')

# 11. Convert decimal to binary 
# num = int(input('Send a number to convert binary: '))
# binary = ""
# while num > 0:
#     binary = str(num % 2) + binary
#     num //= 2
#     print(num)
# print(f'The binary number is: {binary}')

# 12. Reverse string
# str = str(input('Digit a word: '))
# str_2 = ""
# i = len(str) - 1
# while i >= 0:
#     str_2 += str[i]
#     i -= 1
# print(str_2)

# 13. Count how many times a character appears in a string
# str = input('Digite a str: ')
# char = input('Digit a character: ')
# count = 0
# i = 0
# while i < len(str):
#     if str[i] == char:
#         count += 1
#     i += 1
# print(f"The charcater '{char}' appears '{count}' times this string.")

# 14. Average of the positive numbers
# sum = 0
# count = 0
# num = float(input('Digit a number ("0" to exit): '))
# while num != 0:
#     if num > 0:
#         sum += num
#         count += 1
#     num = float(input('Digit a number ("0" to exit): '))
# if count > 0:
#     avg = sum / count
#     print(f'Average of the postive numbers is: {avg:.2f}')
# else:
#     print('None postive number was sended.')

# 15. Sum the numbers until a limit value is reached
# lim = 100
# sum = 0
# while sum < lim:
#     num = float(input('Digit a number: '))
#     sum += num
#     print(f'Total sum: {sum}')
# print("You've reached the limit")