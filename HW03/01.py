
lst = [2, 3, 4, 5, 6] 
lstMulti = []
start = 0
length = len(lst)-1

while start < length:
    lstMulti.append(lst[start] * lst[length])
    start+=1
    length-=1
    if start==length:
        lstMulti.append(lst[start] ** 2)

print(f'The list {lstMulti}')


# lst = [2, 3, 4, 5, 6] 
# lstMulti = []
# length = len(lst)-1

# for i in range(0,length):
#     lstMulti.append(lst[i] * lst[length])
#     length-=1
#     if i==length:
#         lstMulti.append(lst[i] ** 2)
#         break                    #Как остановить цикл for после достижения условия if?  
# print(f'The list {lstMulti}')


# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# cMiddle element into sqr