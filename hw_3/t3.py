import os
os.system('cls')

word_0 = input('Введите слово: ')
word = word_0.upper()
score = 0
for letter in word:
    if letter in 'AEIOULNSTR':
        score += 1
    elif letter in 'DG':
        score += 2
    elif letter in 'BCMP':
        score += 3
    elif letter in 'FHVWY':
        score += 4
    elif letter in 'K':
        score += 5
    elif letter in 'JX':
        score += 8
    elif letter in 'QZ':
        score += 10

    elif letter in 'АВЕИНОРСТ':
        score += 1
    elif letter in 'ДКЛМПУ':
        score += 2
    elif letter in 'БГЁЬЯ':
        score += 3
    elif letter in 'ЙЫ':
        score += 4
    elif letter in 'ЖЗХЦЧ':
        score += 5
    elif letter in 'ШЭЮ':
        score += 8
    elif letter in 'ФЩЪ':
        score += 10
print(f'Очки за слово {word_0}: {score}.')


# score = {"a": 1, "я": 3}
# total = 0
# def scrub_sc(word):
#     return sum(score.get(letter, 0) for letter in word.lower())
# print(scrub_sc(input('Enter the word: ')))

# slvr = {1: 'AETOULNSTRABEMHOPCT', 2: 'DGIKIMIYБЛО', 10: 'QQERHJBТГОРЕАП'}
# slovo = input()
# result = 0
# for i in slovo:
#     for key in slvr:
#         if i.upper() in slvr[key]:
#             result += key
# print(result)
