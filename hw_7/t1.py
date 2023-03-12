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
    else:
        return "Ритма нет. Пам парам"

poem = "пара-ра-рам рам-пам-папам па-ра-па-дам"
print(rhythm(poem))
poem = "ЕХАЛ грека через реку. Видит грека  "
print(rhythm(poem))
