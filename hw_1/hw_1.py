import os
clear = lambda: os.system('cls')
clear()

# --------------------------------------------------------------------------------------------------------------
# Задача 2: Найдите сумму цифр трехзначного числа.

# i = int(input('Введите трёхзначное число: '))

# print('╔════════════════════════════════')
# if 100 <= i <= 999:
#     sum = i//100 + (i//10)%10 + i%10
#     print(f'║ Сумма цифр вашего числа {i} есть число {sum}.')
# else:
#     print('║ Введите ТРЁХЗНАЧНОЕ число!')
# print('╚════════════════════════════════')


# --------------------------------------------------------------------------------------------------------------
# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они 
# сделали S журавликов. Сколько журавликов сделал каждый ребенок, если 
# известно, что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# i = int(input('Введите общее количество журавликов: '))

# print('╔════════════════════════════════')
# if i % 6 == 0 and i >= 0:
#     print(f'║ Количество журавликов, сделанных Петей: {int(i / 6)}.')
#     print(f'║ Количество журавликов, сделанных Катей: {int(4 * i / 6)}.')
#     print(f'║ Количество журавликов, сделанных Серёжей: {int(i / 6)}.')
# else:
#     print('║ Не могут дети так сделать...')
# print('╚════════════════════════════════')


# --------------------------------------------------------------------------------------------------------------
# Задача 6: Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с
#  номером. Счастливым билетом называют такой билет с шестизначным 
#  номером,  где сумма первых трех цифр равна сумме последних трех. 
#  Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.

# i = int(input('Введите номер вашего билета: '))

# print('╔════════════════════════════════')
# if i < 100000 or i > 999999:
#     print('║ Необходим ШЕСТИЗНАЧНЫЙ номер билета!')
# elif i // 100000 + (i // 10000) % 10 + (i // 1000) % 10 == (i // 100) % 10 + (i // 10) % 10 + i % 10:
#     print('║ Поздравляем! У вас счастливый билет!')
# else:
#     print('║ Увы! У вас несчастливый билет...')
# print('╚════════════════════════════════')


# --------------------------------------------------------------------------------------------------------------
# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек 
# отломить k долек, если разрешается сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника).

# n = int(input('Введите количество долек вашей шоколадки по горизонтали: '))
# m = int(input('Введите количество долек вашей шоколадки по вертикали: '))
# k = int(input('Введите желаемое количество отломленных долек: '))

# print('╔════════════════════════════════')
# i = 1
# j = 1
# if k < n * m and (k % n == 0 or k % m == 0):
#     print('║ Да, так можно разломать шоколадку.')
# else:
#     print('║ Нет,так нельзя разломать шоколадку.')
# print('╚════════════════════════════════')
