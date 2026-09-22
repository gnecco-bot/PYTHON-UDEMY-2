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