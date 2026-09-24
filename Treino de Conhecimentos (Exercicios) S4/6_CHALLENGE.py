# 1. Write a program that checks whether a character is a vowel or a consonant
# def vowelConsoant(character):
#     if character.isalpha() and len(character) == 1:
#         if character.upper() in 'AEIOU':
#             return print('is vowel')
#         if character.upper() in 'BCDFGHJKLMNPQRSTVWXYZ':
#             return print('is consonant')
#     else:
#         print('Something sendend isnt one character')
# vowelConsoant('bb')

# 2. Write a program that reads a number and displays it as the corresponding day of the week.
# def dayWeek(d):
#     days = {
#         1:'Sunday',
#         2:'Monday',
#         3:'Tuesday',
#         4:'Wednesday',
#         5:'Thursday',
#         6:'Friday',
#         7:'Saturday'
#     }
#     if d in days:
#         return f'The day corresponding the number {d} is {days[d]}'
#     else:
#         return 'Invalid number'
# print(dayWeek(2))

# 3. Write a program that asks the user for a grade between zero and ten
# def zeroTen():
#     while True:
#         try:
#             n = float(input('Digit a value between 1 and 10: '))
#             if 0 <= n <= 10:
#                 return n
#             else:
#                 print('Incorrect value, only 1 to 10')
#         except ValueError:
#             print('Incorrect value')

# grade = zeroTen()
# print(f'You entered the correct note: {grade}')

# 4. Write a program that reads an indeterminate number of numbers
# def indeterminateNumber():
#     one_0_25 = 0
#     one_26_50 = 0
#     one_51_75 = 0
#     one_76_100 = 0
#     while True:
#         try:
#             n = int(input('Digit a number between 0 to 100: '))
#             if 0 <= n <= 25:
#                 one_0_25+=1
#             if 26 <= n <= 50:
#                 one_26_50+=1
#             if 51 <= n <= 75:
#                 one_51_75+=1
#             if 76 <= n <= 100:
#                 one_76_100+=1
#             if n < 0:
#                 print(f'0-25: {one_0_25}')
#                 print(f'26-50: {one_26_50}')
#                 print(f'51-75: {one_51_75}')
#                 print(f'76-100: {one_76_100}')
#                 return
#             else:
#                 pass
#         except ValueError:
#             print('Something sended is incorrect, pls check it.') 
# indeterminateNumber()

# 5. Write a programa that reads an array of 10 real numbers and then displays them in reverse order
# def reverseOrder():
#     list = []
#     for i in range(10): 
#         while True:
#             try:        
#                 value = float(input(f'Digit ten numbers (current {i+1}): '))
#                 list.append(value)
#                 break
#             except ValueError:
#                 print('Send a correct value')
#     print('Number lists in reverse order:')
#     for n in reversed(list):
#         print(n)
# reverseOrder()

# 6. Write a program that reads 20 integer and stores them in an array
# def intergerStore():
#     v1 = []
#     vEven = []
#     vOdd = []
#     for i in range(20):
#         try:
#             n = int(input(f'Digit 20 numbers (current {i+1}): '))
#             v1.append(n)
#             if n % 2 == 0:
#                 vEven.append(n)
#             elif n % 2 != 0:
#                 vOdd.append(n)
#         except ValueError:
#             print('You sendend a incorrect value')
#     print('Every numbers: ', v1)
#     print('Only even numbers: ', vEven)
#     print('Only odd numbers: ', vOdd)
# intergerStore()

# 7. Write a program that asks for four grades for 10 students, calculates and stores each student's average in an array, and displays the students with an average greater than or equal to 7.
def calculeAvg():
    medias = []
    students_avg_larger_than_seven = 0
    for i in range(10):
        print(f'Digite the 4 grades for studends {i+1}: ')
        sum_note = 0
        for j in range(4):
            while True:
                try:
                    note = float(input(f'Digit the {j+1} note: '))
                    if 0 <= note <= 10:
                        sum_note += note
                        break
                except ValueError:
                    print('Invalid value')
        media = sum_note / 4
        medias.append(media)
        if media >= 7.0:
            students_avg_larger_than_seven += 1
        print(f'Number the average studends larger or equal 7.0: {students_avg_larger_than_seven}')

calculeAvg()