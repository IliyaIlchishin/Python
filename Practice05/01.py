with open ('/Users/iliyailchishin/Desktop/GB/Q2/Python/Practice05/file.txt', 'r') as file:
    print(file.readline ())
    data = list(map(int,(file.readline ().split ())))
    print(data)

    # # (file.read())
    # print(data)


# data = f.read() + ' '

# 1) В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.
# Пример: 1 2 3 5 6 7
# Вывод: 4
# with open("file.txt", "p") as file:
# spisok = list (map(int, (file.readline ().split ())))
# print (spisok)
# for i in range(Men (spisok)):
# if spisok il - 1 != spisok™i-11:
# print (spisok[i])