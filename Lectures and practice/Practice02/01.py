

numbers = [int(i) for i in input('Please enter numbers separated by empty space " " ').split()]
maxnum = numbers[0]
for num in numbers:
    if num > maxnum:
        maxnum = num
print (f'Max number is {maxnum}')



# Задание 1

# Найти Максимальный элемент в списке из 5 элементов. (Не используя встроенные функции)
# *Пример*
# | Ввод: 3 -6 10 23 -14
# Ответ: 23
