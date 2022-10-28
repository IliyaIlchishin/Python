num = int(input('Введите натурально число '))
multipliers = []
start = 2

while num > 1:
    if num % start == 0:
        multipliers.append(start)
        num = num / start
    else:
        start+=1
print(multipliers)


# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# N = 6 | N = 12 | 32 | 13 | 9 | 18 | 21
# 2 * 3 | 2 * 2 * 3 | 2 * 2 * 2 * 2 * 2 | 13 | 3 * 3 | 2 * 3 * 3 | 3*7

