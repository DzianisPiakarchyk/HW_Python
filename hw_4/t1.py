import os
os.system('cls')

import random
n = int(input("Введите количество элементов первого множества: "))
arr1 = [random.randint(0, 20) for _ in range(n)]
print(arr1)
m = int(input("Введите количество элементов второго множества: "))
arr2 = [random.randint(0, 20) for _ in range(m)]
print(arr2)

list_1 = set(arr1)
list_2 = set(arr2)

result = sorted([i for i in list_1 if i in list_2])
print('Общие элементы множеств:')
print(*result, sep=', ')



# mol = [int(x) for x in input().split()]
# n = mol[0]
# m = mol[1]
# set_1 = set()
# set_2 = set()
# list_1 = list()
# a = [int(x) for x in input().split()]
# k = set(a)
# for i in k:
#     set_1.add(i)
# b = [int(x) for x in input().split()]
# k1 = set(b)
# for i in k1:
#     set_2.add(i)
# lok = set_1 & set_2
# kool = list(lok)
# kool.sort()
# for i in kool:
#     print(i, end=' ')
