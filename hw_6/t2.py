import os
os.system('cls')



import random
n = int(input("Введите размерность массива: "))
arr = [random.randint(0, 10) for _ in range(n)]
print(arr)

low = int(input("Введите минимум: "))
high = int(input("Введите максимум: "))

indices = []

for i in range(len(arr)):
    if low <= arr[i] <= high:
        indices.append(i)

print(f'Индексы: {indices}')