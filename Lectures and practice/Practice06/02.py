

def uniquevalues(list):
    unique = []
    for i in range (len(list)):
        if list[i] not in unique:
            unique.append(list[i])
        else:
            unique.remove(list[i])
    return unique

numbers = [2,8,5,9,3,6,2,12,31,4,3]
unique = uniquevalues(numbers)
print(unique)




# Дана последовательность чисел. 
# Получить список уникальных элементов заданной последовательности. Без использования count()
