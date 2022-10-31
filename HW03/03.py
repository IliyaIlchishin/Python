
# num = int(input('Please enter any decimal number 3'))
# binary = ''
 
# while num > 0:
#     binary = str(num % 2) + binary
#     num = num // 2
 
# print(binary)


# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def DecToBinary(num):
    binary=[]
    while num>0:
        if num%2==0:
            binary.append(0)
        else:
            binary.append(1)
        num = num//2
    return binary

binary = DecToBinary(45)
print(binary)


