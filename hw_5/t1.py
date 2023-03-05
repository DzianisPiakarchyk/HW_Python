import os
os.system('cls')





a = int(input("Введите основание степени: "))
b = int(input("Введите показатель степени: "))

def power(base, exp):
    if base == 0 and exp == 0:
        return f'[степень не определена]'
    if exp == 0:
        return 1
    if base == 1:
        return 1
    if base != -1 and exp < 0:
        return f'[введите, пожалуйста, неотрицательное значение показателя степени]'
    if base == -1 and abs(exp) % 2 == 0:
        return 1
    if base == -1 and abs(exp) % 2 != 0:
        return -1
    if exp == 1:
        return base
    else:
        return base * power(base, exp - 1)

print()
print(f'{a} ^ {b} = {power(a, b)}')