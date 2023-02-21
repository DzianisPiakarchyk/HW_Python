import os
os.system('cls')

# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих 
# чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

from math import sqrt 
s = int(input("Введите сумму чисел: "))
p = int(input("Введите произведение чисел: "))
print('╔════════════════════════════════')
if 1 <= s <= 1000 and 1 <= p <= 1000:
    x = (s - sqrt(abs(s * s -4 * p))) / 2
    y = (s + sqrt(abs(s * s -4 * p))) / 2
    if s * s -4 * p >= 0 and sqrt(s * s -4 * p) % 1 == 0:
        print(f'║ {int(x)} {int(y)}')
    else:
        print('║ Такого не бывает!')    
else:
    print('║ Ограничение на ввод!')
print('╚════════════════════════════════')

# x = int(input())
# y = int(input())
# for i in range(x):
#     for j in range(y):
#         if x == i + j and y == i * j:
#             print(i, j)
