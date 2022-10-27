
# lst = [2, 3, 4, 5, 6] 
# lstMulti = []
# start = 0
# length = len(lst)-1

# while start < length:
#     lstMulti.append(lst[start] * lst[length])
#     start+=1
#     length-=1
#     if start==length:
#         lstMulti.append(lst[start] ** 2)

# print(f'The list {lstMulti}')


def mult_two_num():
    lst = list(map(int,input('Введите числа через запятую: ').split(','))) # lst = [int(i) for i in input('#').split(' ')]
    newlst = []
    for i in range( (len(lst) + 1) // 2): 
        newlst.append(lst[i] * lst[- 1 - i])
    print(f'Произведение пар чисел списка: {newlst}')

mult_two_num()

# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# cMiddle element into sqr