
num = int(input('Please enter any decimal number 3'))
binary = ''
 
while num > 0:
    binary = str(num % 2) + binary
    num = num // 2
 
print(binary)


# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10