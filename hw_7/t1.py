import os
os.system('cls')



def rhythm(poems):
    separated = poems.lower().split()
    vowels = []
    for word in separated:
        same_vowels = len([i for i in word if i in 'ёуеыаоэяию'])
        vowels.append(same_vowels)
    if len(set(vowels)) == 1:
        return "Ритм есть. Парам пам-пам"
    return "Ритма нет. Пам парам"

poem = "пара-ра-рам рам-пам-папам па-ра-па-дам"
print(rhythm(poem))
poem = "ЕХАЛ грека через реку. Видит грека  "
print(rhythm(poem))


# def rifma(words):
#     return len(set(map(lambda x: sum(1 for i in x if i in 'ёуеыаоэяию'), words))) == 1

# chant = str(input('Введите текст: ')).lower().split()
# if rifma(chant):
#     print('Ритм есть. Парам пам-пам')
# else:
#     print('Ритма нет. Пам парам')
