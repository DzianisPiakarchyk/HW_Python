import os
os.system('cls')

import random
n = int(input("Введите количество сгенерированных чисел: "))
arr = [random.randint(0, 6) for _ in range(n)]
print(arr)
X = int(input("Введите проверяемое число: "))
min_diff = abs(arr[0] - X)
closest_num = arr[0]
for i in arr:
#     if abs(arr[i] - X) < min_diff:
#         min_diff = abs(arr[i] - X)
      if min_diff > (min_diff := abs(arr[i] - X)):
        closest_num = arr[i]
print(closest_num)
