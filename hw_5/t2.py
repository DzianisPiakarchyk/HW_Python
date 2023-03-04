import os
os.system('cls')



a = int(input("Введите первое слагаемое: "))
b = int(input("Введите второе слагаемое: "))

def sum(a, b):
    if b == 0:
        return a
    else:
        return sum(a + 1, b - 1)

print(sum(a, b))
