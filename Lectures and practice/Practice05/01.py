with open("file.txt", "r") as file:
    data = list (map(int, (file.readline ().split ())))
    print (data)

    for i in range(1,len(data)): 
        if data[i]-1 != data[i-1]:
            print(f'the missing element is {data[i]-1}')

# 1) В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.
# Пример: 1 2 3 5 6 7
# Вывод: 4
