# 1. Large number of the two input sended
# numOne = input('Put one number: ')
# numTwo = input('Put a second number: ')
# 
# if numOne.isdigit() & numTwo.isdigit():
#     if int(numOne) > int(numTwo):
#         print(numOne)
#     elif int(numOne) < int(numTwo):
#         print(numTwo)
#     else:
#         print('The numbers is equal.')
# else:
#     print('Only send numbers.')

# 2. Check a number even or odd (par ou impar)
# numEvenOrOdd = int(input('Send a number: '))
# 
# if numEvenOrOdd % 2 == 0: 
#     print(f'This number "{numEvenOrOdd}" is Even!')
#     print(f'This number "{numEvenOrOdd}" sended is Odd.')

# 3. Check the temperature
# tempUser = int(input('Set your temperature local: '))
# 
# if tempUser < 10:
#     print('It is so cold!') 
# elif 10 <= tempUser <= 25:
#     print('It is great!')
# elif tempUser > 25:
#     print('It is so hot!')
# else:
#     print('Something is wrong :(')

# 4. Calculate income tax
# salaryUser = float(int(input('Put your balance mensaly: ')))
# 
# if salaryUser > 5000.00:
#     newBalance = salaryUser * 0.8
#     deducted = salaryUser - newBalance
#     print(f'Your new balance after de income tax is "${newBalance:.2f}" and "${deducted:.2f}" was deducted.')
# else:
#     print('Your salary is less than $5000 and you dont need to pay income tax.')

# 5. Check the word is palindrome
# 
# word = input('Send a word: ').replace(" ", "").lower()
# 
# if word == word[::-1]:
#     print(f'The word "{word}" is palindrome!')
# else:
#     print(f'The word "{word}" is not palindrome.')

# 6. Check de larger of the 3 numbers
# 
# num1 = int(input('Send number one: '))
# num2 = int(input('Send a number two: '))
# num3 = int(input('Send a number three: '))
# 
# if num1 >= num2 and num1 >= num3:
#     print(f'Number 1 "{num1}" is the larger!')
# elif num2 >= num1 and num2 >= num3:
#     print(f'Number 2 "{num2}" is the larger!')
# elif num3 >=num1 and num3 >= num2:
#     print(f'Number 3 "{num3}" is the larger!')
# else:
#     print('The numers are the same')

# 7. Age category
# 
# try:
#     age = int(input('Send your age: '))
#     if age > 0 and age <= 12:
#         print('You are a kid!')
#     elif age >= 13 and age <= 17:
#         print('You are a adolescent!')
#     elif age >= 18 and age <= 64:
#         print('You are a adult!')
#     elif age >= 65:
#         print('You are a old human!')
#     else: 
#         print('Value invalid.')
# except ValueError:
#     print('Value invalid, only numbers.')

# 8. Score classify 
# 
# score = float(input('Set you grade: '))
# 
# if score >= 9 and score <= 10:
#     print('Grade: A')
# elif score >= 7 and score <= 8.9:
#     print('Grade: B')
# elif score >= 5 and score <= 6.9:
#     print('Grade: C')
# elif score >= 0 and score < 5:
#     print('Grade: D')
# else:
#     print('Score invalid.')

# 9. To check divisibility for 3 and 5
# 
# numberDibisibility = float(input('Enter a number to check dibisibility by 3 and 5: '))
# 
# if numberDibisibility % 3 == 0 and numberDibisibility % 5 == 0:
#     print(f'This number "{numberDibisibility}" is divisible for 3 and 5.')
# elif numberDibisibility % 3 == 0:
#     print(f'Number "{numberDibisibility}" is only divisible by 3.')
# elif numberDibisibility % 5 == 0:
#     print(f'Number "{numberDibisibility}" is only divisible by 5.')
# else:
#     print('Nothing number is divisible between 3 and 5.')

# 10. Calcule salary bonus
# 
# salary = int(input('Enter your salary: '))
# workingTime = int(input('Enter your working time: '))
# 
# if workingTime > 5:
#     bonusSalary = salary * 0.10
#     print(f'You coop on this work project earns an extra bonus, your new salary is "{salary + bonusSalary}"')

# 11. Calcule salary increase
# 
# salary = int(input('Enter your salary: '))
# 
# if salary <= 1000:
#     print(f'{salary * 1.2:.2f}')
# elif salary > 1000 and salary <= 2000:
#     print(f'{salary * 1.1:.2f}')
# elif salary > 2000:
#     print(f'{salary * 1.05:.2f}')

# 12. To check leap year
# 
# year = int(input('Digit one year: '))
# 
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         print(f'This year "{year}" is bissextile!')
# else:
#     print(f'This year "{year}" is not a bissextile.')

# 13. Calcule discount value
# 
# value = int(input('Product value: '))
# 
# if value >= 100 and value <= 500:
#     print(f'New value is {value*0.95}.')
# elif value > 500 and value <= 1000:
#     print(f'New value is {value*0.90}.')
# elif value > 1000:
#     print(f'New value is {value*0.85}.')
# elif value < 100:
#     print('It dont have a discount')
# else:
#     print('Incorrect value.')

# 14. To check validity password

password = str(input('Digit your password: '))
haveUpperCase = False
haveDigit = False
haveCharacterSpecial = False

for c in password:
    if c.isupper():
        haveUpperCase = True
    if c.isdigit():
        haveDigit = True
    if c in '!@#$%¨&*()_+=-':
        haveCharacterSpecial = True

if len(password) >= 8 and haveUpperCase and haveDigit and haveCharacterSpecial:
    print(f'This password "{password}" is STRONG!')
else:
    print(f'This password "{password}" is weak.')