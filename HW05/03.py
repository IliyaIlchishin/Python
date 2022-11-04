with open("encoded.txt", "r") as file:
    data = str(file.readline ())
    print (data)


def compressed(data):
    compressed = ''
    count = 1
    char = data[0]
    for i in range(1, len(data)):
        if data[i] == char:
            count+=1
        else:
            compressed = compressed +str(count)+char
            char=data[i]
            count = 1
    return compressed


def decompressed(data):
    decompressed = ''
    char = ''
    digit = 0
    for i in range(len(data)):
        if data[i].isdigit():
            digit = data[i]
            char += data[i]
        else: 
            decompressed += data[i] * int(digit)
        char = ''
    print(decompressed)

    return decompressed

encoded = compressed(data)
print(encoded)
decoded = decompressed(encoded)
print(decoded)


# # Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# # stroka = "aaabbbbccbbb"
# # ....
# # stroka = "3a4b2c3b"
