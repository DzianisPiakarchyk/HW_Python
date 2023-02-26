import os
os.system('cls')

import random
n = int(input("Введите количество сгенерированных чисел: "))
arr = [random.randint(0, 6) for _ in range(n)]
print(arr)
X = int(input("Введите проверяемое число: "))
count = 0
for i in range(n):     # for i in arr:
    if arr[i] == X:    # if i == X:
        count += 1
print(f'Число {X} встречается в списке вот столько раз: {count}.')
