# Требуется найти наименьший натуральный делитель целого числа N, отличный от 1.
# Пример:
# - Для n = 15:  Ответ: 3
# - Для n = 35:  Ответ: 5


n = int(input('Please enter the number: ')) 
print(n)
i=1
while i<n:
    if n % i == 0:
        devider = i
        i+=i
    else:
        i=i+1
print(f'The minimal devider is {devider}') 





