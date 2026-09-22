# 1. Write a program that checks whether a character is a vowel or a consonant
def vowelConsoant(character):
    if character.isalpha() and len(character) == 1:
        if character.upper() in 'AEIOU':
            return print('is vowel')
        if character.upper() in 'BCDFGHJKLMNPQRSTVWXYZ':
            return print('is consonant')
    else:
        print('Something sendend isnt one character')
vowelConsoant('bb')