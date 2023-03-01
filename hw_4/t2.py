import os
os.system('cls')

import random
n = int(input("Введите количество кустов: "))
berries = [random.randint(0, 50) for _ in range(n)]
print(berries)
berries.extend([berries[0], berries[1]])
# print(berries)
max_sum = 0
for i in range(len(berries) - 2):
    triple_sum = berries[i] + berries[i + 1] + berries[i + 2]
    # print(triple_sum)
    if triple_sum > max_sum:
        max_sum = triple_sum
# print()
print(max_sum)



# def max_berries(arr):
#     max_sum = 0
#     for i in range(len(arr)):
#         curr_sum = arr[i] + arr[(i-1) % len(arr)] + arr[(i+1) % len(arr)]
#         if curr_sum > max_sum:
#             max_sum = curr_sum
#     return max_sum
    
# arr = [int(x) for x in input().split()] 
# print(max_berries(arr))


# n = int(input())
# arr = list()
# for i in range(n):
#     x = int (input())
#     arr.append(x)
# arr_count = list()
# for i in range(len(arr) - 1):
#     arr_count.append(arr[i - 1] + arr[i] + arr[i + 1])
# arr_count.append(arr[-2] + arr[-1] + arr[0])
# print(max(arr_count))
