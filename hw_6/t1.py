import os
os.system('cls')

a = int(input("Введите начальный член прогрессии: "))
d = int(input("Введите разность прогрессии: "))
n = int(input("Введите количество членов прогрессии: "))


progression = [0] * n
for i in range(n):
    progression[i] = a + i * d
print(progression)


progression = []
for i in range(n):
    progression.append(a + i * d)
print(progression)


progression = [a]
for i in range(1, n):
    progression.append(progression[i - 1] + d)  
print(progression)


def ar_progression(array, a, d, n):
    if n == 0:
        return
    ar_progression(array, a, d, n-1)
    array[n-1] = a + (n-1) * d

arr = [0] * n
ar_progression(arr,a, d, n)
print(arr)
