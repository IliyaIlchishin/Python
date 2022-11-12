
def sum(lst):
    n_sum=0
    for i in lst: n_sum += i
    return  int(n_sum)

number = list(map(int,str(input('Please enter number '))))
print(sum(number))

# def sumdigits(num):
#     return sum(map(int, num.replace('.','').replace('-', "")))

# num = input('Введите любое вещественное число: ') 
# print(f'Сумма цифр в этом числе равна {sumdigits(num)}')


# 3) Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0, 56 -> 11

